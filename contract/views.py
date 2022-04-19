import json

import requests
from django.shortcuts import render, redirect
from paycomuz import Paycom
from clickuz import ClickUz
from .models import *
from datetime import datetime
from django.http import JsonResponse
from paycomuz.models import Transaction


def contract_json(request):
    if request.method == 'POST':
        form = request.POST
        csrfmiddlewaretoken = form['csrfmiddlewaretoken']
        amount = form['cost[insurancePremium]']
        contract_json = ContractJson(
            applicant=form['data'],
            csrf=csrfmiddlewaretoken,
            payment_type=form['payment_type']
        )
        contract_json.save()

        if form['payment_type'] == 'Payme':
            paycom = Paycom()
            # amount = int(amount) * 100
            amount = int(amount)
            order_id = form['vehicle[govNumber]'] + " code: " + csrfmiddlewaretoken
            return_url = f"http://195.158.9.252:1338/contract/contract_json_detail/{csrfmiddlewaretoken}/"
            payme_url = paycom.create_initialization(amount=amount, order_id=order_id, return_url=return_url)
            contract_json.payme_url = payme_url
            contract_json.save()
        elif form['payment_type'] == 'Click':
            amount = int(amount)
            order_id = form['vehicle[govNumber]'] + " code: " + csrfmiddlewaretoken
            return_url = f"http://195.158.9.252:1338/contract/contract_json_detail/{csrfmiddlewaretoken}/"
            click_url = ClickUz.generate_url(order_id=order_id, amount=amount, return_url=return_url)
            contract_json.payme_url = click_url
            contract_json.save()

        return redirect('contract_json_payment', csrfmiddlewaretoken)
    return render(request, 'contract/contract_json.html')


def contract_json_payment(request, slug):
    query = ContractJson.objects.filter(csrf=slug).last()
    applicant = json.loads(query.applicant)
    print("applicant= ", applicant)
    payme_url = query.payme_url
    context = {
        "payme_url": payme_url,
        "applicant":applicant
    }
    return render(request, 'contract/contract_json_payment.html', context)


def contract_json_detail(request, slug):
    query = ContractJson.objects.filter(csrf=slug).last()
    applicant = json.loads(query.applicant)
    print(applicant)

    i = 0
    update_drivers = []

    if not "drivers" in applicant:
        applicant["drivers"] = update_drivers
    else:
        while i <= 4:
            if not applicant["drivers"][i]["passportData"]["pinfl"] is "":
                update_drivers.append(applicant["drivers"][i])
            i = i + 1
        applicant["drivers"] = update_drivers

    del applicant["csrfmiddlewaretoken"]
    del applicant["data"]
    del applicant["payment_type"]
    del applicant["startDate"]
    del applicant["endDate"]
    del applicant["region"]
    if "driver" in applicant:
        del applicant["driver"]

    if "select2" in applicant:
        del applicant["select2"]
    del applicant["select3"]
    del applicant["select4"]


    query.applicant_fond = json.dumps(applicant)
    query.save()

    context = {
        "applicant": applicant,
        "query": query,
        "slug": slug
    }
    return render(request, 'contract/contract_json_detail.html', context)


# ajax_posting function
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def ajax_posting(request):
    if is_ajax(request=request):
        slug = request.POST.get('slug', None)  # getting data from first_name input
        query = ContractJson.objects.filter(csrf=slug).last()
        applicant_fond = json.loads(query.applicant_fond)
        unique = applicant_fond["vehicle"]["govNumber"] + " code: " + slug
        transaction = Transaction.objects.filter(order_key=unique).last()

        if query.insuranceFormUuid is None:
            policy_uuid = epolicy_create(applicant_fond)
            if policy_uuid["error"] == 0:
                query.insuranceFormUuid = policy_uuid['result']['uuid']
            else:
                query.insuranceFormUuid = policy_uuid["error_message"]
            query.save()
        else:
            print("uuid olingan")

        if not transaction is None:
            print(transaction.order_key)
            query.transaction_order_key = transaction.order_key
            query.transaction_state = transaction.state
            query.transaction_status = transaction.status
            query.save()

            get_policy = confirm_payed(query, transaction)
            if get_policy["error"] == 0:
                query.policy_seria = get_policy["result"]["seria"]
                query.policy_number = get_policy["result"]["number"]
                query.policy_url = "http://polis.e-osgo.uz/site/export-to-pdf?id=" + query.insuranceFormUuid
            else:
                query.error_message = "error code: " + str(get_policy["error"]) + "error message" + get_policy["error_message"]
            query.save()
        else:
            query.error_message = "To'lov amalga oshirilmagan"
            query.save()

        response = {
            "message": query.error_message,
            "policy_seria": query.policy_seria,
            "policy_number": query.policy_number,
            "policy_url": query.policy_url
        }
        return JsonResponse(response, safe=False)  # return response as JSON


def epolicy_create(applicant):
    get_policy_uuid = requests.post(
        'http://api.e-osgo.uz/api/epolicy/create',
        headers={
            "Authorization": "Bearer YjhhZTFlYzMxYmZlNzRmZDQ5ZDI5OWI2MWY3M2YzYzg1MzMxNWIwYTJhNGZlYWM3Y2IwMWM1YmNlYmY2YTg2NA"},
        json=applicant
    )

    get_policy_uuid.encoding = 'utf-8'
    get_policy_uuid_response = get_policy_uuid.json()

    return get_policy_uuid_response


def confirm_payed(query, transaction):
    insurancePremium = json.loads(query.applicant_fond)["cost"]["insurancePremium"]
    startDate = json.loads(query.applicant_fond)["details"]["startDate"]
    endDate = json.loads(query.applicant_fond)["details"]["endDate"]

    result_payed = {
        "insuranceFormUuid": query.insuranceFormUuid,
        "paymentDate": datetime.utcfromtimestamp(int(transaction.perform_datetime) / 1000).strftime('%Y-%m-%d'),
        "insurancePremiumPaidToInsurer": insurancePremium,
        "startDate": startDate,
        "endDate": endDate
    }

    get_policy = requests.post(
        'http://api.e-osgo.uz/api/epolicy/confirm-payed',
        headers={
            "Authorization": "Bearer YjhhZTFlYzMxYmZlNzRmZDQ5ZDI5OWI2MWY3M2YzYzg1MzMxNWIwYTJhNGZlYWM3Y2IwMWM1YmNlYmY2YTg2NA"},
        json=result_payed
    )

    get_policy.encoding = 'utf-8'
    get_policy_response = get_policy.json()

    return get_policy_response
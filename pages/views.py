from django.shortcuts import render
import json
# Create your views here.
from contract.models import ContractJson
from paycomuz.models import Transaction


def index(request):
    slug="tyQDaZS8Q4olFjnRFHqFdATYyVKY0uO9OOwqx3JUJWzKfkpOcojxIbUzwLdEzKzQ"
    query = ContractJson.objects.filter(csrf=slug).last()
    applicant = json.loads(query.applicant)
    # print(applicant["vehicle"]["govNumber"])
    # print(applicant["details"]["startDate"])
    unique = applicant["vehicle"]["govNumber"] + " " + applicant["details"]["startDate"]
    transaction = Transaction.objects.filter(order_key=unique).last()
    return render(request, 'pages/index.html')
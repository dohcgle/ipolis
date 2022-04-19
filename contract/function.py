import json
from datetime import datetime


# jismoniy cheklangan start

def limit_jismoniy(form_data):
    applicant = {}
    print(form_data)
    personData = json.loads(form_data['personData'])
    print(type(personData))

    print(type(personData['gender']))

    if str(personData['gender'] ) == '1':
        gender = 'm'
    elif str(personData['gender']) == '0':
        gender = 'f'

    if 'applicantIsOwner' in form_data:
        if form_data['applicantIsOwner'] == 'on':
            applicantIsOwner = True
    else:
        applicantIsOwner = False

    sumInsured = 40000000

    if form_data['KT'] == '1.4':
        useTerritoryId = '1'
    elif form_data['KT'] == '1':
        useTerritoryId = '2'

    vehicleData = json.loads(form_data['vehicleData'])

    vehicle_issueDate = datetime.fromisoformat(vehicleData['techPassportIssueDate'])
    vehicle_issueDate = datetime.strftime(vehicle_issueDate, '%Y-%m-%d')


    person = {
        "passportData": {
            "pinfl": form_data['pinfl'],
            "seria": form_data['passportSeries'],
            "number": form_data['passportNumber'],
            "issuedBy": personData['issuedBy'],
            "issueDate": personData['startDate']
        },
        "fullName": {
            "firstname": personData['firstNameLatin'],
            "lastname": personData['lastNameLatin'],
            "middlename": personData['middleNameLatin']
        },
        "phoneNumber": form_data['phone'],
        "gender": gender,
        "birthDate": personData['birthDate'],
        "regionId": str(personData['regionId']),
        "districtId": str(personData['districtId'])
    }
    organization = None
    address = form_data['address']
    email = form_data['email']
    owner = {
        "person": {
            "passportData": {
                "pinfl": form_data['pinfl'],
                "seria": form_data['passportSeries'],
                "number": form_data['passportNumber'],
                "issuedBy": personData['issuedBy'],
                "issueDate": personData['startDate']
            },
            "fullName": {
                "firstname": personData['firstNameLatin'],
                "lastname": personData['lastNameLatin'],
                "middlename": personData['middleNameLatin']
            }
        },
        "organization": None,
        "applicantIsOwner": applicantIsOwner
    }
    details = {
        "issueDate": form_data['startDate'],
        "startDate": form_data['startDate'],
        "endDate": form_data['endDate'],
        "driverNumberRestriction": True,
        "specialNote": "Qayta chiqarish",
        "insuredActivityType": form_data['insuredActivityType']
    }
    cost = {
        "discountId": "1",
        "discountSum": "0",
        "insurancePremium": str(form_data['insurancePremium']),
        "sumInsured": str(sumInsured),
        "contractTermConclusionId": "1",
        "useTerritoryId": str(useTerritoryId),
        "commission": "0",
        "insurancePremiumPaidToInsurer": "0",
        "seasonalInsuranceId": "1"
    }
    vehicle = {
        "techPassport": {
            "number": form_data['techPassportSeria'],
            "seria": form_data['techPassportNumber'],
            "issueDate": vehicle_issueDate
        },
        "modelCustomName": vehicleData['modelName'],
        "engineNumber": vehicleData['engineNumber'],
        "typeId": str(vehicleData['vehicleTypeId']),
        "issueYear": str(vehicleData['issueYear']),
        "govNumber": vehicleData['govNumber'],
        "bodyNumber": vehicleData['bodyNumber'],
        "regionId": personData['regionId']
    }


    # # START DRIVERS 1
    driver1_person_data = json.loads(form_data['driver1_person_data'])

    driver1_data = json.loads(form_data['driver1_data'])
    licenseIssueDate1 = datetime.fromisoformat(driver1_data['issueDate'])
    licenseIssueDate1 = licenseIssueDate1.strftime('%Y-%m-%d')

    driver1 = {
        "passportData": {
            "pinfl": form_data['driver1_pinfl'],
            "seria": form_data['driver1_passportSeries'],
            "number": form_data['driver1_passportNumber'],
            "issuedBy": driver1_person_data['issuedBy'],
            "issueDate": driver1_person_data['startDate']
        },
        "fullName": {
            "firstname": driver1_person_data['firstNameLatin'],
            "lastname": driver1_person_data['lastNameLatin'],
            "middlename": driver1_person_data['middleNameLatin']
        },
        "licenseNumber": form_data['driver1_lic_number'],
        "licenseSeria": form_data['driver1_lic_seria'],
        "relative": int(form_data['driver1_rlt']),  # togrlash kk
        "birthDate": form_data['driver1_birthDate'],
        "licenseIssueDate": licenseIssueDate1
    }


    # # END DRIVERS 1

    # # START DRIVERS 2
    print(form_data)

    driver2_person_data = json.loads(form_data['driver2_person_data'])

    driver2_data = json.loads(form_data['driver2_data'])
    licenseIssueDate2 = datetime.fromisoformat(driver2_data['issueDate'])
    licenseIssueDate2 = licenseIssueDate2.strftime('%Y-%m-%d')

    driver2 = {
        "passportData": {
            "pinfl": form_data['driver2_pinfl'],
            "seria": form_data['driver2_passportSeries'],
            "number": form_data['driver2_passportNumber'],
            "issuedBy": driver2_person_data['issuedBy'],
            "issueDate": driver2_person_data['startDate']
        },
        "fullName": {
            "firstname": driver2_person_data['firstNameLatin'],
            "lastname": driver2_person_data['lastNameLatin'],
            "middlename": driver2_person_data['middleNameLatin']
        },
        "licenseNumber": form_data['driver2_lic_number'],
        "licenseSeria": form_data['driver2_lic_seria'],
        "relative": int(form_data['driver2_rlt']),  # togrlash kk
        "birthDate": form_data['driver2_birthDate'],
        "licenseIssueDate": licenseIssueDate2
    }


    # # END DRIVERS 2

    # # START DRIVERS 3
    driver3_person_data = json.loads(form_data['driver3_person_data'])

    driver3_data = json.loads(form_data['driver3_data'])
    licenseIssueDate3 = datetime.fromisoformat(driver3_data['issueDate'])
    licenseIssueDate3 = licenseIssueDate3.strftime('%Y-%m-%d')

    driver3 = {
        "passportData": {
            "pinfl": form_data['driver3_pinfl'],
            "seria": form_data['driver3_passportSeries'],
            "number": form_data['driver3_passportNumber'],
            "issuedBy": driver3_person_data['issuedBy'],
            "issueDate": driver3_person_data['startDate']
        },
        "fullName": {
            "firstname": driver3_person_data['firstNameLatin'],
            "lastname": driver3_person_data['lastNameLatin'],
            "middlename": driver3_person_data['middleNameLatin']
        },
        "licenseNumber": form_data['driver3_lic_number'],
        "licenseSeria": form_data['driver3_lic_seria'],
        "relative": int(form_data['driver3_rlt']),
        "birthDate": form_data['driver3_birthDate'],
        "licenseIssueDate":licenseIssueDate3
    }


    # # END DRIVERS 3


    # # START DRIVERS 4
    driver4_person_data = json.loads(form_data['driver4_person_data'])

    driver4_data = json.loads(form_data['driver4_data'])
    licenseIssueDate4 = datetime.fromisoformat(driver4_data['issueDate'])
    licenseIssueDate4 = licenseIssueDate4.strftime('%Y-%m-%d')

    driver4 = {
        "passportData": {
            "pinfl": form_data['driver4_pinfl'],
            "seria": form_data['driver4_passportSeries'],
            "number": form_data['driver4_passportNumber'],
            "issuedBy": driver4_person_data['issuedBy'],
            "issueDate": driver4_person_data['startDate']
        },
        "fullName": {
            "firstname": driver4_person_data['firstNameLatin'],
            "lastname": driver4_person_data['lastNameLatin'],
            "middlename": driver4_person_data['middleNameLatin']
        },
        "licenseNumber": form_data['driver4_lic_number'],
        "licenseSeria": form_data['driver4_lic_seria'],
        "relative": int(form_data['driver4_rlt']),
        "birthDate": form_data['driver4_birthDate'],
        "licenseIssueDate": licenseIssueDate4
    }


    # # END DRIVERS 4


    # # START DRIVERS 5
    driver5_person_data = json.loads(form_data['driver5_person_data'])

    driver5_data = json.loads(form_data['driver5_data'])
    licenseIssueDate5 = datetime.fromisoformat(driver5_data['issueDate'])
    licenseIssueDate5 = licenseIssueDate5.strftime('%Y-%m-%d')

    driver5 = {
        "passportData": {
            "pinfl": form_data['driver5_pinfl'],
            "seria": form_data['driver5_passportSeries'],
            "number": form_data['driver5_passportNumber'],
            "issuedBy": driver5_person_data['issuedBy'],
            "issueDate": driver5_person_data['startDate']
        },
        "fullName": {
            "firstname": driver5_person_data['firstNameLatin'],
            "lastname": driver5_person_data['lastNameLatin'],
            "middlename": driver5_person_data['middleNameLatin']
        },
        "licenseNumber": form_data['driver5_lic_number'],
        "licenseSeria": form_data['driver5_lic_seria'],
        "relative": int(form_data['driver5_rlt']),  # togrlash kk
        "birthDate": form_data['driver5_birthDate'],
        "licenseIssueDate":licenseIssueDate5
    }

    # # END DRIVERS 5
    drivers = []
    drivers.append(driver1)
    drivers.append(driver2)
    drivers.append(driver3)
    drivers.append(driver4)
    drivers.append(driver5)
    # print('drivers' ,drivers)

    applicant['applicant'] = {}
    applicant['applicant']['person'] = person
    applicant['applicant']['organization'] = organization
    applicant['applicant']['address'] = address
    applicant['applicant']['email'] = email
    applicant['owner'] = owner
    applicant['details'] = details
    applicant['cost'] = cost
    applicant['vehicle'] = vehicle
    applicant['drivers'] = drivers

    # print(applicant)
    return applicant

# jismoniy cheklangan end


# jismoniy cheklanmagan start

def unlimit_jismoniy(form_data):
    applicant = {}
    print(form_data)
    driver_vip_person_data = json.loads(form_data['driver_vip_person_data'])
    print(type(driver_vip_person_data))

    print(type(driver_vip_person_data['gender']))

    if str(driver_vip_person_data['gender'] ) == '1':
        gender = 'm'
    elif str(driver_vip_person_data['gender']) == '0':
        gender = 'f'

    if 'applicantIsOwner' in form_data:
        if form_data['applicantIsOwner'] == 'on':
            applicantIsOwner = True
    else:
        applicantIsOwner = False

    sumInsured = 40000000

    if form_data['KT'] == '1.4':
        useTerritoryId = '1'
    elif form_data['KT'] == '1':
        useTerritoryId = '2'

    vehicleData = json.loads(form_data['vehicleData'])

    vehicle_issueDate = datetime.fromisoformat(vehicleData['techPassportIssueDate'])
    vehicle_issueDate = datetime.strftime(vehicle_issueDate, '%Y-%m-%d')


    person = {
        "passportData": {
            "pinfl": form_data['pinfl'],
            "seria": form_data['passportSeries'],
            "number": form_data['passportNumber'],
            "issuedBy": driver_vip_person_data['issuedBy'],
            "issueDate": driver_vip_person_data['startDate']
        },
        "fullName": {
            "firstname": driver_vip_person_data['firstNameLatin'],
            "lastname": driver_vip_person_data['lastNameLatin'],
            "middlename": driver_vip_person_data['middleNameLatin']
        },
        "phoneNumber": form_data['phone'],
        "gender": gender,
        "birthDate": driver_vip_person_data['birthDate'],
        "regionId": str(driver_vip_person_data['regionId']),
        "districtId": str(driver_vip_person_data['districtId'])
    }
    organization = None
    address = form_data['address']
    email = form_data['email']
    owner = {
        "person": {
            "passportData": {
                "pinfl": form_data['pinfl'],
                "seria": form_data['passportSeries'],
                "number": form_data['passportNumber'],
                "issuedBy": driver_vip_person_data['issuedBy'],
                "issueDate": driver_vip_person_data['startDate']
            },
            "fullName": {
                "firstname": driver_vip_person_data['firstNameLatin'],
                "lastname": driver_vip_person_data['lastNameLatin'],
                "middlename": driver_vip_person_data['middleNameLatin']
            }
        },
        "organization": None,
        "applicantIsOwner": applicantIsOwner
    }
    details = {
        "issueDate": form_data['startDate'],
        "startDate": form_data['startDate'],
        "endDate": form_data['endDate'],
        "driverNumberRestriction": True,
        "specialNote": "Qayta chiqarish",
        "insuredActivityType": form_data['insuredActivityType']
    }
    cost = {
        "discountId": "1",
        "discountSum": "0",
        "insurancePremium": str(form_data['insurancePremium']),
        "sumInsured": str(sumInsured),
        "contractTermConclusionId": "1",
        "useTerritoryId": str(useTerritoryId),
        "commission": "0",
        "insurancePremiumPaidToInsurer": "0",
        "seasonalInsuranceId": "1"
    }
    vehicle = {
        "techPassport": {
            "number": form_data['techPassportSeria'],
            "seria": form_data['techPassportNumber'],
            "issueDate": vehicle_issueDate
        },
        "modelCustomName": vehicleData['modelName'],
        "engineNumber": vehicleData['engineNumber'],
        "typeId": str(vehicleData['vehicleTypeId']),
        "issueYear": str(vehicleData['issueYear']),
        "govNumber": vehicleData['govNumber'],
        "bodyNumber": vehicleData['bodyNumber'],
        "regionId": str(driver_vip_person_data['regionId'])
    }


    # # START DRIVERS 1
    driver_vip_person_data = json.loads(form_data['driver_vip_person_data'])

    driver_vip_data = json.loads(form_data['driver_vip_data'])
    licenseIssueDate1 = datetime.fromisoformat(driver_vip_data['issueDate'])
    licenseIssueDate1 = licenseIssueDate1.strftime('%Y-%m-%d')

    driver1 = {
        "passportData": {
            "pinfl": form_data['driver_vip_pinfl'],
            "seria": form_data['driver_vip_passportSeries'],
            "number": form_data['driver_vip_passportNumber'],
            "issuedBy": driver_vip_person_data['issuedBy'],
            "issueDate": driver_vip_person_data['startDate']
        },
        "fullName": {
            "firstname": driver_vip_person_data['firstNameLatin'],
            "lastname": driver_vip_person_data['lastNameLatin'],
            "middlename": driver_vip_person_data['middleNameLatin']
        },
        "licenseNumber": form_data['driver_vip_lic_number'],
        "licenseSeria": form_data['driver_vip_lic_seria'],
        "relative": 0,  # togrlash kk
        "birthDate": form_data['driver_vip_birthDate'],
        "licenseIssueDate": form_data['driver_vip_licenseIssueDate']
    }
    #
    #
    # # # END DRIVERS 1
    #
    #
    #
    # # # END DRIVERS 5
    drivers = []
    drivers.append(driver1)

    # print('drivers' ,drivers)

    applicant['applicant'] = {}
    applicant['applicant']['person'] = person
    applicant['applicant']['organization'] = organization
    applicant['applicant']['address'] = address
    applicant['applicant']['email'] = email
    applicant['owner'] = owner
    applicant['details'] = details
    applicant['cost'] = cost
    applicant['vehicle'] = vehicle
    applicant['drivers'] = drivers

    # print(applicant)
    return applicant

# jismoniy cheklanmagan end


# yuridik cheklangan start

def limit_yuridik(form_data):
    applicant = {}
    print(form_data)
    organizationData = json.loads(form_data['organizationData'])
    print(type(organizationData))
    #

    if 'applicantIsOwner' in form_data:
        if form_data['applicantIsOwner'] == 'on':
            applicantIsOwner = True
    else:
        applicantIsOwner = False

    sumInsured = 40000000

    if form_data['KT'] == '1.4':
        useTerritoryId = '1'
    elif form_data['KT'] == '1':
        useTerritoryId = '2'

    vehicleData = json.loads(form_data['vehicleData'])

    vehicle_issueDate = datetime.fromisoformat(vehicleData['techPassportIssueDate'])
    vehicle_issueDate = datetime.strftime(vehicle_issueDate, '%Y-%m-%d')


    person = None
    organization = {
            "inn":form_data['inn'],
            "name":form_data['organizationName'],
            "phoneNumber": form_data['phone']
        }
    address = form_data['organizationAddress']
    email = form_data['email']
    owner = {
        "person": None,
        "organization":  {
            "inn":form_data['inn'],
            "name":form_data['organizationName'],

        },
        "applicantIsOwner": applicantIsOwner
    }
    details = {
        "issueDate": form_data['startDate'],
        "startDate": form_data['startDate'],
        "endDate": form_data['endDate'],
        "driverNumberRestriction": True,
        "specialNote": "Qayta chiqarish",
        "insuredActivityType": form_data['insuredActivityType']
    }
    cost = {
        "discountId": "1",
        "discountSum": "0",
        "insurancePremium": str(form_data['insurancePremium']),
        "sumInsured": str(sumInsured),
        "contractTermConclusionId": "1",
        "useTerritoryId": str(useTerritoryId),
        "commission": "0",
        "insurancePremiumPaidToInsurer": "0",
        "seasonalInsuranceId": "1"
    }
    vehicle = {
        "techPassport": {
            "number": form_data['techPassportSeria'],
            "seria": form_data['techPassportNumber'],
            "issueDate": vehicle_issueDate
        },
        "modelCustomName": vehicleData['modelName'],
        "engineNumber": vehicleData['engineNumber'],
        "typeId": str(vehicleData['vehicleTypeId']),
        "issueYear": str(vehicleData['issueYear']),
        "govNumber": vehicleData['govNumber'],
        "bodyNumber": vehicleData['bodyNumber'],
        "regionId": form_data['regionId']
    }


    # # START DRIVERS 1
    driver1_person_data = json.loads(form_data['driver1_person_data'])

    driver1_data = json.loads(form_data['driver1_data'])
    licenseIssueDate1 = datetime.fromisoformat(driver1_data['issueDate'])
    licenseIssueDate1 = licenseIssueDate1.strftime('%Y-%m-%d')

    driver1 = {
        "passportData": {
            "pinfl": form_data['driver1_pinfl'],
            "seria": form_data['driver1_passportSeries'],
            "number": form_data['driver1_passportNumber'],
            "issuedBy": driver1_person_data['issuedBy'],
            "issueDate": driver1_person_data['startDate']
        },
        "fullName": {
            "firstname": driver1_person_data['firstNameLatin'],
            "lastname": driver1_person_data['lastNameLatin'],
            "middlename": driver1_person_data['middleNameLatin']
        },
        "licenseNumber": form_data['driver1_lic_number'],
        "licenseSeria": form_data['driver1_lic_seria'],
        "relative": int(form_data['driver1_rlt']),  # togrlash kk
        "birthDate": form_data['driver1_birthDate'],
        "licenseIssueDate": licenseIssueDate1
    }


    # # END DRIVERS 1

    # # START DRIVERS 2

    driver2_person_data = json.loads(form_data['driver2_person_data'])

    driver2_data = json.loads(form_data['driver2_data'])
    licenseIssueDate2 = datetime.fromisoformat(driver2_data['issueDate'])
    licenseIssueDate2 = licenseIssueDate2.strftime('%Y-%m-%d')

    driver2 = {
        "passportData": {
            "pinfl": form_data['driver2_pinfl'],
            "seria": form_data['driver2_passportSeries'],
            "number": form_data['driver2_passportNumber'],
            "issuedBy": driver2_person_data['issuedBy'],
            "issueDate": driver2_person_data['startDate']
        },
        "fullName": {
            "firstname": driver2_person_data['firstNameLatin'],
            "lastname": driver2_person_data['lastNameLatin'],
            "middlename": driver2_person_data['middleNameLatin']
        },
        "licenseNumber": form_data['driver2_lic_number'],
        "licenseSeria": form_data['driver2_lic_seria'],
        "relative": int(form_data['driver2_rlt']),  # togrlash kk
        "birthDate": form_data['driver2_birthDate'],
        "licenseIssueDate": licenseIssueDate2
    }


    # # END DRIVERS 2

    # # START DRIVERS 3
    driver3_person_data = json.loads(form_data['driver3_person_data'])

    driver3_data = json.loads(form_data['driver3_data'])
    licenseIssueDate3 = datetime.fromisoformat(driver3_data['issueDate'])
    licenseIssueDate3 = licenseIssueDate3.strftime('%Y-%m-%d')

    driver3 = {
        "passportData": {
            "pinfl": form_data['driver3_pinfl'],
            "seria": form_data['driver3_passportSeries'],
            "number": form_data['driver3_passportNumber'],
            "issuedBy": driver3_person_data['issuedBy'],
            "issueDate": driver3_person_data['startDate']
        },
        "fullName": {
            "firstname": driver3_person_data['firstNameLatin'],
            "lastname": driver3_person_data['lastNameLatin'],
            "middlename": driver3_person_data['middleNameLatin']
        },
        "licenseNumber": form_data['driver3_lic_number'],
        "licenseSeria": form_data['driver3_lic_seria'],
        "relative": int(form_data['driver3_rlt']),
        "birthDate": form_data['driver3_birthDate'],
        "licenseIssueDate":licenseIssueDate3
    }


    # # END DRIVERS 3


    # # START DRIVERS 4
    driver4_person_data = json.loads(form_data['driver4_person_data'])

    driver4_data = json.loads(form_data['driver4_data'])
    licenseIssueDate4 = datetime.fromisoformat(driver4_data['issueDate'])
    licenseIssueDate4 = licenseIssueDate4.strftime('%Y-%m-%d')

    driver4 = {
        "passportData": {
            "pinfl": form_data['driver4_pinfl'],
            "seria": form_data['driver4_passportSeries'],
            "number": form_data['driver4_passportNumber'],
            "issuedBy": driver4_person_data['issuedBy'],
            "issueDate": driver4_person_data['startDate']
        },
        "fullName": {
            "firstname": driver4_person_data['firstNameLatin'],
            "lastname": driver4_person_data['lastNameLatin'],
            "middlename": driver4_person_data['middleNameLatin']
        },
        "licenseNumber": form_data['driver4_lic_number'],
        "licenseSeria": form_data['driver4_lic_seria'],
        "relative": int(form_data['driver4_rlt']),
        "birthDate": form_data['driver4_birthDate'],
        "licenseIssueDate": licenseIssueDate4
    }


    # # END DRIVERS 4


    # # START DRIVERS 5
    driver5_person_data = json.loads(form_data['driver5_person_data'])

    driver5_data = json.loads(form_data['driver5_data'])
    licenseIssueDate5 = datetime.fromisoformat(driver5_data['issueDate'])
    licenseIssueDate5 = licenseIssueDate5.strftime('%Y-%m-%d')

    driver5 = {
        "passportData": {
            "pinfl": form_data['driver5_pinfl'],
            "seria": form_data['driver5_passportSeries'],
            "number": form_data['driver5_passportNumber'],
            "issuedBy": driver5_person_data['issuedBy'],
            "issueDate": driver5_person_data['startDate']
        },
        "fullName": {
            "firstname": driver5_person_data['firstNameLatin'],
            "lastname": driver5_person_data['lastNameLatin'],
            "middlename": driver5_person_data['middleNameLatin']
        },
        "licenseNumber": form_data['driver5_lic_number'],
        "licenseSeria": form_data['driver5_lic_seria'],
        "relative": int(form_data['driver5_rlt']),  # togrlash kk
        "birthDate": form_data['driver5_birthDate'],
        "licenseIssueDate":licenseIssueDate5
    }

    # # END DRIVERS 5
    drivers = []
    drivers.append(driver1)
    drivers.append(driver2)
    drivers.append(driver3)
    drivers.append(driver4)
    drivers.append(driver5)
    # print('drivers' ,drivers)

    applicant['applicant'] = {}
    applicant['applicant']['person'] = person
    applicant['applicant']['organization'] = organization
    applicant['applicant']['address'] = address
    applicant['applicant']['email'] = email
    applicant['owner'] = owner
    applicant['details'] = details
    applicant['cost'] = cost
    applicant['vehicle'] = vehicle
    applicant['drivers'] = drivers

    # print(applicant)
    return applicant

# yuridik cheklangan end



# yuridik cheklanmagan start

def unlimit_yuridik(form_data):
    applicant = {}
    print(form_data)
    driver_vip_person_data = json.loads(form_data['driver_vip_person_data'])
    print(type(driver_vip_person_data))


    if 'applicantIsOwner' in form_data:
        if form_data['applicantIsOwner'] == 'on':
            applicantIsOwner = True
    else:
        applicantIsOwner = False

    sumInsured = 40000000

    if form_data['KT'] == '1.4':
        useTerritoryId = '1'
    elif form_data['KT'] == '1':
        useTerritoryId = '2'

    vehicleData = json.loads(form_data['vehicleData'])

    vehicle_issueDate = datetime.fromisoformat(vehicleData['techPassportIssueDate'])
    vehicle_issueDate = datetime.strftime(vehicle_issueDate, '%Y-%m-%d')


    person = None
    organization = {
            "inn": "123456789",
            "name": "ООО Фирма",
            "phoneNumber": form_data['phone']
        }
    organizationAddress = form_data['organizationAddress']
    email = form_data['email']
    owner = {
        "person": None,
        "organization":  {
            "inn":form_data['inn'],
            "name":form_data['organizationName'],

        },
        "applicantIsOwner": applicantIsOwner
    }
    details = {
        "issueDate": form_data['startDate'],
        "startDate": form_data['startDate'],
        "endDate": form_data['endDate'],
        "driverNumberRestriction": True,
        "specialNote": "Qayta chiqarish",
        "insuredActivityType": form_data['insuredActivityType']
    }
    cost = {
        "discountId": "1",
        "discountSum": "0",
        "insurancePremium": str(form_data['insurancePremium']),
        "sumInsured": str(sumInsured),
        "contractTermConclusionId": "1",
        "useTerritoryId": str(useTerritoryId),
        "commission": "0",
        "insurancePremiumPaidToInsurer": "0",
        "seasonalInsuranceId": "1"
    }
    vehicle = {
        "techPassport": {
            "number": form_data['techPassportSeria'],
            "seria": form_data['techPassportNumber'],
            "issueDate": vehicle_issueDate
        },
        "modelCustomName": vehicleData['modelName'],
        "engineNumber": vehicleData['engineNumber'],
        "typeId": str(vehicleData['vehicleTypeId']),
        "issueYear": str(vehicleData['issueYear']),
        "govNumber": vehicleData['govNumber'],
        "bodyNumber": vehicleData['bodyNumber'],
        "regionId": str(driver_vip_person_data['regionId'])
    }


    # # START DRIVERS 1
    driver_vip_person_data = json.loads(form_data['driver_vip_person_data'])

    driver_vip_data = json.loads(form_data['driver_vip_data'])
    licenseIssueDate1 = datetime.fromisoformat(driver_vip_data['issueDate'])
    licenseIssueDate1 = licenseIssueDate1.strftime('%Y-%m-%d')

    driver1 = {
        "passportData": {
            "pinfl": form_data['driver_vip_pinfl'],
            "seria": form_data['driver_vip_passportSeries'],
            "number": form_data['driver_vip_passportNumber'],
            "issuedBy": driver_vip_person_data['issuedBy'],
            "issueDate": driver_vip_person_data['startDate']
        },
        "fullName": {
            "firstname": driver_vip_person_data['firstNameLatin'],
            "lastname": driver_vip_person_data['lastNameLatin'],
            "middlename": driver_vip_person_data['middleNameLatin']
        },
        "licenseNumber": form_data['driver_vip_lic_number'],
        "licenseSeria": form_data['driver_vip_lic_seria'],
        "relative": 0,  # togrlash kk
        "birthDate": form_data['driver_vip_birthDate'],
        "licenseIssueDate": form_data['driver_vip_licenseIssueDate']
    }
    #
    #
    # # # END DRIVERS 1
    #
    #
    #
    # # # END DRIVERS 5
    drivers = []
    drivers.append(driver1)

    # print('drivers' ,drivers)

    applicant['applicant'] = {}
    applicant['applicant']['person'] = person
    applicant['applicant']['organization'] = organization
    applicant['applicant']['address'] = organizationAddress
    applicant['applicant']['email'] = email
    applicant['owner'] = owner
    applicant['details'] = details
    applicant['cost'] = cost
    applicant['vehicle'] = vehicle
    applicant['drivers'] = drivers

    # print(applicant)
    return applicant

# yuridik cheklanmagan end


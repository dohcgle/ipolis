import json
# JISMONIY CHEKLANMAGAN START
from contract.models import UnlimitJismoniy, LimitedJismoniy


def unlimit_jismoniy(object):
    object = UnlimitJismoniy.objects.last()

    applicant = {}

    person = {
        "passportData": {
            "pinfl": object.person_pinfl,
            "seria": object.person_serial,
            "number": object.person_number,
            "issuedBy": object.person_issuedBy,
            "issueDate": object.person_issueDate
        },
        "fullName": {
            "firstname": object.person_firstname,
            "lastname": object.person_lastname,
            "middlename": object.person_middlename
        },
        "phoneNumber": object.person_phoneNumber,
        "gender": object.person_gender,
        "birthDate": object.person_birthDate,
        "regionId": object.person_regionId,
        "districtId": object.person_districtId
    }
    organization = None
    address = object.address
    email = object.email
    owner = {
        "person": {
            "passportData": {
                "pinfl": object.owner_pinfl,
                "seria": object.owner_seria,
                "number": object.owner_number,
                "issuedBy": object.owner_issuedBy,
                "issueDate": object.owner_issueDate
            },
            "fullName": {
                "firstname": object.owner_firstname,
                "lastname": object.owner_lastname,
                "middlename": object.owner_middlename,
            }
        },
        "organization": None,
        "applicantIsOwner": object.applicantIsOwner
    }
    details = {
        "issueDate": object.details_issueDate,
        "startDate": object.details_startDate,
        "endDate": object.details_endDate,
        "driverNumberRestriction": False,
        "specialNote": object.details_specialNote,
        "insuredActivityType": object.details_insuredActivityType
    }
    cost = {
        "discountId": object.cost_discountId,
        "discountSum": object.cost_discountSum,
        "insurancePremium": object.cost_insurancePremium,
        "sumInsured": object.cost_sumInsured,
        "contractTermConclusionId": object.cost_contractTermConclusionId,
        "useTerritoryId": object.cost_useTerritoryId,
        "commission": object.cost_commission,
        "insurancePremiumPaidToInsurer": object.cost_insurancePremiumPaidToInsurer,
        "seasonalInsuranceId": object.cost_seasonalInsuranceId
    }
    vehicle = {
        "techPassport": {
            "number": object.vehicle_number,
            "seria": object.vehicle_seria,
            "issueDate": object.vehicle_issueDate
        },
        "modelCustomName": object.vehicle_modelCustomName,
        "engineNumber": object.vehicle_engineNumber,
        "typeId": object.vehicle_typeId,
        "issueYear": object.vehicle_typeId,
        "govNumber": object.vehicle_govNumber,
        "bodyNumber": object.vehicle_bodyNumber,
        "regionId": object.vehicle_regionId
    }

    # # START DRIVERS 1

    # driver1 = {
    #     "passportData": {
    #         "pinfl": object.drivers_pinfl,
    #         "seria": object.drivers_seria,
    #         "number": object.drivers_number,
    #         "issuedBy": object.drivers_issuedBy,
    #         "issueDate": object.drivers_issueDate
    #     },
    #     "fullName": {
    #         "firstname": object.drivers_firstname,
    #         "lastname": object.drivers_lastname,
    #         "middlename": object.drivers_middlename
    #     },
    #     "licenseNumber": object.drivers_licenseNumber,
    #     "licenseSeria": object.drivers_licenseSeria,
    #     "relative": object.drivers_relative,
    #     "birthDate": object.drivers_birthDate,
    #     "licenseIssueDate": object.drivers_licenseIssueDate
    # }
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


# JISMONIY CHEKLANMAGAN END

def limited_jismoniy(object):
    print('utils.py dagi limited jismoniy ishga tushti. applicant yaratish\n\n')
    object = LimitedJismoniy.objects.last()
    applicant = {}

    person = {
        "passportData": {
            "pinfl": object.person_pinfl,
            "seria": object.person_serial,
            "number": object.person_number,
            "issuedBy": object.person_issuedBy,
            "issueDate": object.person_issueDate
        },
        "fullName": {
            "firstname": object.person_firstname,
            "lastname": object.person_lastname,
            "middlename": object.person_middlename
        },
        "phoneNumber": object.person_phoneNumber,
        "gender": object.person_gender,
        "birthDate": object.person_birthDate,
        "regionId": object.person_regionId,
        "districtId": object.person_districtId
    }
    organization = None
    address = object.address
    email = object.email
    owner = {
        "person": {
            "passportData": {
                "pinfl": object.owner_pinfl,
                "seria": object.owner_seria,
                "number": object.owner_number,
                "issuedBy": object.owner_issuedBy,
                "issueDate": object.owner_issueDate
            },
            "fullName": {
                "firstname": object.owner_firstname,
                "lastname": object.owner_lastname,
                "middlename": object.owner_middlename,
            }
        },
        "organization": None,
        "applicantIsOwner": object.applicantIsOwner
    }
    details = {
        "issueDate": object.details_issueDate,
        "startDate": object.details_startDate,
        "endDate": object.details_endDate,
        "driverNumberRestriction": True,
        "specialNote": object.details_specialNote,
        "insuredActivityType": object.details_insuredActivityType
    }
    cost = {
        "discountId": object.cost_discountId,
        "discountSum": object.cost_discountSum,
        "insurancePremium": object.cost_insurancePremium,
        "sumInsured": object.cost_sumInsured,
        "contractTermConclusionId": object.cost_contractTermConclusionId,
        "useTerritoryId": object.cost_useTerritoryId,
        "commission": object.cost_commission,
        "insurancePremiumPaidToInsurer": object.cost_insurancePremiumPaidToInsurer,
        "seasonalInsuranceId": object.cost_seasonalInsuranceId
    }
    vehicle = {
        "techPassport": {
            "number": object.vehicle_number,
            "seria": object.vehicle_seria,
            "issueDate": object.vehicle_issueDate
        },
        "modelCustomName": object.vehicle_modelCustomName,
        "engineNumber": object.vehicle_engineNumber,
        "typeId": object.vehicle_typeId,
        "issueYear": object.vehicle_typeId,
        "govNumber": object.vehicle_govNumber,
        "bodyNumber": object.vehicle_bodyNumber,
        "regionId": object.vehicle_regionId
    }

    # # START DRIVERS 1
    drivers = []
    driver1 = {
        "passportData": {
            "pinfl": object.drivers_pinfl,
            "seria": object.drivers_seria,
            "number": object.drivers_number,
            "issuedBy": object.drivers_issuedBy,
            "issueDate": object.drivers_issueDate
        },
        "fullName": {
            "firstname": object.drivers_firstname,
            "lastname": object.drivers_lastname,
            "middlename": object.drivers_middlename
        },
        "licenseNumber": object.drivers_licenseNumber,
        "licenseSeria": object.drivers_licenseSeria,
        "relative": 0,
        "birthDate": object.drivers_birthDate,
        "licenseIssueDate": object.drivers_licenseIssueDate
    }
    drivers.append(driver1)
    if object.drivers_two_pinfl:
        driver2 = {
            "passportData": {
                "pinfl": object.drivers_two_pinfl,
                "seria": object.drivers_two_seria,
                "number": object.drivers_two_number,
                "issuedBy": object.drivers_two_issuedBy,
                "issueDate": object.drivers_two_issueDate
            },
            "fullName": {
                "firstname": object.drivers_two_firstname,
                "lastname": object.drivers_two_lastname,
                "middlename": object.drivers_two_middlename
            },
            "licenseNumber": object.drivers_two_licenseNumber,
            "licenseSeria": object.drivers_two_licenseSeria,
            "relative": object.drivers_two_relative,
            "birthDate": object.drivers_two_birthDate,
            "licenseIssueDate": object.drivers_two_licenseIssueDate
        }
        drivers.append(driver2)

    elif object.drivers_three_pinfl:
        driver3 = {
            "passportData": {
                "pinfl": object.drivers_three_pinfl,
                "seria": object.drivers_three_seria,
                "number": object.drivers_three_number,
                "issuedBy": object.drivers_three_issuedBy,
                "issueDate": object.drivers_three_issueDate
            },
            "fullName": {
                "firstname": object.drivers_three_firstname,
                "lastname": object.drivers_three_lastname,
                "middlename": object.drivers_three_middlename
            },
            "licenseNumber": object.drivers_three_licenseNumber,
            "licenseSeria": object.drivers_three_licenseSeria,
            "relative": object.drivers_three_relative,
            "birthDate": object.drivers_three_birthDate,
            "licenseIssueDate": object.drivers_three_licenseIssueDate
        }
        drivers.append(driver3)

    elif object.drivers_four_pinfl:
        driver4 = {
            "passportData": {
                "pinfl": object.drivers_four_pinfl,
                "seria": object.drivers_four_seria,
                "number": object.drivers_four_number,
                "issuedBy": object.drivers_four_issuedBy,
                "issueDate": object.drivers_four_issueDate
            },
            "fullName": {
                "firstname": object.drivers_four_firstname,
                "lastname": object.drivers_four_lastname,
                "middlename": object.drivers_four_middlename
            },
            "licenseNumber": object.drivers_four_licenseNumber,
            "licenseSeria": object.drivers_four_licenseSeria,
            "relative": object.drivers_four_relative,
            "birthDate": object.drivers_four_birthDate,
            "licenseIssueDate": object.drivers_four_licenseIssueDate
        }
        drivers.append(driver4)
    elif object.drivers_five_pinfl:
        driver5 = {
            "passportData": {
                "pinfl": object.drivers_five_pinfl,
                "seria": object.drivers_five_seria,
                "number": object.drivers_five_number,
                "issuedBy": object.drivers_five_issuedBy,
                "issueDate": object.drivers_five_issueDate
            },
            "fullName": {
                "firstname": object.drivers_five_firstname,
                "lastname": object.drivers_five_lastname,
                "middlename": object.drivers_five_middlename
            },
            "licenseNumber": object.drivers_five_licenseNumber,
            "licenseSeria": object.drivers_five_licenseSeria,
            "relative": object.drivers_five_relative,
            "birthDate": object.drivers_five_birthDate,
            "licenseIssueDate": object.drivers_five_licenseIssueDate
        }
        drivers.append(driver5)


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
    print('utils.py dagi limited jismoniy yakunlandi. applicant yaratildi\n')
    print(applicant)
    return applicant

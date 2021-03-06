# Generated by Django 4.0.1 on 2022-02-11 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0009_unlimitjismoniy_policy_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='LimitedJismoniy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_pinfl', models.CharField(blank=True, max_length=512, null=True)),
                ('person_serial', models.CharField(blank=True, max_length=512, null=True)),
                ('person_number', models.CharField(blank=True, max_length=512, null=True)),
                ('person_issuedBy', models.CharField(blank=True, max_length=512, null=True)),
                ('person_issueDate', models.CharField(blank=True, max_length=512, null=True)),
                ('person_firstname', models.CharField(blank=True, max_length=512, null=True)),
                ('person_lastname', models.CharField(blank=True, max_length=512, null=True)),
                ('person_middlename', models.CharField(blank=True, max_length=512, null=True)),
                ('person_phoneNumber', models.CharField(blank=True, max_length=512, null=True)),
                ('person_gender', models.CharField(blank=True, max_length=512, null=True)),
                ('person_birthDate', models.CharField(blank=True, max_length=512, null=True)),
                ('person_regionId', models.CharField(blank=True, max_length=512, null=True)),
                ('person_districtId', models.CharField(blank=True, max_length=512, null=True)),
                ('organization', models.CharField(blank=True, max_length=512, null=True)),
                ('address', models.CharField(blank=True, max_length=512, null=True)),
                ('email', models.CharField(blank=True, max_length=512, null=True)),
                ('owner_pinfl', models.CharField(blank=True, max_length=512, null=True)),
                ('owner_seria', models.CharField(blank=True, max_length=512, null=True)),
                ('owner_number', models.CharField(blank=True, max_length=512, null=True)),
                ('owner_issuedBy', models.CharField(blank=True, max_length=512, null=True)),
                ('owner_issueDate', models.CharField(blank=True, max_length=512, null=True)),
                ('owner_firstname', models.CharField(blank=True, max_length=512, null=True)),
                ('owner_lastname', models.CharField(blank=True, max_length=512, null=True)),
                ('owner_middlename', models.CharField(blank=True, max_length=512, null=True)),
                ('owner_organization', models.CharField(blank=True, max_length=512, null=True)),
                ('applicantIsOwner', models.BooleanField(blank=True, default=True, null=True)),
                ('details_issueDate', models.CharField(blank=True, max_length=512, null=True)),
                ('details_startDate', models.CharField(blank=True, max_length=512, null=True)),
                ('details_endDate', models.CharField(blank=True, max_length=512, null=True)),
                ('details_driverNumberRestriction', models.BooleanField(blank=True, null=True)),
                ('details_specialNote', models.CharField(blank=True, max_length=512, null=True)),
                ('details_insuredActivityType', models.CharField(blank=True, max_length=512, null=True)),
                ('cost_discountId', models.CharField(blank=True, max_length=512, null=True)),
                ('cost_discountSum', models.CharField(blank=True, max_length=512, null=True)),
                ('cost_insurancePremium', models.CharField(blank=True, max_length=512, null=True)),
                ('cost_sumInsured', models.CharField(blank=True, max_length=512, null=True)),
                ('cost_contractTermConclusionId', models.CharField(blank=True, max_length=512, null=True)),
                ('cost_useTerritoryId', models.CharField(blank=True, max_length=512, null=True)),
                ('cost_commission', models.CharField(blank=True, max_length=512, null=True)),
                ('cost_insurancePremiumPaidToInsurer', models.CharField(blank=True, max_length=512, null=True)),
                ('cost_seasonalInsuranceId', models.CharField(blank=True, max_length=512, null=True)),
                ('vehicle_number', models.CharField(blank=True, max_length=512, null=True)),
                ('vehicle_seria', models.CharField(blank=True, max_length=512, null=True)),
                ('vehicle_issueDate', models.CharField(blank=True, max_length=512, null=True)),
                ('vehicle_modelCustomName', models.CharField(blank=True, max_length=512, null=True)),
                ('vehicle_engineNumber', models.CharField(blank=True, max_length=512, null=True)),
                ('vehicle_typeId', models.CharField(blank=True, max_length=512, null=True)),
                ('vehicle_issueYear', models.CharField(blank=True, max_length=512, null=True)),
                ('vehicle_govNumber', models.CharField(blank=True, max_length=512, null=True)),
                ('vehicle_bodyNumber', models.CharField(blank=True, max_length=512, null=True)),
                ('vehicle_regionId', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_pinfl', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_seria', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_number', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_issuedBy', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_issueDate', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_firstname', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_lastname', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_middlename', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_licenseNumber', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_licenseSeria', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_relative', models.IntegerField(blank=True, null=True)),
                ('drivers_birthDate', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_licenseIssueDate', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_two_pinfl', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_two_seria', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_two_number', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_two_issuedBy', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_two_issueDate', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_two_firstname', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_two_lastname', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_two_middlename', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_two_licenseNumber', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_two_licenseSeria', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_two_relative', models.IntegerField(blank=True, null=True)),
                ('drivers_two_birthDate', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_two_licenseIssueDate', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_three_pinfl', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_three_seria', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_three_number', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_three_issuedBy', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_three_issueDate', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_three_firstname', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_three_lastname', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_three_middlename', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_three_licenseNumber', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_three_licenseSeria', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_three_relative', models.IntegerField(blank=True, null=True)),
                ('drivers_three_birthDate', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_three_licenseIssueDate', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_four_pinfl', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_four_seria', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_four_number', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_four_issuedBy', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_four_issueDate', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_four_firstname', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_four_lastname', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_four_middlename', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_four_licenseNumber', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_four_licenseSeria', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_four_relative', models.IntegerField(blank=True, null=True)),
                ('drivers_four_birthDate', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_four_licenseIssueDate', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_five_pinfl', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_five_seria', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_five_number', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_five_issuedBy', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_five_issueDate', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_five_firstname', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_five_lastname', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_five_middlename', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_five_licenseNumber', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_five_licenseSeria', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_five_relative', models.IntegerField(blank=True, null=True)),
                ('drivers_five_birthDate', models.CharField(blank=True, max_length=512, null=True)),
                ('drivers_five_licenseIssueDate', models.CharField(blank=True, max_length=512, null=True)),
                ('payment_type', models.CharField(blank=True, max_length=512, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=512, null=True)),
                ('transaction_state', models.CharField(blank=True, max_length=512, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('form_data', models.JSONField(blank=True, null=True)),
                ('applicant', models.JSONField(blank=True, null=True)),
                ('insuranceFormUuid', models.CharField(blank=True, max_length=512, null=True)),
                ('policy_seria', models.CharField(blank=True, max_length=512, null=True)),
                ('policy_number', models.CharField(blank=True, max_length=512, null=True)),
                ('policy_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]

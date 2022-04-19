# Generated by Django 4.0.1 on 2022-02-21 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contract', '0010_limitedjismoniy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='limitedjismoniy',
            old_name='drivers_firstname',
            new_name='drivers_one_lastname',
        ),
        migrations.RenameField(
            model_name='limitedjismoniy',
            old_name='drivers_licenseNumber',
            new_name='drivers_one_licenseNumber',
        ),
        migrations.RenameField(
            model_name='limitedjismoniy',
            old_name='drivers_birthDate',
            new_name='drivers_one_licenseSeria',
        ),
        migrations.RenameField(
            model_name='limitedjismoniy',
            old_name='drivers_issueDate',
            new_name='drivers_one_middlename',
        ),
        migrations.RenameField(
            model_name='limitedjismoniy',
            old_name='drivers_issuedBy',
            new_name='drivers_one_number',
        ),
        migrations.RenameField(
            model_name='limitedjismoniy',
            old_name='drivers_lastname',
            new_name='drivers_one_pinfl',
        ),
        migrations.RenameField(
            model_name='limitedjismoniy',
            old_name='drivers_relative',
            new_name='drivers_one_relative',
        ),
        migrations.RenameField(
            model_name='limitedjismoniy',
            old_name='drivers_licenseIssueDate',
            new_name='drivers_one_seria',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='is_published',
        ),
        migrations.RemoveField(
            model_name='limitedjismoniy',
            name='drivers_licenseSeria',
        ),
        migrations.RemoveField(
            model_name='limitedjismoniy',
            name='drivers_middlename',
        ),
        migrations.RemoveField(
            model_name='limitedjismoniy',
            name='drivers_number',
        ),
        migrations.RemoveField(
            model_name='limitedjismoniy',
            name='drivers_pinfl',
        ),
        migrations.RemoveField(
            model_name='limitedjismoniy',
            name='drivers_seria',
        ),
        migrations.AddField(
            model_name='contract',
            name='address',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='applicantIsOwner',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='cost_commission',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='cost_contractTermConclusionId',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='cost_discountId',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='cost_discountSum',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='cost_insurancePremium',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='cost_insurancePremiumPaidToInsurer',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='cost_seasonalInsuranceId',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='cost_sumInsured',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='cost_useTerritoryId',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='details_driverNumberRestriction',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='details_endDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='details_insuredActivityType',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='details_issueDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='details_specialNote',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='details_startDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_five_birthDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_five_firstname',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_five_issueDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_five_issuedBy',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_five_lastname',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_five_licenseIssueDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_five_licenseNumber',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_five_licenseSeria',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_five_middlename',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_five_number',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_five_pinfl',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_five_relative',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_five_seria',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_four_birthDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_four_firstname',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_four_issueDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_four_issuedBy',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_four_lastname',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_four_licenseIssueDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_four_licenseNumber',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_four_licenseSeria',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_four_middlename',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_four_number',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_four_pinfl',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_four_relative',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_four_seria',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_one_birthDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_one_firstname',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_one_issueDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_one_issuedBy',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_one_lastname',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_one_licenseIssueDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_one_licenseNumber',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_one_licenseSeria',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_one_middlename',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_one_number',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_one_pinfl',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_one_relative',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_one_seria',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_three_birthDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_three_firstname',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_three_issueDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_three_issuedBy',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_three_lastname',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_three_licenseIssueDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_three_licenseNumber',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_three_licenseSeria',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_three_middlename',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_three_number',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_three_pinfl',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_three_relative',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_three_seria',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_two_birthDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_two_firstname',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_two_issueDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_two_issuedBy',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_two_lastname',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_two_licenseIssueDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_two_licenseNumber',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_two_licenseSeria',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_two_middlename',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_two_number',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_two_pinfl',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_two_relative',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='drivers_two_seria',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='email',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='organization',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='owner_firstname',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='owner_issueDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='owner_issuedBy',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='owner_lastname',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='owner_middlename',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='owner_number',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='owner_organization',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='owner_pinfl',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='owner_seria',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='payment_type',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='person_birthDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='person_districtId',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='person_firstname',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='person_gender',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='person_issueDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='person_issuedBy',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='person_lastname',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='person_middlename',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='person_number',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='person_phoneNumber',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='person_pinfl',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='person_regionId',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='person_serial',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='policy_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='transaction_state',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='vehicle_bodyNumber',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='vehicle_engineNumber',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='vehicle_govNumber',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='vehicle_issueDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='vehicle_issueYear',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='vehicle_modelCustomName',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='vehicle_number',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='vehicle_regionId',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='vehicle_seria',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='contract',
            name='vehicle_typeId',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='limitedjismoniy',
            name='drivers_one_birthDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='limitedjismoniy',
            name='drivers_one_firstname',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='limitedjismoniy',
            name='drivers_one_issueDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='limitedjismoniy',
            name='drivers_one_issuedBy',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='limitedjismoniy',
            name='drivers_one_licenseIssueDate',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='contract',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

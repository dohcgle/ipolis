from django.db import models


class ContractJson(models.Model):
    applicant = models.JSONField(blank=True, null=True)
    applicant_fond = models.JSONField(blank=True, null=True)
    csrf = models.CharField(max_length=1024, null=True, blank=True)
    payment_type = models.CharField(max_length=255, null=True, blank=True)
    payme_url = models.URLField(max_length=1024, blank=True, null=True)


    insuranceFormUuid = models.CharField(max_length=512, null=True, blank=True)
    policy_seria = models.CharField(max_length=512, null=True, blank=True)
    policy_number = models.CharField(max_length=512, null=True, blank=True)
    policy_url = models.URLField(null=True, blank=True)
    transaction_order_key = models.CharField(max_length=512, null=True, blank=True)
    transaction_state = models.IntegerField(null=True, blank=True)
    transaction_status = models.CharField(max_length=512, null=True, blank=True)

    error_message = models.CharField(max_length=512, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Полис"
        verbose_name_plural = "Полиса"

    def __str__(self):
        return f"{str(self.id)}"
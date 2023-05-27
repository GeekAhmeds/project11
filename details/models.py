from django.db import models

# Create your models here.


class Drug(models.Model):
    name = models.CharField(("Drug Name"), max_length=50)
    medical_condition = models.CharField(("MedicalCondition"),max_length=50, blank=True)
    side_effects = models.TextField(("Side Effects"), blank=True)
    generic_name = models.CharField(("Generic Name"), max_length=150, blank=True)
    drug_classes = models.CharField(("Drug Classes"), max_length=150, blank=True)
    brand_names = models.TextField(("Brand Names"), max_length=500, blank=True)
    activity = models.CharField(("activity"), max_length=50, blank=True)
    rx_otc = models.CharField(("rx_otc"), max_length=50, blank=True)
    pregnancy_category = models.CharField(("Pregnancy Category"),max_length=50, blank=True)
    csa = models.CharField(("CSA"),max_length=50, blank=True)
    alcohol = models.CharField(("Alcohol"),max_length=50, default='False', blank=True)
    related_drugs = models.TextField(("Related Drugs"), max_length=500, blank=True)
    medical_condition_description = models.TextField(("Medical Condition Description"), blank=True)
    rating = models.CharField(("Rating"), max_length=50, blank=True)
    no_of_reviews = models.CharField(("Number Of Reviews"), max_length=50, blank=True)
    drug_link = models.URLField(("Drug Link"), max_length=500, blank=True)
    medical_condition_url = models.URLField(("Medical Condition URL"), max_length=500, blank=True)




    class Meta:
        verbose_name = ("Drug")
        verbose_name_plural = ("Drugs")

    def __str__(self):
        return self.name


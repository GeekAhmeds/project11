import csv
from io import TextIOWrapper

from django.shortcuts import render
from .models import Drug
from .forms import UploadFileForm


def drug_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = TextIOWrapper(request.FILES['file'].file, encoding='utf-8')
            reader = csv.DictReader(file)
            for row in reader:
                drug = Drug(
                    name=row['drug_name'],
                    medical_condition=row['medical_condition'],
                    side_effects=row['side_effects'],
                    generic_name=row['generic_name'],
                    drug_classes=row['drug_classes'],
                    brand_names=row['brand_names'],
                    activity=row['activity'],
                    rx_otc=row['rx_otc'],
                    pregnancy_category=row['pregnancy_category'],
                    csa=row['csa'],
                    alcohol=row['alcohol'],
                    related_drugs=row['related_drugs'],
                    medical_condition_description=row['medical_condition_description'],
                    rating=row['rating'],
                    no_of_reviews=row['no_of_reviews'],
                    drug_link=row['drug_link'],
                    medical_condition_url=row['medical_condition_url'],
                )
                drug.save()
            return render(request, 'drug_upload.html', {'form': form, 'success': True})
    else:
        form = UploadFileForm()
    return render(request, 'drug_upload.html', {'form': form})

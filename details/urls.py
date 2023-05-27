from django.urls import path
from . import api
from . import views
urlpatterns = [
    path('upload/', views.drug_upload, name='upload'),
    path('drugs/details/', api.search_models),


]
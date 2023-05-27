from django.urls import path
from pages import views

urlpatterns = [
    #path('login/', views.LoginAPIView.as_view(), name='login'),
    #path('log/', views.CustomAuthToken.as_view(), name='loge')
    path('login/', views.user_login, name='loge')
]
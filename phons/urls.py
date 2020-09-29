from django.urls import path

from .views import PhonsList , PhonDetails

urlpatterns = [
    path('', PhonsList.as_view(), name='phons'), 
    path('<int:pk>/', PhonDetails.as_view(), name='phons_details')
]

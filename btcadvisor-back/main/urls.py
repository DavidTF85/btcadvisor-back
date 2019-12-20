from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from homepage import views

urlpatterns = [
    path('', views.main_page, name='main'),
    #path('contactus', views.contactus_page,name='contactus'),
    #path('api/version', views.GetVersion.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

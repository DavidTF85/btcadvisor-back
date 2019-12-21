"""
api/urls.py
"""
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from api import views


urlpatterns = [
    #---------------------------#
    # UNPROTECTED API ENDPOINTS #
    # --------------------------#
#btc_price caculations
    path('stats/tsd', views.GetStatistics.as_view()name= 'btc_stadstics'), 
    path('api/version', views.VersionAPI.as_view(), name='version_api'),


    # GATEWAY
    #path('api/register', views.RegisterAPI.as_view(), name='register_api'),
    path('api/login', obtain_auth_token, name='api_token_auth'),
    #path('api/logout', views.post_logout_api, name='logout_api'),


]
urlpatterns = format_suffix_patterns(urlpatterns)

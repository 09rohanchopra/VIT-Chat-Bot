from django.conf.urls import include, url
from .views import VitBotView
urlpatterns = [
                  url(r'^9ac26cdb25884892cbebd23d8987edd81289056f335f44f9e0/?$', VitBotView.as_view()) 
               ]

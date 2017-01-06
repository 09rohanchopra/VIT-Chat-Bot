from django.conf.urls import include, url
from .views import VitBotView
urlpatterns = [
                  url(r'^0dcc2f2ff78590f0fd035d42c45a6a83dd3d7f2e1b59298501/?$', VitBotView.as_view()) 
               ]

"""SouqScrapper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from SouqScrapperApp import api

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/scrapSouq/$',api.fetchScrapper, name='fetchScrapper'),
    url(r'^api/v1/ounass/$',api.fetch_ounass_scrapper, name='fetch_ounass_scrapper'),
    url(r'^api/v1/nass/$',api.fetch_nass_scrapper, name='fetch_nass_scrapper'),
    url(r'^api/v1/gap/$',api.fetch_gap_scrapper, name='fetch_gap_scrapper'),


    url(r'^api/v1/scrapSouqMissed/(?P<id>.*)/$',api.fetchScrapperMissed, name='fetchScrapperMissed'),

]

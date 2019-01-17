from django.urls import path

from . import views

from .views import homepageData

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('api/data/homepage/',homepageData.as_view(), name='homepageData'),

]

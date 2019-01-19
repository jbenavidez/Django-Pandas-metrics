from django.urls import path

from . import views

from .views import homepageData , dropdownData

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('report-one/', views.report_one, name='report_one'),
    path('api/data/homepage/',homepageData.as_view(), name='homepageData'),
    path('api/data/report_one/',dropdownData.as_view(), name='dropdownData'),

]

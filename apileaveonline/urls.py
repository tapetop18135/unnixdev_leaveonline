from django.urls import path

from . import views

app_name = 'apiLeave'

urlpatterns = [
    path('readsheetgoogle', views.ReadFromSheet.as_view(), name='readsheetgoogle'),
    path('get_policys', views.get_policy, name="policys")
]
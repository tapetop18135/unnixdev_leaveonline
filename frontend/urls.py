from django.urls import path

from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.IndexPage, name='index'),
    # path('checkSend', views.checkSendForm, name='checkSend')

]
from django.urls import path
from  .views import *

urlpatterns=[
    path('predict/', ModelView.as_view(), name='predict'),
]
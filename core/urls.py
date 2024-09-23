from django.urls import path

from .views import TestMsgAPI

urlpatterns = [
    path('test/', TestMsgAPI.as_view(), name='test'),
]
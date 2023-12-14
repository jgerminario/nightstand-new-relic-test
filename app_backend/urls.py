from . import views
from django.urls import path

urlpatterns = [
    path('sync_test/', views.sync_test, name='sync_test'),
    path('test/', views.test_endpoint, name='test_endpoint'),
]
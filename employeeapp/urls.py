from django.contrib import admin
from django.urls import path

from employeeapp.views import index, employees_api

urlpatterns = [
    path( '', index, name="employees"),
    path( 'api/employees/', employees_api, name="employees api" ),
    # path( 'api/employees/<int:employee_id>/', employees_api, name="employee" ),
]

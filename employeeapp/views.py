from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse

from employeeapp.models import Employee

import json


def index( request ):
    '''
    This view returns the home page of the employees app
    '''
    n = Employee.objects.all().count()
    return render( request, 'employeeapp/index.html', { 'n' : n } )

def employees_api( request ):
    '''
    This method is responsible for handling requests for the employees API

    It handles all four types of requests:
    GET - Retrieves all employee details and returns them
    PUT - Allows you edit a single entry of an employee
    DELETE - Allows you to delete an employee
    POST - Allows you to add a new employee
    '''
    if request.method == 'GET':
        return JsonResponse( {
            'employees': [ #list comprehension
                employee.to_dict()
                for employee in Employee.objects.all()
            ]
        } )
    if request.method == 'POST':
        body_unicode = request.body.decode('utf8')
        body = json.loads(body_unicode)

        name = body['name']
        email = body['email']
        date = body['date']
        salary = body['salary']

        newEmployee = Employee.objects.create (
            name = name,
            email = email,
            date_joined = date,
            annual_salary = salary,
        )

        return JsonResponse(newEmployee.to_dict())

    if request.method == "DELETE":
        body_unicode = request.body.decode('utf8')
        body = json.loads(body_unicode)

        employee_id = body['id']

        employee = get_object_or_404(Employee, id=employee_id)
        employee.delete()

        return JsonResponse({
            'id': employee_id
        })

    if request.method == "PUT":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        employee_id = body['id']
        employee = get_object_or_404(Employee, id=employee_id)

        employee.name = body['name'];
        employee.email = body['email'];
        employee.date_joined = body['date'];
        employee.annual_salary = body['salary'];

        employee.save();

        return JsonResponse(
            employee.to_dict()
        )




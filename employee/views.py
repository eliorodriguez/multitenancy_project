from django.shortcuts import render
from employee.models import Employee
from organization.models import Organization
from django.http import JsonResponse,request
from django.views import View
from tenant_schemas.utils import schema_context
import json

# Create your views here.
class EmployeeView(View):

    def get(self, request, *args, **kwargs):
        print(request.META)
        try:
            organizations = Organization.objects.get(domain_url=request.META['REMOTE_ADDR'])
            schema_name = organizations.schema_name

        except Organization.DoesNotExist:
            return JsonResponse({"error":"no organization"})

        with schema_context(schema_name):
            print(schema_name)
            employees = Employee.objects.all()
            data = {"results": list(employees.values("id","name"))}
            return JsonResponse(data)


    def post(self, request, *args, **kwargs):
        try:
            #organizations = Organization.objects.get(domain_url=request.META['HTTP_HOST'])
            organizations = Organization.objects.get(domain_url=request.META['REMOTE_ADDR'])
            schema_name = organizations.schema_name

        except Organization.DoesNotExist:
            return JsonResponse({"error":"no organization"})

        with schema_context(schema_name):
            name = json.loads(request.body)['name']
            employee = Employee(name=name)
            employee.save()
        return  JsonResponse({"message":"Employee added successfully"})
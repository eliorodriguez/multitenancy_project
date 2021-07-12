from django.shortcuts import render
from organization.models import Organization
from django.http import JsonResponse,request
from django.views import View

# Create your views here.
class OrganizationView(View):

      def get(self, request, *args, **kwargs):
            organizations = Organization.objects.all()
            data = {"results": list(organizations.values("domain_url","schema_name","name"))}
            return JsonResponse(data)


      def post(self, request, *args, **kwargs):
            tenant = Organization(domain_url=request.POST.get('domain_url'),
                        schema_name=request.POST.get('schema_name'),
                        name=request.POST.get('name'),
                        )
            tenant.save()

            return "Organization added successfully"


# tenant = Organization(domain_url='127.0.0.1',
#       schema_name='schema1',
#       name='test1',
#       )
# tenant.save()
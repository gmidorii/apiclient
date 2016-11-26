from django.shortcuts import render
from django.http import HttpResponse

from cms.models import Domain

# Create your views here.
def domain_list(request):
	domains = Domain.objects.all().order_by('id')
	return render(request,
					'cms/domain_list.html',
					{'domains': domains})

def domain_edit(request, domain_id=None):
	return HttpResponse('Edit Domain')

def domain_del(request, domain_id):
	return HttpResponse('Delete Domain')


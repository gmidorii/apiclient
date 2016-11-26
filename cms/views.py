from django.shortcuts import render

# Create your views here.
def domain_list(request):
	return HttpResponse('Domain List')

def domain_edit(request, domain_id=None):
	return HttpResponse('Edit Domain')

def domain_del(request, domain_id):
	return HttpResponse('Delete Domain')


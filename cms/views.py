from django.shortcuts import render, get_object_or_404, redirect

from cms.models import Domain, ConvertParam
from cms.forms import DomainForm, ConvertParamForm

import csv

# Create your views here.
def domain_list(request):
	domains = Domain.objects.all().order_by('id')
	params = ConvertParam.objects.all().order_by('id')
	return render(request,
					'cms/domain_list.html',
					{'domains': domains,
					 'params': params})

def domain_edit(request, domain_id=None):
	if domain_id:
		domain = get_object_or_404(Domain, pk=domain_id)
	else:
		domain = Domain()

	if request.method == 'POST':
		form = DomainForm(request.POST, instance=domain)
		if form.is_valid():
			domain = form.save(commit=False)
			domain.save()
			return redirect('cms:domain_list')
	else:
		form = DomainForm(instance=domain)

	return render(request, 'cms/domain_edit.html', dict(form=form, domain_id=domain_id))

def param_edit(request, param_id=None):
	if param_id:
		param = get_object_or_404(ConvertParam, pk=param_id)
	else:
		param = ConvertParam()

	if request.method == 'POST':
		form = ConvertParamForm(request.POST, instance=param)
		if form.is_valid():
			param = form.save(commit=False)
			param.save()
			return redirect('cms:domain_list')
	else:
		form = ConvertParamForm(instance=param)

	return render(request, 'cms/param_edit.html', dict(form=form, param_id=param_id))

def domain_del(request, domain_id):
	domain = get_object_or_404(Domain, pk=domain_id)
	domain.delete()
	return redirect('cms:domain_list')

def param_del(request, param_id):
	param = get_object_or_404(ConvertParam, pk=param_id)
	param.delete()
	return redirect('cms:domain_list')

def domain_add_byfile(request):
	# "domain", "ip"
	csv_file = request.POST['csv_file']
	reader = csv.reader(csv_file.strip().splitlines())
	for row in reader:
		print(row)
		domain = Domain()
		domain.name = row[0]
		domain.ip = row[1]
		domain.save()

	return redirect('cms:domain_list')

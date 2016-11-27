from django.shortcuts import render, get_object_or_404, redirect

from cms.models import Domain
from cms.forms import DomainForm

# Create your views here.
def domain_list(request):
	domains = Domain.objects.all().order_by('id')
	return render(request,
					'cms/domain_list.html',
					{'domains': domains})

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

def domain_del(request, domain_id):
	domain = get_object_or_404(Domain, pk=domain_id)
	domain.delete()
	return redirect('cms:domain_list')

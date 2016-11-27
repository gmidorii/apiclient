from django.forms import ModelForm
from cms.models import Domain


class DomainForm(ModelForm):
    class Meta:
        model = Domain
        fields = ('name', 'ip', )

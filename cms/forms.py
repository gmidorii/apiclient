from django.forms import ModelForm
from cms.models import Domain, ConvertParam


class DomainForm(ModelForm):
    class Meta:
        model = Domain
        fields = ('name', 'ip', )

class ConvertParamForm(ModelForm):
    class Meta:
        model = ConvertParam
        fields = ('key', 'value', )

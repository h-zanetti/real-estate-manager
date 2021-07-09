from webdev.users.models import User
from webdev.imoveis.models import Imovel, Reserva
from django import forms

class ImovelForm(forms.ModelForm):
    anfitriao = forms.ModelChoiceField(
        queryset=User.objects.filter(is_active=True),
        widget=forms.HiddenInput()
    )
    class Meta:
        model = Imovel
        exclude = ('fotos',)

class ReservaForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.filter(is_active=True),
        required=False,
        widget=forms.HiddenInput()
    )
    imovel = forms.ModelChoiceField(
        queryset=Imovel.objects.all(),
        widget=forms.HiddenInput()
    )
    nome_completo = forms.CharField()
    email = forms.EmailField()
    telefone = forms.IntegerField()
    check_in = forms.DateField(input_formats=['%d/%m/%Y', '%d-%m-%Y'])
    check_out = forms.DateField(input_formats=['%d/%m/%Y', '%d-%m-%Y'])
    class Meta:
        model = Reserva
        fields = '__all__'
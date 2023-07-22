from django import forms
from .models import Teklif

class TeklifForm(forms.ModelForm):
    yazar = forms.ChoiceField(choices=Teklif.YAZAR_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    usmodel = forms.ChoiceField(choices=Teklif.USMODEL_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    tonaj = forms.ChoiceField(choices=Teklif.TONAJ_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    uzunluk = forms.ChoiceField(choices=Teklif.UZUNLUK_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    indikator = forms.ChoiceField(choices=Teklif.INDIKATOR_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    cekvade = forms.ChoiceField(choices=Teklif.CEKVADE_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    class Meta:
        model = Teklif
        fields = '__all__'
        widgets = {
            'toemail': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'E-posta adresi'}),
            'firma': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Firma Adi'}),
            'usmodel': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'indikator': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'yazar': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'uzunluk': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'tonaj': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'cekvade': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }
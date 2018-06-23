from django import forms
from django.contrib.auth.models import User
from .models import DataSheet

choicest= (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    (8,8),
)

class DataSheetForm(forms.ModelForm):
    class Meta:
        model = DataSheet
        fields = [
            'integrales',
            'derivadas',
            'matrices',
        ]
        widgets = {
            'integrales' : forms.Select(choices=choicest),
            'derivadas' : forms.Select(choices=choicest),
            'matrices' : forms.Select(choices=choicest),

        }


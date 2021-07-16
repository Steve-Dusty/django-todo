from django import forms
from .models import Code


class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ['room_code']


class JoinRoomForm(forms.Form):
    room_code = forms.CharField(max_length=64)

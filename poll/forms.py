from django import forms
from django.forms import ModelForm, fields
from .models import Poll

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three']

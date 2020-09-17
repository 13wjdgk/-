from django import forms
from .models import Add

class AddPost(forms.ModelForm):
    class Meta:
        model = Add
        fields = ['guest_say']
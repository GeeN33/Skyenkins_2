from django import forms

from appfiles.models import Files
from users.models import User


class FilesForm(forms.ModelForm):

    # author = forms.ModelMultipleChoiceField(queryset=User.objects.all())

    class Meta:
        model = Files
        fields = ['title','file']




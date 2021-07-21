from django import forms
from .models import Feed,Discussion,Discussion2

class FeedForm(forms.ModelForm):
    class Meta:
        model=Feed
        fields=('title','url')

class DiscussionForm(forms.ModelForm):
    class Meta:
        model=Discussion
        fields=('body',)

class DiscussionForm2(forms.ModelForm):
    class Meta:
        model=Discussion2
        fields=('body',)
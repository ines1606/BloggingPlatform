# main/forms.py

from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=2000)

class SearchArticles(forms.Form):
    title = forms.CharField(required=False)
    #TODO: find out how to separate them in a list by ","
    #tags = forms.CharField()
    publish_date = forms.DateField(required=False)
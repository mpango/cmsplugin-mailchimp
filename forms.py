from django import forms
from django.template.loader import render_to_string
import mailchimp

class MailchimpForm(forms.Form):
    email 	= forms.EmailField()
    first_name	= forms.CharField(required=False)
    last_name	= forms.CharField(required=False)

    def subscribe(self, list_id):
        list = mailchimp.utils.get_connection().get_list_by_id(list_id)
        list.subscribe(self.cleaned_data['email'],{'EMAIL':self.cleaned_data['email'], 'FNAME': self.cleaned_data['first_name'], 'LNAME':self.cleaned_data['last_name']})

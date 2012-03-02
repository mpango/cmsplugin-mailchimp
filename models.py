from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import CMSPlugin

class Mailchimp(CMSPlugin):
	list_id 	= models.CharField(_('Mailchimp List ID'), max_length=100)
	email_label 	= models.CharField(_('E-mail address label'), max_length=100)
	first_name_label	= models.CharField(_('First name label'), max_length=100, blank=True, help_text=_('Leave blank to omit the field from the subscription form.'))
	last_name_label 	= models.CharField(_('Last name label'), max_length=100, blank=True, help_text=_('Leave blank to omit the field from the subscription form.'))
	thanks 		= models.CharField(_('Message displayed on successful subscription'), max_length=200)
	submit		= models.CharField(_('Submit button label'), blank=True, max_length=30)

	def __unicode__(self):
		return self.list_id

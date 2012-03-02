from django.utils.translation import ugettext_lazy as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import Mailchimp
from forms import MailchimpForm

class MailchimpPlugin(CMSPluginBase):
    model = Mailchimp
    name = _("Mailchimp Subscription Form")
    render_template = "mailchimp.html"
    
    def render(self, context, instance, placeholder):
	    request = context['request']
        
	    if request.method == "POST":
	    	form = MailchimpForm(request.POST)
	    	if form.is_valid():
	    		form.subscribe(instance.list_id)
	    		context.update( {
	    			'mailchimp': instance,
	    			})
	    		return context
	    	else:
	    		context.update( {
	    			'mailchimp': instance,
	    			'form': form,
	    			})
	    		return context
	    	    
	    else:
	    	form = MailchimpForm()
            context.update({
	    	'mailchimp': instance,
	    	'form': form,
            	})
            return context
    
plugin_pool.register_plugin(MailchimpPlugin)

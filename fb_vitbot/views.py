from django.views import generic
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import requests
# Create your views here.

class VitBotView(generic.View):
	def get(self, request, *args, **kwargs):
		if self.request.GET['hub.verify_token'] == '3482957692':
			return HttpResponse(self.request.GET['hub.challenge'])
		else:
			return HttpResponse('Error, invalid token')
	
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return generic.View.dispatch(self, request, *args, **kwargs)

	# Post function to handle Facebook messages
	def post(self, request, *args, **kwargs):
		# Converts the text payload into a python dictionary
		incoming_message = json.loads(self.request.body.decode('utf-8'))
		
		for entry in incoming_message['entry']:
			for message in entry['messaging']:
				# Check if the received call is a message call
				if 'message' in message:
					# Print the message to terminal
					print(message)  
					# Check if the message has text, attachments don't generally have text
					if 'text' in message['message']:   
						post_facebook_message(message['sender']['id'], message['message']['text'])     
		return HttpResponse()


def post_facebook_message(fbid, recevied_message):           
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=<Get Token!>' 


    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":recevied_message}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    print(status.json())

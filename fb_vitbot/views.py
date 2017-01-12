from django.views import generic
from django.http.response import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import logging

from fb_vitbot.response import get_response
#from response import get_response

logger = logging.getLogger(__name__)

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
        #logger.debug(incoming_message)
	
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                # Check if the received call is a message call
                if 'message' in message:
                    # Print the message to terminal
                    is_typing(self, message['sender']['id'],1)
                    if 'is_echo' in message['message']:
                        if message['message']['is_echo']:
                            pass
                        else:
                            logger.debug(message)  
                            if 'text' in message['message']:   
                            	get_response(message['message']['text'],message['sender']['id'])
                    else:
                        logger.debug(message)  
                        # Check if the message has text, attachments don't generally have text
                        if 'text' in message['message']:   
                        	get_response(message['message']['text'],message['sender']['id'])
        is_typing(self, message['sender']['id'],0)
        return HttpResponse()


def is_typing(self, fbid, typing):
        if typing == 1:
            typing_indicator = "typing_on"
        else:
            typing_indicator = "typing_off"
        post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAADljwd55ogBAJSRkD4JJZBklUPD7AKNb7g5FcTbZASrjJDBifAfz6y3OLJcAGQrYEcHhWAgfqduegl7rlL770u3xU21QTvzpVWtDsWajFguush2bDimEdorL4iT3ZC0kDz6G8khBzXbesxsgO7Spqrwm3aLbS26oCXATOPGAZDZD'


        response_msg = json.dumps({"recipient":{"id":fbid}, "sender_action":typing_indicator})
        status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)



def post_facebook_message(fbid, received_message):           
    
    #response = get_response(received_message,fbid)

    #send_message = response['text'].decode('utf-8')

    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAADljwd55ogBAJSRkD4JJZBklUPD7AKNb7g5FcTbZASrjJDBifAfz6y3OLJcAGQrYEcHhWAgfqduegl7rlL770u3xU21QTvzpVWtDsWajFguush2bDimEdorL4iT3ZC0kDz6G8khBzXbesxsgO7Spqrwm3aLbS26oCXATOPGAZDZD' 
    

    user_details_url = "https://graph.facebook.com/v2.6/%s"%fbid
    user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':'EAADljwd55ogBAJSRkD4JJZBklUPD7AKNb7g5FcTbZASrjJDBifAfz6y3OLJcAGQrYEcHhWAgfqduegl7rlL770u3xU21QTvzpVWtDsWajFguush2bDimEdorL4iT3ZC0kDz6G8khBzXbesxsgO7Spqrwm3aLbS26oCXATOPGAZDZD'}
    user_details = requests.get(user_details_url, user_details_params).json()


    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":received_message}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    logger.debug(status.json())


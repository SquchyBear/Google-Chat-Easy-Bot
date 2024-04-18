import json
from httplib2 import Http
from pprint import pprint

class webhook():
    def __init__(self, url:str):
        '''
        The webhook url should be in this form:
        https://chat.googleapis.com/v1/spaces/~/messages?key=~&token=~
        replace each ~ with the respective text of the url.
        '''
        self.url = url

    def send(self, message:str, printResponse:bool=False):
        app_message = {"text": message}
        message_headers = {"Content-Type": "application/json; charset=UTF-8"}
        http_obj = Http()
        response = http_obj.request(
            uri=self.url,
            method="POST",
            headers=message_headers,
            body=dumps(app_message),
        )
        if printResponse:
            pprint(response)

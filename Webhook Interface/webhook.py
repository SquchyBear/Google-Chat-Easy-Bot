import json
from httplib2 import Http
from pprint import pprint
from google.colab import userdata

class webhook():
    def __init__(self, url:str):
        '''
        The webhook url should be in this form:
        https://chat.googleapis.com/v1/spaces/~/messages?key=~&token=~
        replace each ~ with the respective text of the url.
        '''
        self.url = url

    def send(self, message:str, printResponse:bool=False):
        response = Http().request(
            uri=self.url,
            method="POST",
            headers={"Content-Type": "application/json; charset=UTF-8"},
            body=json.dumps({"text": message}),
        )
        if printResponse:
            pprint(response)

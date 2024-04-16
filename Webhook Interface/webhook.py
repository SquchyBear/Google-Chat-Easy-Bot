import json
import http2lib

class webhook():
    def __init__(self, url:str):
        self.url = url

    def send(self, message:str):
        # Code to send message
    

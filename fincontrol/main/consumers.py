from channels.generic.websocket import WebsocketConsumer
from .models import *
import json
from datetime import datetime

def default_converter(o):
    if isinstance(o, datetime):
        return o.isoformat()

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        transactions = transaction.objects.all()
        toJSON = list(transactions.values())
        toJSON = json.dumps(toJSON, default=default_converter)
        self.send(toJSON)

    


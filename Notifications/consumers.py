from channels.generic.websocket import WebsocketConsumer

class WSConsumer(WebsocketConsumer):
    def connect(self):
        # self.accept()
        self.send({
            "type": "telegram.message",
            "text": "You said:text"
        })

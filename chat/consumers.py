from django.shortcuts import render
import json
from datetime import datetime
from channels.generic.websocket import WebsocketConsumer
from .models import UsersTbl, Message

class ChatConsumer(WebsocketConsumer):     
    def connect(self):
        """
        Accepts the WebSocket connection and sends an acceptance event to the client page.
        """
        # Accept the connection
        self.accept()
        
        # sending event to the client page 
        self.send('{"type":"accept", "status":"accepted"}')
        
        # user = self.scope.get("user")
        # user_session = self.scope.get("session")
        # chat_person = self.scope.get("url_route")
        self.chat_person_id = self.scope.get("url_route").get("kwargs").get("id")

        # channel layer - debug purpose 
        # print('user : ',  user)
        # print('chat_person : ',chat_person)
        # print('user_session : ', user_session)
        # print('channel layer : ',  self.channel_layer)
        # print('name : ', self.channel_name)
        # print('channels in layer : ', self.channel_layer.channels)
        
        
    def receive(self, text_data):
        """
        Receives a message from the client and prints it.
        Sends an event to the client page indicating that a new message has arrived.
        """
        # Receive msg coming from the client - debug purpose
        # print(str(text_data))
        # print(received_data.get("type"))
        # print(received_data.get("message"))

        received_data = json.loads(text_data)
        
        # save the msg to the db 
        save_msg = Message()
        save_msg.from_user = self.scope.get("user")
        save_msg.to_user = UsersTbl.objects.get(id=self.chat_person_id)
        save_msg.message = received_data.get("message")
        save_msg.message_seen_status = False
        save_msg.save()

        # sending event to the client page 
        self.send('{"type":"event_arrive", "status":"arrived"}')
        
    def disconnect(self, code):
        """
        Handles WebSocket disconnection.
        Prints a message indicating disconnection.
        """
        # For disconnecting the websocket
        print("Connection stopped or disconnected !!")

from django.shortcuts import render
import json

from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):     
    def connect(self):
        """
        Accepts the WebSocket connection and sends an acceptance event to the client page.
        """
        # Accept the connection
        self.accept()
        
        # sending event to the client page 
        self.send('{"type":"accept", "status":"accepted"}')
        
        user = self.scope.get("user")
        user_session = self.scope.get("session")
        
        print('user : ',  user)
        print('user_session : ', user_session)
        
        # channel layer - debug purpose 
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

        received_data = json.loads(text_data)
        print(received_data.get("type"))
        print(received_data.get("message"))
        
        # sending event to the client page 
        self.send('{"type":"event_arrive", "status":"arrived"}')
        
    def disconnect(self, code):
        """
        Handles WebSocket disconnection.
        Prints a message indicating disconnection.
        """
        # For disconnecting the websocket
        print("Connection stopped or disconnected !!")

from channels.generic.websocket import AsyncWebsocketConsumer
import json


class EchoConsumer(AsyncWebsocketConsumer):

    async def websocket_connect(self, event):
        print("connected", event)
        self.return_channel = 'user_channel'

        await self.channel_layer.group_add(
            self.return_channel,
            self.channel_name
        )
        await self.accept()

    async def websocket_receive(self, event):
        print("received notifier", event)

        data = int(event['text'])
        await self.channel_layer.send(
            "file-upload",
            {
                "type": "stupid.message",
                "num_lines": data,
                "return_channel": self.return_channel
            },
        )

    async def websocket_disconnect(self, event):
        print("close", event)

    async def upload_notification(self, event):
        message = event['data']

        await self.send(text_data=json.dumps({
            'message': message
        }))

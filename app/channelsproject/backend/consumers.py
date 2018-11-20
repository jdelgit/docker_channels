from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync


class UploadConsumer(AsyncWebsocketConsumer):

    async def websocket_connect(self, event):
        print("connected", event)
        await self.accept()

    async def websocket_receive(self, event):
        print("received backend", event)

    async def websocket_disconnect(self, event):
        print("close", event)

    async def stupid_message(self, event):
        try:
            num_lines = event["num_lines"]
        except KeyError:
            num_lines = 1

        stupid_str = f"I will write {num_lines} lines and I will write {num_lines} more.\
        \n Just to be the code that writes {num_lines} lines to test asyncio"
        for i in range(num_lines):
            print(stupid_str)

        ch = event['return_channel']
        msg = f'done writing {i} lines'
        # notify frontend
        async_to_sync(
            await self.channel_layer.group_send(
                    ch,
                    {
                        'type': 'upload.notification',
                        'data': msg
                    },
                )
        )

        # delete channel once message sent
        async_to_sync(
            await self.channel_layer.group_send(
                    ch,
                    {
                        'type': 'websocket.close',
                    },
                )
        )
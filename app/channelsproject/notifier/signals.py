import channels.layers
from asgiref.sync import async_to_sync
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DummyModel


@receiver(post_save, sender=DummyModel)
def trigger_consumer(sender, instance, **kwargs):
    message = 100
    print("sending signals")
    channel_layer = channels.layers.get_channel_layer()
    async_to_sync(channel_layer.send)(
        'file-upload',
        {
            'type': 'stupid.message',
            "num_lines": message,
            'return_channel': "my_return_channel"
        }
    )
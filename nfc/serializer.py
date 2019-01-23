from rest_framework import serializers
from .models import CardRead
from message.serializer import MessageSerializer
from pilibs import nfc_reader


class CardReadSerializer(serializers.Serializer):
    idm = serializers.CharField(max_length=255, read_only=True)
    message = MessageSerializer()

    def create(self, validated_data):
        message_data = validated_data.pop('message')
        message = MessageSerializer.create(MessageSerializer(), validated_data=message_data)
        nfc = CardRead(message=message, **validated_data)
        nfc.idm = nfc_reader.read()
        return nfc

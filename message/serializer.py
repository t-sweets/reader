from rest_framework import serializers
from .models import Message
from pilibs.sc1602 import SC1602


class MessageSerializer(serializers.Serializer):
    lcd = SC1602()
    line_1 = serializers.CharField(max_length=16, allow_blank=True)
    line_2 = serializers.CharField(max_length=16, allow_blank=True)

    def create(self, validated_data):
        message = Message(**validated_data)
        self.lcd.string(message.line_1, 1)
        self.lcd.string(message.line_2, 2)
        return message

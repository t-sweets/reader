from rest_framework.generics import CreateAPIView
from .serializer import MessageSerializer


class MessageView(CreateAPIView):
    serializer_class = MessageSerializer

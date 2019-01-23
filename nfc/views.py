from rest_framework.generics import CreateAPIView
from .serializer import CardReadSerializer


class CardReadView(CreateAPIView):
    serializer_class = CardReadSerializer

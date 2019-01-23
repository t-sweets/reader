from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from nfc.views import CardReadView
from message.views import MessageView


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include([
        url(r'^v1/', include([
            url(r'card_read/$', CardReadView.as_view(), name='card_read'),
            url(r'message/$', MessageView.as_view(), name='message'),
        ]))
    ])),
]

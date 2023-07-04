from django.contrib import admin

from .models import Conversation, ConservationMessage

admin.site.register(Conversation)
admin.site.register(ConservationMessage)

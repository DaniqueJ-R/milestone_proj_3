from django.contrib import admin
from .models import Notes, Sticker, StickerTypeModel, Background

# Register your models here.

admin.site.register(Notes)
admin.site.register(Sticker)
admin.site.register(StickerTypeModel)
admin.site.register(Background)


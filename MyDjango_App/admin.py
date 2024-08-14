from django.contrib import admin
from .models import Topic, WebPage, AccessRecord, UserProfileInfo
# # Register your models here.
# admin.site.register(Event)
# admin.site.register(Booking)

admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(AccessRecord)
admin.site.register(UserProfileInfo)


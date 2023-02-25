from django.contrib import admin
from .models import Guestbook


class GuestbookAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'desc', 'created_at', 'updated_at', 'status')
    list_filter = ('status',)
    search_fields = ('name',)


admin.site.register(Guestbook, GuestbookAdmin)

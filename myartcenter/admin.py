from django.contrib import admin
from myartcenter.models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
#admin.site.register(User)

class AccountAdmin(UserAdmin):
    list_display = ("email", "username", "date_joined", 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, AccountAdmin)
admin.site.register(Art)
admin.site.register(Album)

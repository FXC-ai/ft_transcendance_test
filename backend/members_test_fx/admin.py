from django.contrib import admin

from members_test_fx.models import Members
from members_test_fx.models import Games

class MembersAdmin(admin.ModelAdmin):
    list_display = ('name','surname', 'age', 'active', 'connection_state')

class GamesAdmin(admin.ModelAdmin):
    list_display = ('title','members')

admin.site.register(Members, MembersAdmin)
admin.site.register(Games)
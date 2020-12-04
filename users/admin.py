#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#Models
from django.contrib.auth.models import User
from users.models import UsersRole

# Register your models here.
@admin.register(UsersRole)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""
    list_display = ('pk', 'user_id','get_username','role')
    list_filter  = ('created', 'user__is_active')
    
    def get_username(self, obj):
        return obj.user.username

    readonly_fields = ('created','modified',)



class ProfileInLine(admin.StackedInline):
    """Profile in line admin for users"""
    model = UsersRole
    can_delete = False
    verbose_name_plural = 'usersroles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin"""
    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

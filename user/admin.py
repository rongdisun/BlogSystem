from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user.models import User, UserProfile

# Register your models here.

admin.site.unregister(Group)


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('userid', 'username', 'password')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'password')


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = User
    list_display = ['userid', 'username', 'is_staff']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('userid', 'username', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    fieldsets = (
        (None, {'fields': ('password',)}),
        ('个人信息', {'fields': ('username', 'is_active', 'is_staff', 'is_superuser')}),
        # ('Permissions', {'fields': ('groups', 'user_permissions')}),
    )

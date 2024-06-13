from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("username", "email", "profile_photo", "is_staff", "is_active",)
    list_filter = ("username", "email", "profile_photo", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "email", "password", "profile_photo")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "email", "password1", "password2", "profile_photo", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)



class CustomChirp(admin.ModelAdmin):
    model = Chirp 
    list_display = ("chirp","author","created")

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Chirp, CustomChirp)
admin.site.register(Like)
admin.site.register(Reply)
admin.site.register(Follow)
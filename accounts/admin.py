from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, User
from .forms import CustomUserCreationForm, CustomUserChangeForm


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_plural_name = "User Profile"
    fk_name = "user"


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display_links = ["username"]
    search_fields = ("username",)
    ordering = ("username",)
    # inlines = (UserProfileInline,)
    list_display = (
        "username",
        "is_superuser",
    )
    list_filter = ("username", "is_superuser", "user_type")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            ("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone_number",
                    "user_type",
                )
            },
        ),
        (
            ("Permissions"),
            {
                "fields": ("is_superuser", "groups", "user_permissions"),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "user_type"),
            },
        ),
    )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(User, CustomUserAdmin)

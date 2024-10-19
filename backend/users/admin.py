from datetime import date

from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "age",
        "is_premium",
    )
    ordering = ("-id",)
    search_fields = ("username", "first_name", "last_name", "email")

    @admin.display(description="age")
    def age(self, user):
        birth_date = user.birth_date
        today_date = date.today()
        age = today_date - birth_date
        return age.days // 365

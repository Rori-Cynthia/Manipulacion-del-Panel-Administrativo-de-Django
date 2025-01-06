from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import AccountUser, Book


class CustomUserAdmin(UserAdmin):
    model = AccountUser
    fieldsets = UserAdmin.fieldsets


admin.site.register(AccountUser, CustomUserAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'valuation')
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('valuation', 'updated_at') 
from django.contrib import admin
from .models import Register

# Register your models here.


class RegisterAdmin(admin.ModelAdmin):
    model = Register
    list_display = ['name', 'school', 'location', 'titles']


admin.site.register(Register, RegisterAdmin)

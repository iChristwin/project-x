from django.contrib import admin
from .models import Register, Tutor, Subscribe


# Register your models here.


class RegisterAdmin(admin.ModelAdmin):
    model = Register
    list_display = ['f1name', 'email', 'phone', 'why', ]


class TutorAdmin(admin.ModelAdmin):
    model = Tutor
    list_display = ['f1name', 'email', 'phone',  'you', ]

class SubscribeAdmin(admin.ModelAdmin):
    model = Subscribe
    list_display = ['Email']


admin.site.register(Register, RegisterAdmin)

admin.site.register(Tutor, TutorAdmin)

admin.site.register(Subscribe, SubscribeAdmin)


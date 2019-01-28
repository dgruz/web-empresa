from django.contrib import admin
from .models import Service  #, MyUser

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')


admin.site.register(Service,ServiceAdmin)

#admin.site.register(MyUser)


from pyclbr import Class
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, InstructorProfile

 
@admin.register(User) # el decorador recibe la clase de abajo para personalizarla
class userAdmin(BaseUserAdmin): #personaliza como se ve en el admin
    #los fieldsets definen como se agrupan los campos en la pantalla
    # (título, {opciones})
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Rol personalizado", {"fields": ("is_instructor",)}),
    )
    #pantalla para crear un usuario nuevo
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {"fields": ("is_instructor",)}),
    )

admin.site.register(InstructorProfile)

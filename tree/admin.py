from django.contrib import admin
from .models import T_user,T_card

@admin.register(T_user)
class T_userAdmin(admin.ModelAdmin):
    list_display = ['name', 'name_second', 'slug', 'phone', 'address']
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(T_card)
class T_cardAdmin(admin.ModelAdmin):
    list_display = ['account', 'card']

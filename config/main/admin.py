from django.contrib import admin
from .models import Cars, Colors, Brands,Comment


class CarsAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'color', 'name']

admin.site.register(Cars, CarsAdmin)  # To'g'ri usul

admin.site.register(Colors)
admin.site.register(Brands)
admin.site.register(Comment)







# from django.contrib import admin
# from .models import Cars, Comment
#
# # Ushbu qatorni o‘chirib tashlang, agar mavjud bo‘lsa:
# @admin.register(Cars)
#
# class CarsAdmin(admin.ModelAdmin):
#     list_display = ('name', 'brand', 'color')

# Avtomobillar faqat bir marta ro‘yxatdan o‘tishi kerak:
# admin.site.register(Cars, CarsAdmin)
# admin.site.register(Comment)

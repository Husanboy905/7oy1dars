from django.contrib import admin
from .models import Cars, Comment, Brands, Colors, Categories

@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'color')
    search_fields = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('car', 'user', 'created_at')

admin.site.register(Brands)
admin.site.register(Colors)
admin.site.register(Categories)




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

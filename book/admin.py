from django.contrib import admin

from book.models import Book, Category, Group,Product


# Register your models here.
# admin.site.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'price')
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title', 'description')
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
      list_display = ('name', 'description')
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
      list_display = ('name',)

from django.contrib import admin

from olcha.models import Category, Group, Product


# Register your models here.
# admin.site.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'price')
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    list_filter = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}

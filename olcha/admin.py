from django.contrib import admin

from olcha.models import Category, Group, Product, Image, Comment, AttributeKey,AttributeValue,ProductAttribute


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

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('product',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
      list_display = ('user', )
      list_filter = ('user',)


admin.site.register(AttributeKey)
admin.site.register(AttributeValue)
admin.site.register(ProductAttribute)

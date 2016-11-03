from django.contrib import admin

from models import Article
from models import Master
from models import Topic
from models import Comments
from models import Product, Category, Order
# # class ArticleAdmin(admin.ModelAdmin):
# #     fields = ['header_text', 'text', 'author', 'pubDate']
#
admin.site.register(Article)
admin.site.register(Master)
admin.site.register(Topic)
admin.site.register(Comments)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)

# admin.site.register(MyUser)

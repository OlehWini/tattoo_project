from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/', views.blog_page, name='blog_page'),
    url(r'^shop/', views.shop_page, name='shop_page'),
    url(r'^masters/', views.masters_page, name='masters_page'),
    url(r'^home/', views.index, name='index'),
    url(r'^search_master/', views.search_master, name='searching'),
    url(r'^topic_(\d+)/', views.topic_blog_page, name='topic_block_page'),
    url(r'tattoo_kits/', views.product_page_category  , name='product_page'),
    url(r'rotary_mashine/', views.product_page_category, name='products_page_rotory_mashine'),
    url(r'inductive_mashine/', views.product_page_category, name='products_page_inductive_mashine'),
    url(r'tattoo_inks/', views.product_page_category, name='products_page_tattoo_inks'),
    url(r'transfer_tools/', views.product_page_category, name='products_page_tattoo_inks'),
    url(r'grips_tips_and_tubes/', views.product_page_category, name='products_page_tattoo_inks'),
    url(r'sterile_needles/', views.product_page_category, name='products_page_tattoo_inks'),
    url(r'tattoo_skin/', views.product_page_category, name='products_page_tattoo_inks'),
    url(r'tattoo_ink_accessories/', views.product_page_category, name='products_page_tattoo_inks'),
    url(r'tattoo_mashine_accessories/', views.product_page_category, name='products_page_tattoo_inks'),
    url(r'^product_(\d+)/', views.product_page, name='show_product_page'),
    url(r'^vk_first_page/', views.vk_first_page, name='vk_first_page'),
    url(r'^vk_second_page/', views.vk_second_page, name='vk_second_page'),
    url(r'^vk_third_page/', views.vk_third_page, name='vk_third_page'),
    url(r'^buy/(\d+)', views.ordering, name='buy'),


]
# https://www.youtube.com/watch?v=QgdINlxm-wE&list=PLpTASIMYgCp8supkEmnnrYa5xi9g91ZPI
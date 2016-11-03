from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from .models import Article
from .models import Master
from  django.template import Context
from .models import Topic, Comments, Category, Product, Order
from forms import CommentForm
from django.core.context_processors import csrf
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
import vk

def index(request):
    articles = Article.objects.all()
    return render(request, 'main/index.html', {'articles': articles,'username': auth.get_user(request).username})



def topic_blog_page(request, topic_id=1):
    topic = Topic.objects.get(id=topic_id)
    comments = Comments.objects.filter(topic_id=topic_id)
    count_of_comments = topic.comments_set.count()
    if request.method == 'POST':
        Comments.objects.create(
            comments_text_of_comment=request.POST.get('fCommentText'),
            topic=topic,
            user=request.user

        )
    topic.topic_count_of_records = count_of_comments
    context = {
        'topic': topic,
        'comments': comments,
        'username': auth.get_user(request).username,
    }
    return  render(request, 'main/topic_in_blog.html', context)

def blog_page(request):
    topics = Topic.objects.all()
    for topic in topics:
        topic.topic_count_of_records = topic.comments_set.count()
    return render(request, 'main/blog.html', {'topics':topics,'username': auth.get_user(request).username})

# def add_record(request, topic_id=1):
#     topic22=Topic.objects.get(id=topic_id)
#     if request.method =='POST':
#         Comments.objects.create(
#             comments_text_of_comment=request.POST.get('fCommentText'),
#             topic = topic22,
#             username=auth.get_user(request).username
#         )
#
#     context = {
#         'username':username
#     }
#     return render(request, 'main/topic_in_blog.html', context)
#

# def show_record(request):
#     return render(request, 'main/topic_in_blog.html', {})


def masters_page(request):
    masters = Master.objects.all()
    return render(request, 'main/masters.html', {'masters':masters, 'username': auth.get_user(request).username})


def search_master(request):
    search_masters =[]
    masters = Master.objects.all()
    if request.method == 'POST':
        search_character = request.POST.get('f_for_search')
        for master in masters:
            if search_character.upper() == master.city.upper():
                search_masters.append(master)

            elif search_character.upper() == master.name.upper():
                search_masters.append(master)
            elif search_character.upper() == master.sur_name.upper():
                search_masters.append(master)
    return render(request, 'main/searchMastersResult.html', {'search_masters':search_masters, 'username': auth.get_user(request).username})


def shop_page(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'username': auth.get_user(request).username
    }
    return render(request, 'main/shop.html', context)

def product_page_category(request):
    my_category = ''
    products = Product.objects.all()
    categories = Category.objects.all()

    if request.get_full_path() == "/rotary_mashine/":
        my_category = Category.objects.get(name='Rotary tattoo machine').name

    elif request.get_full_path() == "/tattoo_kits/":
        my_category = Category.objects.get(name='Tattoo kits').name

    elif request.get_full_path() == "/inductive_mashine/":
        my_category = Category.objects.get(name='Inductive tattoo machine').name

    elif request.get_full_path() == "/tattoo_inks/":
        my_category = Category.objects.get(name='Tattoo inks').name

    elif request.get_full_path() == "/transfer_tools/":
        my_category = Category.objects.get(name='Transfer Tools').name

    elif request.get_full_path() == "/grips_tips_and_tubes/":
         my_category = Category.objects.get(name='Grips Tips & Tubes ').name

    elif request.get_full_path() == "/sterile_needles/":
         my_category = Category.objects.get(name='Sterile Tattoo Needles').name

    elif request.get_full_path() == "/tattoo_skin/":
         my_category = Category.objects.get(name='Tattoo Skin').name

    elif request.get_full_path() == "/tattoo_ink_accessories/":
        my_category = Category.objects.get(name='Tattoo Ink Accessories').name

    elif request.get_full_path() == "/tattoo_mashine_accessories/":
        my_category = Category.objects.get(name='Tattoo Machine Accessories ').name

    context = {
        'categories': categories,
        'products': products,
        'username': auth.get_user(request).username,
        'my_category': my_category,
        'www':request.get_full_path()
    }
    return render(request, 'main/product_category_page.html', context)


def product_page(request, product_id):
    product=Product.objects.get(id=product_id)
    products = Product.objects.all()

    context = {
        'product': product,
        'products': products,
        'user': auth.get_user(request),
    }
    return render(request, 'main/product_page.html', context)


def ordering(request, product_id):
    product=Product.objects.get(id=product_id)
    if request.method=='POST':
        Order.objects.create(
            mobil_number=request.POST.get('mob_number'),
            user=request.user,
            product=product
        )

    return render(request, 'main/order_result.html', {'product':product})

def vk_first_page(request):
    session = vk.Session()
    api = vk.API(session)

    group_info = api.groups.getById(group_id=26776509, version=5.59)
    group_users_info = api.groups.getMembers(group_id=26776509, version=5.59)

    users_count=group_users_info['count']
    group_name = group_info[0]['name']
    group_description = group_info[0]['screen_name']
    group_avatar_small = group_info[0]['photo']
    group_avatar = group_info[0]['photo_big']

    wall = api.wall.get(owner_id=-26776509, count=50, extended=1, version=5.59)
    src_img_arr = []
    likes_arr = []
    i = 1
    while i < 50:
        if wall['wall'][i]['attachments'][0]['type'] == 'photo':
            src_img_arr.append(wall['wall'][i]['attachments'][0]['photo']['src_big'])
            likes_arr.append(wall['wall'][i]['likes']['count'])
            i += 1
        else:
            i += 1
            continue



    context = {
        'likes_arr':likes_arr,
        'src_img_arr': src_img_arr,
        'group_name': group_name,
        'group_avatar': group_avatar,
        'users_count':users_count,
        'group_description': group_description,
        'group_avatar_small':group_avatar_small

    }
    return render(request, 'main/vk_page.html', context)

def vk_second_page(request):
    session = vk.Session()
    api = vk.API(session)

    group_info = api.groups.getById(group_id=25559245, version=5.59)
    group_users_info = api.groups.getMembers(group_id=25559245, version=5.59)

    users_count=group_users_info['count']
    group_name = group_info[0]['name']
    group_description = group_info[0]['screen_name']
    group_avatar_small = group_info[0]['photo']
    group_avatar = group_info[0]['photo_big']

    wall = api.wall.get(owner_id=-25559245, count=50, extended=1, version=5.59)
    src_img_arr = []
    likes_arr = []
    i = 1
    while i < 50:
        if wall['wall'][i]['attachments'][0]['type'] == 'photo':
            src_img_arr.append(wall['wall'][i]['attachments'][0]['photo']['src_big'])
            likes_arr.append(wall['wall'][i]['likes']['count'])
            i += 1
        else:
            i += 1
            continue



    context = {
        'likes_arr':likes_arr,
        'src_img_arr': src_img_arr,
        'group_name': group_name,
        'group_avatar': group_avatar,
        'users_count':users_count,
        'group_description': group_description,
        'group_avatar_small':group_avatar_small

    }
    return render(request, 'main/vk_page.html', context)


def vk_third_page(request):
    session = vk.Session()
    api = vk.API(session)

    group_info = api.groups.getById(group_id=69273673, version=5.59)
    group_users_info = api.groups.getMembers(group_id=69273673, version=5.59)

    users_count=group_users_info['count']
    group_name = group_info[0]['name']
    group_description = group_info[0]['screen_name']
    group_avatar_small = group_info[0]['photo']
    group_avatar = group_info[0]['photo_big']

    wall = api.wall.get(owner_id=-69273673, count=10, extended=1, version=5.59)
    src_img_arr = []
    likes_arr = []
    i = 1
    while i < 10:
        if wall['wall'][i]['attachments'][0]['type'] == 'photo':
            src_img_arr.append(wall['wall'][i]['attachments'][0]['photo']['src_big'])
            likes_arr.append(wall['wall'][i]['likes']['count'])
            i += 1
        else:
            i += 1
            continue



    context = {
        'likes_arr':likes_arr,
        'src_img_arr': src_img_arr,
        'group_name': group_name,
        'group_avatar': group_avatar,
        'users_count':users_count,
        'group_description': group_description,
        'group_avatar_small':group_avatar_small

    }
    return render(request, 'main/vk_page.html', context)

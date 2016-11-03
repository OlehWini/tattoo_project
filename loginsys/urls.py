from django.conf.urls import url
from . import views

app_name = 'loginsys'

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),

]
# https://www.youtube.com/watch?v=QgdINlxm-wE&list=PLpTASIMYgCp8supkEmnnrYa5xi9g91ZPI
from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id
from main.views import show_json_by_id, register, login_user, logout_user,  delete_product_ajax, add_stock, sub_stock, get_product_json, add_product_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete_product_ajax/<int:id>', delete_product_ajax, name='delete_product_ajax'),
    path('add_stock/<int:id>/', add_stock, name='add_stock'),
    path('sub_stock/<int:id>/', sub_stock, name='sub_stock'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', add_product_ajax, name='add_product_ajax')
]
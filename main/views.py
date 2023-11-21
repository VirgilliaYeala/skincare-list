import datetime
import json
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from main.forms import ProductForm
from main.models import Product
from django.urls import reverse
from django.core import serializers
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)
    
    # Ambil pesan notifikasi dari sesi
    notification_message = request.session.get('notification_message', None)
    
    # Hapus pesan notifikasi dari sesi
    if 'notification_message' in request.session:
        del request.session['notification_message']
    
    # Cek apakah cookies 'last_login' ada
    last_login = request.COOKIES.get('last_login', None)

    context = {
        'name': request.user.username,
        'products': products,
        'notification_message': notification_message,
        'last_login': last_login,  # Gunakan nilai yang diperoleh dari cookies atau None jika tidak ada
    }

    return render(request, "main.html", context)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Product.objects.create(
            user = request.user,
            brand = data["brand"],
            name = data["name"],
            price = int(data["price"]),
            amount = int(data["amount"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

def delete_product_ajax(request, id):
    product = Product.objects.get(pk= id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
    
def add_stock(request, id = None):
    product = Product.objects.get(pk=id)
    product.amount += 1
    product.save()
    return HttpResponseRedirect(reverse('main:show_main'))
    
def sub_stock(request, id = None):
    product = Product.objects.get(pk=id)
    if product.amount > 1:
        product.amount -= 1
        product.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()

        # Ambil data produk terakhir yang dimasukkan
        latest_product = Product.objects.latest('id')
        
        # Buat pesan notifikasi dengan informasi produk terakhir
        notification_message = f"Kamu menyimpan skincare {latest_product.brand} dengan jumlah {latest_product.amount}."
        
        # Simpan pesan notifikasi di dalam sesi untuk ditampilkan di halaman utama
        request.session['notification_message'] = notification_message
        
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
        
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def get_product_json(request):
    product_item = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        brand = request.POST.get("brand")
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        price = request.POST.get("price")
        user = request.user

        new_product = Product(brand=brand, name=name, amount=amount, description=description,price=price, user=user)
        new_product.save()

        return HttpResponse(f"Kamu menyimpan skincare {brand} dengan jumlah {amount}.", status=201)


    return HttpResponseNotFound()

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

from django.http import HttpResponseRedirect, HttpResponse
from main.forms import ProductForm
from django.urls import reverse
from django.shortcuts import render
from django.core import serializers

from main.models import Product

def show_main(request):
    products = Product.objects.all()
    
    # Ambil pesan notifikasi dari sesi
    notification_message = request.session.get('notification_message', None)
    
    # Hapus pesan notifikasi dari sesi
    if 'notification_message' in request.session:
        del request.session['notification_message']
    
    context = {
        'name': 'Virgillia Yeala Prabowo',
        'class': 'PBP E',
        'products': products,
        'notification_message': notification_message,
    }

    return render(request, "main.html", context)


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        
        # Ambil data produk terakhir yang dimasukkan
        latest_product = Product.objects.latest('id')
        
        # Buat pesan notifikasi dengan informasi produk terakhir
        notification_message = f"Kamu menyimpan skincare {latest_product.brand} dengan jumlah {latest_product.amount}."
        
        # Simpan pesan notifikasi di dalam sesi untuk ditampilkan di halaman utama
        request.session['notification_message'] = notification_message
        
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)



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

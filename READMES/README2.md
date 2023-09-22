# Tugas 3
## Apa perbedaan antara form POST dan form GET dalam Django?
**Form POST**:
1. Menggunakan metode HTTP POST untuk mengirim data.
2. Data dikirim dalam tubuh permintaan HTTP dan tidak terlihat dalam URL.
3. Cocok digunakan untuk mengirim data yang bersifat sensitif atau data yang ingin disembunyikan dari pengguna.
4. Data yang dikirim tidak terlihat dalam baris alamat browser, sehingga lebih aman.
   
**Form GET**:
1. Menggunakan metode HTTP GET untuk mengirim data.
2. Data dikirim sebagai bagian dari URL dan terlihat dalam tautan atau baris alamat browser.
3. Cocok digunakan untuk mengambil data dari server.
4. Data yang dikirim dapat dengan mudah di-bookmark atau dibagikan karena terlihat dalam URL.
5. Tidak aman untuk mengirim data sensitif, seperti kata sandi, karena terlihat dalam URL.

## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
**XML**:
1. XML adalah bahasa markup yang digunakan untuk mengatur dan mengirim data dalam bentuk yang dapat dibaca oleh manusia maupun komputer.
2. XML memiliki aturan yang ketat dalam hal struktur dan validasi data melalui DTD (Document Type Definition) atau XML Schema.
3. Dapat digunakan untuk menggambarkan struktur data yang kompleks dan memiliki kemampuan untuk mendefinisikan sendiri elemen dan atribut.
4. Digunakan secara luas dalam pertukaran data terstruktur antar sistem dan dalam berbagai konteks seperti SOAP (Simple Object Access Protocol) dalam layanan web.
   
**JSON**:
1. JSON adalah format pertukaran data yang ringan dan mudah dibaca oleh manusia.
2. Berdasarkan notasi objek JavaScript, JSON memiliki sintaksis yang lebih sederhana dibandingkan dengan XML.
3. JSON mendukung tipe data seperti objek, array, string, angka, boolean, dan null.
4. Umumnya digunakan dalam pengembangan web dan aplikasi yang memerlukan pertukaran data antara server dan klien. Selain itu, JSON juga digunakan dalam API RESTful.

**HTML**:
1. HTML adalah bahasa markup yang digunakan untuk membuat halaman web dan mengatur cara tampilan dan struktur konten di browser web.
2. HTML terutama digunakan untuk mengatur tampilan dan interaksi dengan pengguna dalam konteks pengembangan web.
3. Meskipun HTML juga dapat digunakan untuk mengirim data, penggunaan utamanya adalah dalam membuat antarmuka pengguna dan menampilkan informasi di halaman web.

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON (JavaScript Object Notation) sering digunakan dalam pertukaran data antara aplikasi web modern karena kemudahan penggunaan, efisiensi, dan dukungan yang luas. JSON memiliki sintaksis yang sederhana dan mudah dibaca oleh manusia, serta ringan sehingga mengurangi beban jaringan. Selain itu, JSON berasal dari notasi objek JavaScript, sehingga mudah diintegrasikan dengan bahasa pemrograman yang banyak digunakan dalam pengembangan web. Format ini juga mendukung berbagai tipe data, seperti objek, array, string, angka, boolean, dan null, menjadikannya fleksibel untuk merepresentasikan berbagai jenis data. JSON digunakan secara luas dalam pengembangan API RESTful, yang merupakan pendekatan umum dalam pembangunan aplikasi web modern. Keterbacaan dalam log dan kemudahan debugging adalah keuntungan tambahan. Dengan semua keunggulan ini, JSON telah menjadi format standar untuk pertukaran data antara aplikasi web, memfasilitasi komunikasi yang efisien dan efektif di seluruh ekosistem web.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### Membuat input form untuk menambahkan objek model pada app sebelumnya
1. saya buka direktori `main`, kemudian saya buat file baru dengan nama `forms.py` dan tambahkan kode berikut ke file tersebut :
   ```python
   from django.forms import ModelForm
   from main.models import Product
   
   class ProductForm(ModelForm):
       class Meta:
           model = Product
           fields = ["brand","name", "amount", "description", "price"]
     ```
2. Di direktori yang sama, saya menambahkan beberapa import berikut ke file `views.py` :
   ```python
   from django.http import HttpResponseRedirect
   from main.forms import ProductForm
   from django.urls import reverse
     ```
3. Di `views.py`, saya menambahkan beberapa fungsi baru berikut ini dengan nama `create_product` dengan parameter `request` :
   ```python
   def create_product(request):
       form = ProductForm(request.POST or None)
   
       if form.is_valid() and request.method == "POST":
           form.save()
           return HttpResponseRedirect(reverse('main:show_main'))
   
       context = {'form': form}
       return render(request, "create_product.html", context)
     ```
4. Tidak hanya itu, saya juga mengubah fungsi `show_main` di berkas `views.py` dengan kode berikut :
   ```python
   def show_main(request):
       products = Product.objects.all()
   
       context = {
           'name': 'Virgillia Yeala Prabowo', # Nama kamu
           'class': 'PBP E', # Kelas PBP kamu
           'products': products
       }
   
       return render(request, "main.html", context)
     ```
5. Di file `urls.py` saya menambahkan beberapa kode berikut :
   import fungsi `create_product`
   ```python
   from main.views import show_main, create_product
   ```
   menambahkan path url ke dalam `urlpatterns`
   ```python
   path('create-product', create_product, name='create_product'),
   ```
6. Saya membuat berkas HTML baru dengan nama file `create_product.html` di direktori `main/templates` dengan kode berikut ini :
   ```python
   {% extends 'base.html' %} 

   {% block content %}
   <h1>Add New Product</h1>
   
   <form method="POST">
       {% csrf_token %}
       <table>
           {{ form.as_table }}
           <tr>
               <td></td>
               <td>
                   <input type="submit" value="Add Product"/>
               </td>
           </tr>
       </table>
   </form>
   
   {% endblock %}
   ```
7. Saya mengubah file `main.html` saya dengan menambahkan beberapa kode berikut :
   ```python
   ...
   <table>
       <tr>
           <th>Name</th>
           <th>Price</th>
           <th>Description</th>
           <th>Date Added</th>
       </tr>
   
       {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}
   
       {% for product in products %}
           <tr>
               <td>{{product.name}}</td>
               <td>{{product.price}}</td>
               <td>{{product.description}}</td>
               <td>{{product.date_added}}</td>
           </tr>
       {% endfor %}
   </table>
   
   <br />
   
   <a href="{% url 'main:create_product' %}">
       <button>
           Add New Product
       </button>
   </a>
   
   {% endblock content %}
   ```
### Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.
**Format HTML**
1. Dalam format html sudah dilakukan pada tugas 2 yaitu dengan membuat berkas html `main.html` untuk menampilkan data yang telah ditambahkan. 
2. Membuat fungsi pada `views.py` di direktori mian dengan kode
    ```python
    def show_main(request):
    Items = Item.objects.all()

    if ((Items.count() == 0)):
      context = {
          'data' : default_book
      }
    else:
      context = {
          'data' : Items
      }

    return render(request, "main.html", context)
    ```
**Format XML dan XML by ID**
1. Membuka file `views.py` dan menambahkan terlebih dahulu import berikut :
   ```python
   from django.http import HttpResponse
   from django.core import serializers
   ```
2. Membuat fungsi baru dalam berkas `views.py` di direktori `main` dengan nama `show_xml` untuk menampilkan format XML dan `show_xml_by_id` untuk menampilkan format XML dengan ID tertentu.
3. Untuk `show_xml` yang menampilkan semua data maka ditambahkan kode untuk mengambil data dengan `Product.objects.all()` dan untuk `show_xml_by_id` yang menampilkan data dengan ID tertentu ditambahkan kode dengan melakukan filter yaitu dengan `Product.objects.filter(pk=id)`
3. Kemudian data akan diubah menjadi format XML dengan `serializers.serialize("xml",data)` sehingga menampilkan format XML. Kurang lebih kode akan menjadi
    ```python
    def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```

**Format JSON dan JSON by ID**
1. Membuka file `views.py` dan menambahkan terlebih dahulu import berikut :
   ```python
   from django.http import HttpResponse
   from django.core import serializers
   ```
2. Menambahkan fungsi `show_json` di direktori `main` untuk menampilkan format JSON dan `show_json_by_id` untuk menampilkan format JSON by ID. Sehingga `views.py` dalam direktori `main` ditambahkan dengan kode berikut :
    ```python
    def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
### Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.
1. **Format HTML**   :
   untuk format HTML, saya hanya perlu menambahkan beberapa potongan kode berikut ke file `urls.py` yang berada di direktori `main` :
   ```bash
   path('', show_main, name='show_main'),
   ```
2. **Format XML dan XML by ID**   :
   untuk Format XML dan XML by ID, saya perlu menambahkan potongan kode berikut :
   import fungsi 
   ```python
   from main.views import show_main, create_product, show_xml, show_xml_by_id
   ```
   menambahkan path url di `urlspatterns`
   ```python
   urlpatterns = [
       ...
       path('xml/', show_xml, name='show_xml'),
       path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id')
       ...
   ]
   ```
3. **Format JSON dan JSON by ID**   :
   untuk Format JSON dan JSON by ID, saya perlu menambahkan potongan kode berikut :
   import fungsi
   ```python
   from main.views import show_main, show_landing_page, create_book, show_xml, show_json, show_xml_by_id, show_json_by_id
   ```
   menambahkan path url di `urlpatterns`
   ```python
   urlpatterns = [
       ...
       path('json/', show_json, name='show_json'), 
       path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
       ...
   ]
   ```
### Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
1. **Format HTML**
   ![image](https://github.com/VirgilliaYeala/skincare-list/assets/124979875/85be7d78-bfb8-49de-9670-a9e3a9a081a2)
2. **Format XML**
   ![image](https://github.com/VirgilliaYeala/skincare-list/assets/124979875/47e4a3e0-edd0-42a3-9faa-cd31aca09c6e)
3. **Format XML by ID**
   ![image](https://github.com/VirgilliaYeala/skincare-list/assets/124979875/465181e8-e4a9-4cb8-a7d1-7f0676a01291)
4. **Format JSON**
   ![image](https://github.com/VirgilliaYeala/skincare-list/assets/124979875/f05e5498-6719-41fe-9456-b65f65254cf5)
5. **Format JSON by ID**
   ![image](https://github.com/VirgilliaYeala/skincare-list/assets/124979875/4f0b631a-8719-4587-8001-aea567459187)

## Bonus 
Untuk implementasi bonus ini ada beberapa hal yang saya ubah di file `views.py` yaitu :
1. di fungsi `create_product`, saya menambahkan beberapa logika untuk bisa mengambil data produk terakhir yang dimasukkan oleh pengguna setelah produk berhasil di simpan :
   ```python
   ...
           # Ambil data produk terakhir yang dimasukkan
           latest_product = Product.objects.latest('id')
           
           # Buat pesan notifikasi dengan informasi produk terakhir
           notification_message = f"Kamu menyimpan skincare {latest_product.brand} dengan jumlah {latest_product.amount}."
           
           # Simpan pesan notifikasi di dalam sesi untuk ditampilkan di halaman utama
           request.session['notification_message'] = notification_message
   ...
   ```
2. di fungsi `show_main`, saya juga menambahkan beberapa logika untuk mengambil pesan notifikasinya dari sesi dan kemudian pesannya bakal di hapus dari sesi agar hanya dapat ditampilkan sekali saja :
   ```python
   ...
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
   ...
   ```
3. lalu di `main.html`, saya menambahkan potongan kode berikut :
   ```python
   {% if notification_message %}
   <div class="notification">
       {{ notification_message }}
   </div>
   {% endif %}
   ```
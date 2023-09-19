[Skincare List Adabtable](https://my-skincare-app.adaptable.app/main/)
# Tugas 2
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawaban :
### Membuat Proyek Django baru
1. karena saya belom pernah menginstal Django sebelumnya, maka saya harusmembuat direktori dengan `skincare_list` dan menjalankan virtual environment dengan menjalankan perintah `python -m venv env` dan mengaktifkan nya dengan perintah `env\Scripts\activate.bat`.
2. Kemudian, saya membuat berkas `requirements.txt` yang berisikan :
   ```text
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
3. saya menjalankan perintah berikut di terminal saya dengan posisi virtual environment aktif.
   ```bash
    pip install -r requirements.txt
   ```
4. karena tugas ini adalah sebuah proyek baru (selain dari tutorial) maka saya harus menjalankan perintah :
   ```bash
    django-admin startproject skincare_list'
   ```
5. supaya nanti bisa di deployment, maka saya harus menambahkan `*` di `settings.py` di bagian `ALLOWED_HOSTS`.

### Membuat Aplikasi Main
setelah saya sudah membuat proyek baru, selanjutnya saya menjalankan perintah berikut untuk memulai proses pembuatan proyek aplikasi `skincare_list` saya.
  ```bash
  python manage.py startapp main
  ```
kemudian saya mendaftarkan aplikasi main ke dalam proyek saya dengan manambahkan `main` di `settings.py` seperti berikut :
```python
  INSTALLED_APPS = [
    ...,
    'main',
    ...
  ]
  ```

### Melakukan Routing pada Proyek
untuk tahap ini, saya perlu membuka file `urls.py` di direktori proyek saya yaitu dengan menambahkan beberapa path berikut :
```python
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('main/', include('main.urls')),  # Tambahkan baris ini
  ]
  ```

### Membuat Model Item
untuk membuat mode item, saya membuat file `models.py` yang ada di direktori proyek saya dan menuliskan model item yang harus ada di proyek saya, yaitu `name`, `amount`, dan `description`. untuk proyek saya ini, saya tidak menambahkan model item lain selain yang sudah disebutkan. setelah itu, saya melakukan migrasi dengan menjalankan perintah berikut :
```bash
  python manage.py makemigrations
  ```
dan 
``` bash
  python manage.py migrate
  ```
untuk mengelola struktur database dari proyek yang saya buat.

### Membuat fungsi dalam views.py
1. saya harus membuat direktori baru dengan nama `templates` di dalam direktori aplikasi `main`
2. di dalam direktori tersebut, saya membuat berkas html baru dengan nama `main.html`. saya hanya menambahkan beberapa data yang di minta soal, yaitu dari `nama aplikasi saya`, `nama saya`, dan `kelas saya`.
   
### Membuat routing pada urls.py pada aplikasi main
step ini berbeda dengan step yang ketiga, karena `urls.py` ini perlu kita buat di direktori main dengan path berikut :
```python
  from django.urls import path
  from main.views import show_main, show_landing_page

  app_name = 'main'

  urlpatterns = [
      path('main/', show_main, name='show_main'),
      path('', show_landing_page, name='show_landing_page'),
  ]
  ```

### Deployment ke adaptable
setelah step sebelumnya sudah dilakukan dengan baik, saya perlu sign-in ke adaptable nya dengan menggunakan akun GitHub saya dan mengunggah direktori proyek kita ke adaptablenya. setelah saya mengisi beberapa hal yang memang harus di lengkapi seperti `deployment branch, template deployment, tipe basis data, dan start command`, adaptable akan melakukan proses `Deploy App` untuk deployment proyek aplikasi saya ini.

### Membuat sebuah README.md
untuk step terakhir ini, saya hanya perlu mengisi beberapa pertanyaan yang sudah di sediakan oleh tim dosen dan tim asdos untuk mereview kembali materi yang sudah diajarkan dosen di kelas dan pada asdos di sesi tutorial.

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
<<<<<<< HEAD
Jawaban :
![Bagan Request Client](./src/image1.png)
=======
<img width="717" alt="image1" src="https://github.com/VirgilliaYeala/skincare-list/assets/124979875/1fa729e8-15e5-4541-a7f6-3a7133f3947a">

>>>>>>> ca139f456c03793448d335affc290534f943f258
### request client
Client akan mengirimkan permintaan ke aplikasi web Django berupa URL tertentu melalui browser atau aplikasi lainnya
### urls.py
Django akan mencocokkan URL yang diterima dari client dengan pola URL yang telah didefinisikan. Jika URL cocok, Django akan memetakan permintaan ke fungsi view yang sesuai
### views.py
`views.py` berisi logika untuk mengambil, memproses, atau memanipulasi data yang diperlukan dari database yang jika sesuai, view akan menerima permintaan dari urls.py. Setelah data diproses, view akan mempersiapkan konteks yang akan disematkan dalam template HTML.
### models.py
`views.py` dapat berinteraksi dengan database melalui model yang telah didefinisikan dalam file `models.py`. Model ini menggambarkan struktur tabel dalam database dan menyediakan API untuk mengakses dan memanipulasi data. Data yang diperoleh dari database dapat digunakan dalam `views.py` untuk kemudian disajikan dalam template HTML.
### templates HTML
Template dapat mengambil data dari konteks yang diberikan oleh view dan menampilkan data tersebut sesuai dengan desain tampilan yang telah didefinisikan.

## Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jawaban :
Dengan virtual environment, setiap proyek dapat memiliki dependensi dan paket Python yang berbeda-beda tanpa konflik, menghindari masalah konflik dependensi dan masalah kompatibilitas antar-proyek. Selain itu, penggunaan virtual environment menjaga proyek-proyek tetap bersih dan terorganisir dengan menyimpan semua dependensi proyek, termasuk interpreter Python, dalam direktori terisolasi. Ini juga memudahkan replikasi lingkungan pengembangan, pengelolaan dependensi yang efisien, penggunaan versi Python yang berbeda, dan melindungi lingkungan Python sistem operasi dari perubahan yang tidak diinginkan yang dapat menyebabkan masalah dengan aplikasi atau paket sistem.

## Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
Jawaban :
1. MVC (Model-View-Controller)
   merupakan sebuah pola desain arsitektural yang digunakan dalam pengembangan perangkat lunak, termasuk dalam pengembangan    aplikasi web. MVC terdiri dari :
   - Model, yaitu Representasi data dan logika bisnis dalam aplikasi. Model mengurus pengelolaan data dan berinteraksi           dengan database.
   - View, yaitu Bertanggung jawab untuk menampilkan informasi kepada pengguna. Ini adalah komponen tampilan yang                menampilkan data dari Model kepada pengguna.
   - Controller, yaitu Menangani interaksi pengguna dan mengontrol aliran aplikasi. Ini menerima input dari pengguna,
     memprosesnya, dan memutuskan bagaimana data dari Model akan ditampilkan oleh View 
2. MVT (Model-View-Template)
   merupakan sebuah varian dari MVC yang digunakan dalam kerangka kerja Django, yang merupakan kerangka kerja pengembangan aplikasi web Python. MVT terdiri dari :
   - Model: Mirip dengan konsep dalam MVC, Model mengelola data dan logika bisnis.
   - View: Bertanggung jawab untuk menampilkan data kepada pengguna seperti dalam MVC.
   - Template: Template adalah bagian yang unik dari MVT. Ini berisi kode HTML yang digunakan untuk merender tampilan. 
3. MVVM (Model-View-ViewModel)
   merupakan sebuah pola desain arsitektural yang sering digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI), terutama dalam pengembangan aplikasi seluler dan desktop. MVVM terdiri dari :
   - Model: Sama dengan konsep dalam MVC dan MVT, Model mengelola data dan logika bisnis.
   - View: Mirip dengan View dalam MVC dan MVT, View menampilkan data kepada pengguna.
   - ViewModel: Ini adalah komponen unik dalam MVVM. ViewModel bertindak sebagai penghubung antara Model dan View. 
4. Perbedaan utama di antara ketiganya
   - Model-View-Controller (MVC) adalah pola arsitektur yang digunakan dalam pengembangan aplikasi perangkat lunak. Dalam
     MVC, Model bertanggung jawab untuk mengelola data dan logika bisnis, View menampilkan data kepada pengguna serta
     mengumpulkan input dari pengguna, sedangkan Controller mengatur aliran program, menerima input dari pengguna melalui
     View, dan berkomunikasi dengan Model. MVC sering digunakan dalam pengembangan aplikasi web dan desktop, dan membantu
     dalam pemisahan tugas-tugas aplikasi untuk memudahkan pengembangan dan pemeliharaan.

   - Model-View-Template (MVT) adalah varian dari MVC yang digunakan dalam framework web Django. Seperti MVC, Model dalam
     MVT tetap bertanggung jawab untuk mengelola data, sedangkan View mengatur tampilan data dan logika utama yang
     melakukan pemrosesan terhadap permintaan yang masuk. Perbedaan utama adalah adanya Template, yang adalah komponen
     tambahan yang mengatur cara tampilan web dibangun dan disusun. MVT membantu pengembang Django untuk merancang dan
     memisahkan tampilan web dengan lebih terstruktur.

   - Model-View-ViewModel (MVVM) adalah pola arsitektur yang digunakan khususnya dalam pengembangan aplikasi berbasis
     antarmuka pengguna (UI), terutama aplikasi mobile dan desktop. Model dalam MVVM tetap mengelola data, View merupakan
     antarmuka pengguna yang menampilkan data dan merespons tindakan pengguna, sedangkan ViewModel adalah perantara antara
     Model dan View. ViewModel menghubungkan data Model ke tampilan View dan berisi logika bisnis terkait tampilan. MVVM
     membantu dalam memisahkan logika bisnis tampilan dari tampilan itu sendiri, memungkinkan pengembangan UI yang lebih
     fleksibel dan terkelola.

## Bonus
Saya berhasil mengimplementasikan testing dasar yang dapat dilihat pada `./main/tests.py` yang melakukan testing untuk Model data dan response routing dengan menjalankan perintah `python manage.py test`
<img width="717" alt="image2" src="https://github.com/VirgilliaYeala/skincare-list/assets/124979875/a4cf8516-34fa-44c7-8897-99f09a858470">

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

[Skincare List Adabtable](https://my-skincare-app.adaptable.app/main/)

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
Jawaban :
<img width="717" alt="image1" src="https://github.com/VirgilliaYeala/skincare-list/assets/124979875/1fa729e8-15e5-4541-a7f6-3a7133f3947a">

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

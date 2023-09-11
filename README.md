[Skincare List Adabtable](https://my-skincare-app.adaptable.app/main/)

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawaban :
### Membuat Proyek Django baru
1. karena saya belom pernah menginstal Django sebelumnya, maka saya harusmembuat direktori dengan 'skincare_list' dan menjalankan virtual environment dengan menjalankan perintah 'python -m venv env' dan mengaktifkan nya dengan perintah 'env\Scripts\activate.bat'.
2. Kemudian, saya membuat berkas 'requirements.txt' yang berisikan :
   ```text
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
3. saya menjalankan perintah berikut  di terminal saya dengan posisi virtual environment aktif.
   ```bash
    pip install -r requirements.txt
   ```
4. karena tugas ini adalah sebuah proyek baru (selain dari tutorial) maka saya harus menjalankan perintah :
   ```bash
    django-admin startproject skincare_list'
   ```
5. supaya nanti bisa di deployment, maka saya harus menambahkan '*' di 'settings.py' di bagian 'ALLOWED_HOSTS'.

### Membuat Aplikasi Main
setelah saya sudah membuat proyek baru, selanjutnya saya menjalankan perintah berikut untuk memulai proses pembuatan proyek aplikasi 'skincare_list' saya.
  ```bash
  python manage.py startapp main
  ```
kemudian saya mendaftarkan aplikasi main ke dalam proyek saya dengan manambahkan 'main' di 'settings.py' seperti berikut :
```python
  INSTALLED_APPS = [
    ...,
    'main',
    ...
  ]
  ```

### Melakukan Routing pada Proyek
untuk tahap ini, saya perlu membuka file 'urls.py' di direktori proyek saya yaitu dengan menambahkan beberapa path berikut :
```python
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('main/', include('main.urls')),  # Tambahkan baris ini
  ]
  ```

### Membuat Model Item
untuk membuat mode item, saya membuat file 'models.py' yang ada di direktori proyek saya dan menuliskan model item yang harus ada di proyek saya, yaitu 'name', 'amount', dan 'description'. untuk proyek saya ini, saya tidak menambahkan model item lain selain yang sudah disebutkan. setelah itu, saya melakukan migrasi dengan menjalankan perintah berikut :
```bash
  python manage.py makemigrations
  ```
dan 
``` bash
  python manage.py migrate
  ```
untuk mengelola struktur database dari proyek yang saya buat.

### Membuat fungsi dalam views.py
1. saya harus membuat direktori baru dengan nama 'templates' di dalam direktori aplikasi 'main'
2. di dalam direktori tersebut, saya membuat berkas html baru dengan nama 'main.html'. saya hanya menambahkan beberapa data yang di minta soal, yaitu dari 'nama aplikasi saya', 'nama saya', dan 'kelas saya'.
   
# Membuat routing pada urls.py pada aplikasi main
step ini berbeda dengan step yang ketiga, karena urls.py ini perlu kita buat di direktori main dengan path berikut :
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
setelah step sebelumnya sudah dilakukan dengan baik, saya perlu sign-in ke adaptable nya dengan menggunakan akun GitHub saya dan mengunggah direktori proyek kita ke adaptablenya. setelah saya mengisi beberapa hal yang memang harus di lengkapi seperti deployment branch, template deployment, tipe basis data, dan start command, adaptable akan melakukan proses 'Deploy App' untuk deployment proyek aplikasi saya ini.

### Membuat sebuah README.md
untuk step terakhir ini, saya hanya perlu mengisi beberapa pertanyaan yang sudah di sediakan oleh tim dosen dan tim asdos untuk mereview kembali materi yang sudah diajarkan dosen di kelas dan pada asdos di sesi tutorial.

# Tugas 4
## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
Jawaban : Django UserCreationForm adalah impor formulir bawaan yang memudahkan pembuatan formulir pendaftaran pengguna dalam aplikasi web. Dengan formulir ini, pengguna baru dapat mendaftar dengan mudah di situs web Anda tanpa harus menulis kode dari awal.
| ------------- | ------------- |
| mempercepat proses pendaftaran pengguna | tidak memenuhi kebutuhan desain yang lebih kompleks atau khusus  |
| melakukan validasi otomatis dalam pendaftaran  | perlu menambahkan fitur pendaftaran yang lebih kompleks secara manual  |
| memudahkan penyimpanan dan manajemen data pengguna | masih harus menangani logika bisnis tambahan setelah pendaftaran berhasil  |
| custom perilaku form sesuai dengan kebutuhan aplikasi Anda  | tidak cocok untuk aplikasi yang lebih kompleks  |

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
| autentikasi  | otorisasi |
| ------------- | ------------- |
| proses verifikasi identitas pengguna yang mencoba mengakses aplikasi | proses yang mengendalikan hak akses pengguna yang sudah terotentikasi ke berbagai bagian dari aplikasi  |
|  umumnya mencakup username dan password (autentikasi lainnya : media sosial atau pihak ketiga)  | mengacu pada pengaturan izin yang diberikan kepada pengguna  |
| memiliki built-in sistem autentikasi yang dapat mengelola proses autentikasi | menyediakan sistem otorisasi yang kuat dengan konsep "objek-objek izin"  |
Alasan keduanya penting :
Kedua konsep ini bekerja bersama untuk menciptakan aplikasi web yang aman dan berfungsi dengan baik. Autentikasi memastikan identitas pengguna, sementara otorisasi mengontrol apa yang dapat mereka lakukan setelah terotentikasi. Dengan mengimplementasikan baik autentikasi maupun otorisasi dalam Django, Anda dapat mengembangkan aplikasi yang aman, andal, dan sesuai dengan kebutuhan bisnis Anda.

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies adalah mekanisme penyimpanan data kecil yang disimpan di dalam browser web dan digunakan dalam konteks aplikasi web untuk menyimpan informasi yang dapat diakses oleh server web pada kunjungan selanjutnya. Django menggunakan cookies untuk mengelola data sesi pengguna melalui middleware dan pustaka yang disebut "django.contrib.sessions." Berikut adalah cara Django menggunakan cookies untuk mengelola sesi pengguna:
1. Django menggunakan `SessionMiddleware`. kita harus mengaktifkannya dalam pengaturan Django kita. Ini biasanya dilakukan dengan menambahkannya ke `MIDDLEWARE` di berkas `settings.py`.
    ```python
        MIDDLEWARE = [
        # ...
        'django.contrib.sessions.middleware.SessionMiddleware',
        # ...
    ]
    ```
2. Ketika pengguna mengakses situs web kita, SessionMiddleware akan menciptakan sesi pengguna dan menyimpan ID sesi di cookie yang dikirimkan ke browser pengguna.
3. kita dapat menyimpan dan mengambil data dalam sesi pengguna menggunakan objek request.session dalam view Django Anda. contoh :
    ```python
        # Menyimpan data dalam sesi pengguna
        request.session['user_id'] = 123

        # Mengambil data dari sesi pengguna
        user_id = request.session.get('user_id')
    ```

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies dalam pengembangan web dapat aman jika diimplementasikan dengan benar, tetapi juga ada risiko potensial yang harus diwaspadai. Berikut adalah beberapa hal yang menjadi risiko potensial keamanan aplikasi web Anda:
1. Cross-Site Scripting (XSS)
2. Cross-Site Request Forgery (CSRF):
3. Session Hijacking
4. Cookie Poisoning
Penting untuk memahami bahwa risiko ini dapat diminimalkan dengan menerapkan praktik keamanan yang tepat, seperti penggunaan cookies HttpOnly, enkripsi data sensitif, dan pengaturan cookies yang benar.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
#### registrasi
1. menjalankan virtual environment dengan menjalankan perintah `env\Scripts\activate.bat`.
2. membuka file `views.py` di direktori main dan menambahkan beberapa import berikut :
```bash
    from django.shortcuts import redirect
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages  
```
lalu menambahkan fungsi `register` baru di file yang sama :
```python
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
```
3. kemudian di `main/templates` membuat file HTML baru dengan nama `register.html` dan diisi dengan kode berikut :
```pyhton
    {% extends 'base.html' %}

    {% block meta %}
        <title>Register</title>
    {% endblock meta %}

    {% block content %}  

    <div class = "login">
        
        <h1>Register</h1>  

            <form method="POST" >  
                {% csrf_token %}  
                <table>  
                    {{ form.as_table }}  
                    <tr>  
                        <td></td>
                        <td><input type="submit" name="submit" value="Daftar"/></td>  
                    </tr>  
                </table>  
            </form>

        {% if messages %}  
            <ul>   
                {% for message in messages %}  
                    <li>{{ message }}</li>  
                    {% endfor %}  
            </ul>   
        {% endif %}

    </div>  

    {% endblock content %}
```
4. pergi ke file `urls.py` di direktori main dan menambahkan beberapa kode berikut :
- menambahkan import baru
    ```bash
        from main.views import register
    ```
- menambahkan path url baru
    ```bash
    path('register/', register, name='register'),
    ```
#### login
1. buka file `views.py` yang ada di direktori main dan tambahkan beberapa kode berikut :
```python
    from django.contrib.auth import authenticate, login

    def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:show_main')
            else:
                messages.info(request, 'Sorry, incorrect username or password. Please try again.')
        context = {}
        return render(request, 'login.html', context)
```
2. pergi ke direktori `main/templates` dan buat file HTML baru dengan format nama `login.html` dan tambahkan beberapa kode dibawah ini :
```python
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```
3. pergi ke file `urls.py` di direktori main dan menambahkan beberapa kode berikut :
- menambahkan import baru
    ```bash
        from main.views import login_user
    ```
- menambahkan path url baru
    ```bash
    path('login/', login_user, name='login'),
    ```

#### logout
1. buka file `views.py` yang ada di direktori main dan tambahkan beberapa kode berikut :
```python
    from django.contrib.auth import logout

    def logout_user(request):
    logout(request)
    return redirect('main:login')
```
2. pergi ke direktori `main/templates` dan buka file HTML `main.html` dan Tambahkan potongan kode di bawah ini setelah hyperlink tag untuk Add New Product pada berkas `main.html` :
```python
    ...
    <a href="{% url 'main:logout' %}">
        <button>
            Logout
        </button>
    </a>
    ...
```
3. pergi ke file `urls.py` di direktori main dan menambahkan beberapa kode berikut :
- menambahkan import baru
    ```bash
        from main.views import logout_user
    ```
- menambahkan path url baru
    ```bash
    path('logout/', logout_user, name='logout'),
    ```
### Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
1. Setelah checklist pertama sudah di lakukan dan dipastikan tidak ada yang error, saya menjalankan proyek saya ini dengan menulis perintah :
```bash
python manage.py runserver
```
2. membuat 2 akun baru dengan fitur `Register Now` dan mengisi data data yang diperlukan untuk register.
3. setelah udah register akun baru, login ke aplikasinya dan `add product` sebanyak 3 kali dengan mengisi data data dari model yang sudah di tentukan, yaitu `[brand, name, amount, description, price]`

### Menghubungkan model Item dengan User
1. buka file `modles.py` yang ada di direktori main dan menambahkan beberapa kode berikut :
- menambahkan import
    ```bash
    from django.contrib.auth.models import User
    ```
- menambahkan kode di class `Product` 
    ```bash
    class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
    ```
2. buka file `views.py` yang ada di direktori main dan ubah beberapa potongan kode berikut :
    ```python
        def create_product(request):
            form = ProductForm(request.POST or None)

            if form.is_valid() and request.method == "POST":
                product = form.save(commit=False)
                product.user = request.user
                product.save()
                return HttpResponseRedirect(reverse('main:show_main'))
            ...
    ```
3. ubah fungsi `show_main` menjadi berikut :
    ```python
        def show_main(request):
        products = Product.objects.filter(user=request.user)

        context = {
            'name': request.user.username,
    ```
4. tidak lupa simpan semua perubahan dengan menjalankan perintah `python manage.py makemigrations` kemudian `python manage.py migrate`

### Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
1. untuk menampilkan informasi `username` pengguna di aplikasi web nya, saya menambahkan potongan kode berikut di file `main.html` saya :
    ```html
    <h4 class="custom-h4">
        Halo! {{name}}
    </h4>
    ```
2. implementasi cookie `last_login` :
- menambahkan beberapa import berikut di file `views.py` direktori `main` :
    ```python
        import datetime
        from django.http import HttpResponseRedirect
        from django.urls import reverse
    ```
    pada fungsi `login_user` kita ubah kode yang ada pada blok if user is not None menjadi potongan kode berikut :
    ```python
        ...
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        ...
    ```
- pada fungsi `show_main` tambahkan kode berikut di dalam `context` :
    ```python
    'last_login': request.COOKIES['last_login'],
    ```
- ubah fungsi `logout_user` menjadi kode berikut :
    ```python
        def logout_user(request):
            logout(request)
            response = HttpResponseRedirect(reverse('main:login'))
            response.delete_cookie('last_login')
            return response
    ```
- untuk menampilkan informasi `last_login`, saya menambahkan potongan kode berikut di file `main.html` saya :
    ```html
    <h5>Sesi terakhir login: {{ last_login }}</h5>
    ```

## Bonus
1. menambahkan fungsi baru di `views.py` seperti potongan kode berikut :
    ```python
    def add_stock(request, id = None):
        product = Product.objects.get(pk=id)
        product.amount += 1
        product.save()
        return redirect('main:show_main')
    
    def sub_stock(request, id = None):
        product = Product.objects.get(pk=id)
        if product.amount > 1:
            product.amount -= 1
            product.save()
        return redirect('main:show_main')
    
    def delete_product(request, id = None):
        product = Product.objects.get(pk=id)
        product.delete()
        return redirect('main:show_main')
    ```
2. menambahkan import berikut di file `urls.py` dan `urlpatterns`nya :
    ```python
    from main.views import add_stock, sub_stock, delete_product

    urlpatterns = [
        ...
        path('add_stock/<int:id>/', add_stock, name='add_stock'),
        path('sub_stock/<int:id>/', sub_stock, name='sub_stock'),
        path('delete/<int:id>/)', delete_product, name='delete'),
        ...
    ]
    ```
3. menambahkan beberapa potongan kode berikut di `main.html` :
    ```html
    <form action="{% url 'main:sub_stock' id=product.id %}" method="POST">
        {% csrf_token %}
        <button type="submit" class="update-button">
            -
        </button>
    </form>
    <div class="custom-font" style="margin-left: 20px; margin-right: 20px;">
        {{product.amount}}
    </div>
    <form action="{% url 'main:add_stock' id=product.id %}" method="POST">
        {% csrf_token %}
        <button type="submit" class="update-button">
            +
        </button>
    </form>
    ```
    dan
    ```html
    <td class="center-td">
        <div class="container">
        <form action="{% url 'main:delete' id=product.id %}" method="POST">
            {% csrf_token %}
            <button type="submit" class="delete-button">Delete</button>
        </form>
        </div>
    </td>
    ```

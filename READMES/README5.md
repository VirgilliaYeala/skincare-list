# Tugas 6
## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Jawaban :
| Asynchronous Programming  | Synchronous Programming |
| ------------- | ------------- |
|  tugas-tugas dieksekusi secara berurutan dan satu per satu | tugas-tugas dieksekusi tanpa harus menunggu satu sama lain  |
| hanya ada satu thread utama yang mengendalikan eksekusi program | menggunakan konsep thread bersamaan atau "event loop" untuk mengelola tugas-tugas yang berjalan secara paralel |
| kodenya lebih sulit untuk di-debug dan dipelihara | kodenya lebih linear  |

## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Jawaban :
Paradigma "event-driven programming" adalah pendekatan  pemrograman di mana eksekusi program dan respons terhadap peristiwa yang terjadi merupakan inti dari desain dan struktur aplikasi. Dalam model ini, program mengikuti alur eksekusi yang ditentukan oleh peristiwa yang terjadi, seperti klik mouse, interaksi pengguna, atau data yang datang dari luar. Aplikasi event-driven programming secara aktif mendengarkan peristiwa ini dan meresponsnya dengan melakukan tindakan atau fungsi tertentu. contoh penerapan pada tugas ini ada di file `main.html` dan di potongan kode berikut:
```html
<script>
...
        function addProduct() {
            fetch("/create-ajax/", {
                method: "POST",
                body: new FormData(document.querySelector('#form'))
            }).then(response => {
                if (response.status === 201) {
                    // Jika respons berhasil, ambil pesan notifikasinya
                    return response.text();
                } else {
                    throw new Error("Failed to add product");
                }
            })
            .then(notificationMessage => {
                // Tampilkan pesan notifikasi jika ada
                if (notificationMessage) {
                    const notificationElement = document.querySelector('.notification');
                    if (notificationElement) {
                        notificationElement.textContent = notificationMessage;
                    }
                }
                // Kemudian, perbarui daftar produk
                refreshProducts();
            })

            document.getElementById("form").reset()
            return false
        }

        // contoh penerapan event-driven programming
        // ketika buttonnya diklik oleh user, maka productnya akan di add
        document.getElementById("button_add").onclick = addProduct 
...
</script>
```

## Jelaskan penerapan asynchronous programming pada AJAX.
Jawaban :
Berikut adalah penerapan asynchronous programming pada AJAX :
1. menggunakan objek XMLHttpRequest (XHR) untuk mengirim permintaan ke server dan menerima respons, karena kode JavaScript dapat terus berjalan tanpa harus menunggu respons server.
2. menetapkan callback function pada properti `onreadystatechange` dari objek XHR untuk menangani respons dari server saat statusnya berubah.
3. menggunakan Fetch API yang berbasis promise untuk mengelola permintaan dan respons secara asynchronous, karena Fetch API menyediakan cara yang lebih modern dan mudah untuk mengelola respons dari server.
4. mengatur mode asynchronous dengan mengatur parameter `true`, supaya kode JavaScript tetap berjalan tanpa harus menunggu respons dari server.
5. Callback functions atau metode `.catch()` pada promise digunakan untuk menangani kesalahan yang mungkin terjadi selama komunikasi dengan server.

## Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.
Jawaban :
### Bandingkanlah kedua teknologi tersebut
| Fetch API  | jQuery |
| ------------- | ------------- |
|  bagian dari standar JavaScript modern (ES6+) dan tidak memerlukan pustaka eksternal  | sebuah pustaka JavaScript eksternal yang harus diunduh dan dimasukkan ke dalam proyek  |
| menggunakan konsep promise untuk mengelola permintaan dan respons | menggunakan pendekatan callback-based untuk mengelola permintaan dan respons |
| memberikan kontrol yang lebih langsung dan lebih sederhana terhadap permintaan HTTP | menyediakan banyak fitur lain seperti manipulasi DOM, animasi, dan event handling  |
| lebih ringan daripada jQuery | lebih berat daripada Fetch API  |

### tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan
Menurut saya teknologi yang lebih baik untuk digunakan tergantung dengan fitur fitur yang nanti akan digunakan di proyek saya nanti.Jika proyek saya relatif sederhana dan saya ingin mengadopsi praktik terbaru dalam pengembangan web, menggunakan Fetch API atau XMLHttpRequest dengan JavaScript native bisa menjadi pilihan yang baik. Namun, jika proyek saya lebih rumit dan tim saya sudah terbiasa dengan jQuery, maka menggunakan jQuery juga dapat menjadi solusi yang baik. 

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
### Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX.
#### AJAX GET
- di direktori `main`, kita pergi ke file `views.py` dan menambahkan fungsi `get_product_json` seperti kode berikut :
    ```python
    def get_product_json(request):
        product_item = Product.objects.all()
        return HttpResponse(serializers.serialize('json', product_item))
    ```
- buka file `urls.py` di direktori yang sama dan menambahkan path berikut :
    ```python
    from main.views import  get_product_json

    urlpatterns = [
        ..
        path('get-product/', get_product_json, name='get_product_json'),
        ..
    ]
    ```
- buka berkar `main.html` pada direktori `main/templates` dan mengubah kode data tablenya menjadi seperti ini :
    ```html
    <table id="product_table"></table>
    ```
- membuat blok `<Script>` di bagian bawah kode saya dan menambahkan fungsi baru dengan nama `getProducts()` seperti kode dibawah ini :
```html
<script>
    async function getProducts() {
        return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
    }
</script>
```
- di blok `<Script>` yang sama kita tambahkan fungsi baru dengan nama `refreshProduct()` :
```html
<script>
    ...
    async function refreshProducts() {
            document.getElementById("product_table").innerHTML = ""
            const products = await getProducts()
            let htmlString = `<tr>
                <th> 
                    <div class = "custom-header">
                        Brand
                    </div>
                </th>
                <th>
                    <div class = "custom-header">
                        Name
                    </div>
                </th>
                <th>
                    <div class = "custom-header">
                        Amount
                    </div>
                </th>
                <th>
                    <div class = "custom-header">
                        Description
                    </div>
                </th>
                <th>
                    <div class = "custom-header">
                        Price
                    </div>
                </th>
            </tr>`

            products.forEach((item, index, array) => {
                htmlString += `\n<tr class="${index === array.length - 1 ? 'last-row' : ''}" style="text-align: center;">
                <td>${item.fields.brand}</td>
                <td>${item.fields.name}</td>
                <td>
                    <div class = "container">
                        <a href="sub_stock/${item.pk}">
                                <button type="submit" class="update-button">
                                    -
                                </button>
                            </a>
                        <div class="custom-font" style="margin-left: 20px; margin-right: 20px;">
                                ${item.fields.amount}
                        </div> 
                        <a href="add_stock/${item.pk}">
                                <button type="submit" class="update-button">
                                    +
                                </button>
                            </a>
                    </div>
                </td>
                <td>${item.fields.description}</td>
                <td>${item.fields.price}</td>
                <td><a href="delete/${item.pk}">
                    <button type="submit" class="delete-button">Delete</button>
                </a></td>
            </tr>` 
            })
            
            document.getElementById("product_table").innerHTML = htmlString
        }

    refreshProducts()
</script>
```

### AJAX POST 
- di dalaM direktori `main`, buka file `views.py` dan menambahkan fungsi baru dengan nama `add_product_ajax` seperti potongan kode berikut :
    ```python
    from django.views.decorators.csrf import csrf_exempt
    ...
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
    ```
- buka file `urls.py` di direktori yang sama dan menambahkan path berikut :
    ```python
    from main.views import add_product_ajax

    urlpatterns = [
        ..
        path('create-ajax/', add_product_ajax, name='add_product_ajax')
        ..
    ]
    ```
- menambahkan beberapa potongan kode berikut sebagai button yang berfungsi untuk menampilkan modal bootstrap sebagai form untuk menambahkan produk :
    ```html
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" style="color: #A42153;">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Skincare</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form id="form" onsubmit="return false;">
                            {% csrf_token %}
                            <div class="mb-3">
                                <label for="name" class="col-form-label">Brand:</label>
                                <input type="text" class="form-control" id="brand" name="brand"></input>
                            </div>
                            <div class="mb-3">
                                <label for="name" class="col-form-label">Name:</label>
                                <input type="text" class="form-control" id="name" name="name"></input>
                            </div>
                            <div class="mb-3">
                                <label for="name" class="col-form-label">Amount:</label>
                                <input type="number" class="form-control" id="amount" name="amount"></input>
                            </div>
                            <div class="mb-3">
                                <label for="description" class="col-form-label">Description:</label>
                                <textarea class="form-control" id="description" name="description"></textarea>
                            </div>
                            <div class="mb-3">
                                <label for="price" class="col-form-label">Price:</label>
                                <input type="text" class="form-control" id="price" name="price"></input>
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="custom-button" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="custom-button" id="button_add" data-bs-dismiss="modal">Add Product</button>
                    </div>
                </div>
            </div>
        </div>
        

        <div class="container">
            <button class="custom-button" type="button" data-bs-toggle="modal" data-bs-target="#exampleModal">
                Add New Skincare by AJAX
            </button>
        </div>
    ```
- menambahkan potongan kode berikut di blok `<Script>` di bagian bawah kode saya dan menambahkan fungsi baru dengan nama `addProduct()` seperti kode dibawah ini :
    ```html
    <script>
        function addProduct() {
                fetch("/create-ajax/", {
                    method: "POST",
                    body: new FormData(document.querySelector('#form'))
                }).then(response => {
                    if (response.status === 201) {
                        // Jika respons berhasil, ambil pesan notifikasinya
                        return response.text();
                    } else {
                        throw new Error("Failed to add product");
                    }
                })
                .then(notificationMessage => {
                    // Tampilkan pesan notifikasi jika ada
                    if (notificationMessage) {
                        const notificationElement = document.querySelector('.notification');
                        if (notificationElement) {
                            notificationElement.textContent = notificationMessage;
                        }
                    }
                    // Kemudian, perbarui daftar produk
                    refreshProducts();
                })

                document.getElementById("form").reset()
                return false
            }
            document.getElementById("button_add").onclick = addProduct
        
            refreshProducts()
    </script>
    ```

### Melakukan Perintah collectstatic
- di direktori proyek `skincare_list`, buka terminal dan pastikan untuk menyalakan `env` nya dengan menjalankan perintah berikut :
    ```bash
        env\Script\activate.bat
    ```
- jalankan perintah berikut untuk mengumpulkan file statis :
    ```bash
    python manage.py collectstatic
    ```

## Bonus
### Menambahkan fungsionalitas hapus dengan menggunakan AJAX DELETE
1. menambahkan fungsi baru bernama `delete_product_ajax` di file `views.py` yang berada di direktori main dengan beberapa potongan kode berikut :
    ```python
    def delete_product_ajax(request, id):
        product = Product.objects.get(pk= id)
        product.delete()
        return HttpResponseRedirect(reverse('main:show_main'))
    ```
2. tidak lupa import fungsi `delete_product_ajax` di file  `urls.py` dan menambahkan path baru seperti potongan kode berikut :
    ```python
    from main.views import delete_product_ajax

    urlpatterns = [
        ..
        path('delete_product_ajax/<int:id>', delete_product_ajax, name='delete_product_ajax'),
        ..
    ]
    ```
3. menambahkan function baru di blok `<script>` yang ada di file `main.html` dengan potongan kode berikut :
    ```javascript
    async function deleteProduct(id) {
        const response = await fetch(`/delete_product_ajax/${id}`);
        refreshProducts();
    }

    ```
4. yang terakhir tidak lupa untuk mengubah button `delete` sebelumnya seperti potongan kode berikut agar dapat menghapus produk yang didukung dengan AJAX :
    ```html
    <td> 
        <button class = delete-button onclick="deleteProduct(${item.pk})">
            Delete
        </button>
    </td>
    ```

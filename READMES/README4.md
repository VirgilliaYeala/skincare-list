# Tugas 5
## Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
Jawaban:
#### manfaat dari setiap element selector :
1. Memungkinkan kita menerapkan gaya secara universal pada elemen-elemen dengan tag yang sama di seluruh halaman web.
2. Dapat memberikan gaya dasar pada elemen-elemen HTML, seperti mengatur margin, padding, atau tampilan dasar pada proyek kita.
3. Memungkinkan kita mengganti gaya default yang diberikan oleh browser pada elemen-elemen tertentu, seperti hyperlink atau paragraf.

#### kapan waktu yang tepat untuk menggunakannya :
1. Ketika kita ingin mengubah gaya elemen-elemen yang memiliki tag yang sama secara konsisten di seluruh halaman web kita.
2. Ketika kita ingin memberikan tampilan dasar pada elemen-elemen tertentu, seperti judul-judul atau paragraf dalam dokumen HTML kita.
3. Ketika kita ingin mengendalikan tampilan elemen HTML dengan lebih rinci dan mengganti gaya default yang diberikan oleh browser.

##  Jelaskan HTML5 Tag yang kamu ketahui.
Jawaban :
1. `<button>`, berguna untuk membuat tombol interaktif yang dapat digunakan untuk berbagai tindakan, seperti mengirimkan formulir atau menjalankan skrip JavaScript.
2. `<form>`, berguna untuk membuat formulir interaktif yang memungkinkan pengguna mengirimkan data ke server. Berisi elemen-elemen seperti input, textarea, dan tombol kirim.
3. `<section>`, berguna untuk merepresentasikan bagian-bagian terpisah atau blok konten dalam halaman web. Digunakan untuk mengelompokkan konten yang berhubungan.
4. `<nav>`, berguna untuk Menunjukkan bahwa elemen tersebut berisi navigasi atau menu. Biasanya digunakan untuk membuat menu utama atau menu navigasi.
5. `<header>`: Digunakan untuk mendefinisikan bagian atas (header) dari sebuah dokumen atau bagian halaman. Biasanya berisi elemen-elemen seperti judul, logo, dan navigasi.

## Jelaskan perbedaan antara margin dan padding.
Jawaban :
| Margin  | Padding |
| ------------- | ------------- |
| mengosongkan area di sekitar border (transparan) | mengosongkan area di sekitar konten (transparan)  |
| Margin tidak memiliki latar belakang atau warna. Ini hanya berpengaruh pada tata letak elemen.  | Padding dapat memiliki latar belakang atau warna, sehingga memengaruhi tampilan elemen itu sendiri. |
| Ketika dua elemen dengan margin bertemu, margin terbesar di antara keduanya yang akan diterapkan (margin terjauh) | Padding tidak memengaruhi tata letak elemen atau elemen-elemen di sekitarnya.  |
| Margin tidak mempengaruhi ukuran atau konten elemen itu sendiri.  | Padding mempengaruhi ukuran dan tampilan konten elemen  |

## Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Jawaban :
#### perbedaan 
| Bootstrap  | Tailwind |
| ------------- | ------------- |
| Bootstrap menggunakan gaya dan komponen yang telah didefinisikan | membangun tampilan dengan menggabungkan kelas-kelas utilitas yang telah didefinisikan sebelumnya.  |
| memiliki file CSS yang lebih besar  | memiliki file CSS yang lebih kecil |
| menghasilkan tampilan yang lebih konsisten di seluruh proyek | memberikan fleksibilitas dan adaptabilitas tinggi terhadap proyek  |
| memiliki pembelajaran yang lebih cepat untuk pemula  | memiliki pembelajaran yang lebih curam  |

#### Kapan kita menggunakan Bootstrap daripada Tailwind?
1. Jika kita ingin membangun situs web dengan cepat tanpa banyak menulis CSS kustom, Bootstrap bisa menjadi pilihan yang baik.
2. Jika kita ingin membangun situs web yang memiliki tampilan yang seragam atau konsisten tanpa harus menghabiskan banyak waktu mengatur desain.
3. Jika Anda bekerja dalam tim dan perlu kerangka kerja yang umum dikenal dan dipahami oleh banyak pengembang.
4. Jika anda memerlukan responsif pada situs web anda karena bootstrap memiliki bawaan yang mendukung desain responsif, sehingga situs web Anda akan bekerja dengan baik di berbagai perangkat dan layar.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawaban 
### Kustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut
Jawaban : 
di tahap ini saya memutuskan untuk menggunakan CSS dalam pembuatan tugas 5 saya. berikut adalah beberapa kode CSS yang saya tambahkan di tiap file `HTML` saya.
1. Kustomisasi halaman `login.html`
    ```css
    <style>
        body {
            font-family: 'Sora', sans-serif; /* mengatur font untuk halaman login*/
        }

        h1, h5, p {
            text-align: center; /*memastikan posisi teksna itu ada di center*/
        }

        .login { /* mengatur tampilan login ini biar posisi nya ada di tengah*/
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 90vh; 
        }

        .custom-button { /* membuat tampilan button yang menarik*/
            background-color: #EBC2D5; 
            color: #A42153; 
            padding: 10px 20px; 
            margin-top: 10px; 
            margin-bottom: 15px;
            border: none; 
            border-radius: 20px; 
            font-family: 'Sora', sans-serif;
            font-weight: 600;
        }
            
        .custom-button:hover { /* membuat button ketika sebelum di pencet ada efek melayang" nya */
            background-color: #df3c7b;
            color: #EBC2D5;
        }
        
        .form-control { /* ngatur margun nya biar ada jarak*/
            margin-bottom: 15px;
        }
    </style>
    ```
2. Kustomasi halaman `register.html` 
    ```css
    <style>
        body {
            font-family: 'Sora', sans-serif; /* mengatur font untuk halaman register*/
        }

        h1, h5, p {
            text-align: center; /*memastikan posisi teksnya itu ada di center*/
        }

        .login { /* mengatur tampilan register ini biar posisi nya ada di tengah*/
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 90vh; 
        }

        .custom-button { /* membuat tampilan button yang menarik*/
            background-color: #EBC2D5; 
            color: #A42153; 
            padding: 10px 20px; 
            margin-top: 10px; 
            margin-bottom: 15px;
            border: none; 
            border-radius: 20px; 
            font-family: 'Sora', sans-serif;
            font-weight: 600;
        }
            
        .custom-button:hover { /* membuat button ketika sebelum di pencet ada efek melayang" nya */
            background-color: #df3c7b;
            color: #EBC2D5;
        }
    </style>
    ```
3. Kustomasi halaman `create_product.html`
    ```css
        table { /* mengatur tampilan table agar lebih rapih dan tidak berdempetan*/
            border-collapse: separate;
            border-spacing: 10px;
        }

        th, td { /*mengatur padding pada kolon=m dan baris table*/ 
            padding: 10px;
        }
        
        body { /* mengatur font untuk halaman create_product*/
            font-family: 'Sora', sans-serif;
        }

        h1, h5, p { /*memastikan posisi teksnya itu ada di center*/
            text-align: center;
        }
        
        .form-container { /*mengatur posisi table agar selalu di tengah sehingga lebih rapih*/ 
            display: flex;
            justify-content: center; 
            align-items: center; 
        }
        
        .custom-button {  /* membuat tampilan button yang menarik*/
            background-color: #EBC2D5; 
            color: #A42153; 
            padding: 10px 20px; 
            margin-top: 10px; 
            border: none; 
            border-radius: 20px; 
            font-family: 'Sora', sans-serif;
            font-weight: 600;
        }
        
        .custom-button:hover { /* membuat button ketika sebelum di pencet ada efek melayang" nya */
            background-color: #df3c7b; 
            color: #EBC2D5;
        }
    ```

### Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.
Jawaban :
Disini saya masih belom menggunakan card tetapi kemungkinan di tugas berikut nya saya akan ganti menggunakan card
1. Kustomasi halaman `main.html`
    ```css
    <style>
            table { /* mengatur tampilan table agar lebih rapih dan tidak berdempetan*/
                border-collapse: separate;
                border-spacing: 10px;
            }
            th, td { /*mengatur padding pada kolon=m dan baris table*/ 
                padding: 10px;
            }
            
            body { /* mengatur font untuk halaman main*/
                font-family: 'Sora', sans-serif;
            }

            .custom-font { /* mengatur font yang kedua untuk halaman main*/
                font-family: 'Manrope', sans-serif;
                font-weight: 600;
                text-align: center;
                font-size: 15px;
            }

            h1, h5,h3, p { /*memastikan posisi teksnya itu ada di center*/
                text-align: center;
            }
            
            .container { /*mengatur posisi table agar selalu di tengah sehingga lebih rapih*/
                display: flex;
                justify-content: center; 
                align-items: center; 
            }
            
            .notification { /*mengatur design untuk notifikasi yang akan muncul ketika ada produk baru yang ditambahkan*/
                color: #EBC2D5;
                margin-top: 20px; 
                margin-bottom: 20px;
                font-family: 'Manrope', sans-serif; 
                font-weight: 600;
            }
            
            .custom-header { /* mengatur posisi dan design ntuk header yang ada di main*/
                background-color: #EBC2D5; 
                color: #A42153; 
                padding: 10px 20px; 
                margin-top: 20px; 
                border: none; 
                border-radius: 20px; 
                font-family: 'Sora', sans-serif;
                font-weight: 600;
            }

            .custom-button { /* membuat tampilan button yang menarik*/
                background-color: #EBC2D5; 
                color: #A42153; 
                padding: 10px 20px; 
                margin-top: 20px; 
                border: none; 
                border-radius: 20px; 
                font-family: 'Sora', sans-serif;
                font-weight: 600;
            }
            
            .custom-button:hover { /* membuat button ketika sebelum di pencet ada efek melayang" nya */
                background-color: #df3c7b;
                color: #EBC2D5;
            }

            .update-button { /* membuat tampilan button edit product yang menarik*/
                background-color: #EBC2D5; 
                color: #A42153; 
                padding: 10px 20px; 
                border: none; 
                border-radius: 100px; 
                font-family: 'Sora', sans-serif;
                font-weight: 600;
            }

            .update-button:hover { /* membuat button edit product ketika sebelum di pencet ada efek melayang" nya */
                background-color: #df3c7b;
                color: #EBC2D5;
            }

            .delete-button { /* membuat tampilan button delete product yang menarik*/
                background-color: #EBC2D5; 
                color: #A42153; 
                padding: 10px 20px; 
                border: none; 
                border-radius: 100px; 
                font-family: 'Sora', sans-serif;
                font-weight: 400;
            }

            .delete-button:hover { /* membuat button delete product ketika sebelum di pencet ada efek melayang" nya */
                background-color: #df3c7b;
                color: #EBC2D5;
            }
 
            .custom-h4 { /* mengatur font yang kedua untuk halaman main untuk deskripsi penjelasan situs webnya */
                font-family: 'Manrope', sans-serif;
                max-width: 600px;
                text-align: center;
                margin: 0 auto;
                line-height: 1.4; 
            }
        </style>
    ```

## Bonus
### Memberikan warna yang berbeda (teks atau background) pada baris terakhir dari item pada inventori anda menggunakan CSS.
untuk mengimplementasi bonus, saya memberikan warna teks yang berbeda pada baris terakhir di table item inventori saya, berikut potongan kode yang saya tambahkan :
1. style CSS saya 
    ```css
    ...
    .last-row {
        color: #FEE4E0; /* ganti warna font yang lebih terang */
        font-style: italic;/* nge-italic font untuk baris terakhir  */
    }
    ...
    ```
2. menambahkan kondisi tambahan pada iterasi pambacaan pembuatan table nya
    ```html
    {% for product in products %}
    <tr class="{% if forloop.last %}last-row{% endif %}">
        <!-- konten sel lainnya -->
    </tr>
    {% endfor %}
    ```
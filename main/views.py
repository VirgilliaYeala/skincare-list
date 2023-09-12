from django.shortcuts import render

def show_main(request):
    context = {
      'toner' : {
        'brand' : "AVOSKIN -",
        'name' : "Miraculous Retinol Toner",
        'amount' : "3",
        'description' : "mencerahkan dan meratakan tekstur kulit.",
        'price' : "Rp 135.000"
      },
      'moisturizer' : {
        'brand' : "Somethinc -",
        'name' : "Ceramic Skin Saviour",
        'amount' : "5",
        'description' : "menghidrasi dan memperkuat kulit.",
        'price': "Rp 186.000"
      },
      'serum' : {
        'brand' : "AVOSKIN -",
        'name' : "Miraculous Refining Serum",
        'amount' : "11",
        'description' : "mengeksfoliasi dan mencerahkan kulit.",
        'price' : "Rp 110.000"
      },
      'sunscreen' : {
        'brand' : "Somethinc -",
        'name' : "Holyshield!",
        'amount' : "12",
        'description' : "memproteksi kulit dari panas matahari",
        'price' : "Rp 53.900"
      }
    }

    return render(request, "main.html", context)
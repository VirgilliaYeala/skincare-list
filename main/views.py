from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Virgillia Yeala Prabowo',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306165856',
        'name': 'Adinda Maharani Wardhana',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
from django.shortcuts import render, HttpResponse



def home(request):
    context = {
        'title': "Home | Happy Protein",
        'keywords': "Happy Protein, happy protein, protein, plant based products",
        'description': "Company based on plant based products",
    }
    return render(request, "home/home.html", context)
from django.shortcuts import render

def index(request):
    context_dict = {'title': "DentalSoft"}

    return render(request, 'charts/index.html', context_dict)

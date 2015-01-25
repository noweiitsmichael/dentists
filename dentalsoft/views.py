from django.shortcuts import get_object_or_404, render


def index(request):
    context_dict = {'title': "DentalSoft"}

    return render(request, 'login.html', context_dict)
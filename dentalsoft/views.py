from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from charts import views
import datetime
from dateutil.relativedelta import relativedelta
import json


def index(request):
    context = {
        'title': "DentalSoft",
        'error': "",
    }

    context.update(csrf(request));
    print('login')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    print("CHECKED USER")
    
    if user is not None:
        print("valid login")
        auth.login(request, user)
        return render(request, 'charts/index.html', context)
    else :
        print("not valid login")
        if username != "":
            context = {
                'title': "DentalSoft",
                'error': "Invalid Login",
            }
        return render(request, 'login.html', context)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/charts/index.html')
    else:
            context = {
                'title': "DentalSoft ERROR",
            }

            context.update(csrf(request));
            return HttpResponseRedirect('/charts/index.html')

def parse_date_path(path):
    paths = path.split('/')
    index = paths.index('reports') + 1
    out = []
    for x in paths[index:]:
        try:
            out.append(int(x))
        except:
            pass
    return out


def report_year(request):
    year, = parse_date_path(request.path)
    start = datetime.datetime(year, 1, 1)
    end = start + relativedelta(years=1)

    print(start)
    print(end)
    context = {
    }

    return render(request, 'year.html', context)


def report_month(request):
    year, month = parse_date_path(request.path)
    start = datetime.datetime(year, month, 1)
    end = start + relativedelta(months=1)

    print(start)
    print(end)
    context = {
    }
    return render(request, 'month.html', context)


def report_day(request):
    year, month, day = parse_date_path(request.path)
    start = datetime.datetime(year, month, day)
    end = start + relativedelta(days=1)

    print(start)
    print(end)
    context = {
    }
    return render(request, 'day.html', context)


def report_week(request):
    year, month, day = parse_date_path(request.path)
    date = datetime.datetime(year, month, day)
    day_of_week = date.isocalendar()[2]
    start = date + relativedelta(days=-day_of_week)
    end = start + relativedelta(days=7)

    print(start)
    print(end)
    context = {
    }
    return render(request, 'week.html', context)


def get_data(request):
    start = request.GET['start']
    end = request.GET['end']
    data = model.get_data(start, end)
    return HttpResponse(json.dumps(data))

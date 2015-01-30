from django.conf.urls import patterns, include, url
from django.contrib import admin
from dentalsoft import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dentalsoft.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^get_data$', views.get_data, name='get_data'),
    url(r'^reports/\d{4}$', views.report_year, name='year'),
    url(r'^reports/\d{4}/\d{2}$', views.report_month, name='month'),
    url(r'^reports/\d{4}/\d{2}/\d{1,3}$', views.report_day, name='day'),
    url(r'^reports/\d{4}/\d{2}/\d{1,3}/week$', views.report_week, name='week'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^charts/', include('charts.urls')),
)

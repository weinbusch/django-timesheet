from django.conf.urls import url

from django_timesheet.timesheet import views
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView

from django_timesheet.timesheet.models import Task

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='index'),
    url(r'^file/$', views.FileListView.as_view(), name='file_list'),
    url(r'^file/(?P<pk>\d+)/$', views.FileUpdateView.as_view(), name='file'),
    url(r'^file/(?P<pk>\d+)/task/create/$', views.TaskCreateView.as_view(), name='create_task'),
    url(r'^task/(?P<pk>\d+)/$', views.TaskUpdateView.as_view(), name='task'),
    url(r'^task/archive/$', ArchiveIndexView.as_view(model=Task, date_field='date'), name='task_archive'),
    url(r'^task/archive/(?P<year>\d{4})/$', YearArchiveView.as_view(model=Task, date_field='date'), name='task_archive'),
    url(r'^task/archive/(?P<year>\d{4})/(?P<month>\w+)/$', MonthArchiveView.as_view(model=Task, date_field='date'), name='task_archive'),
]
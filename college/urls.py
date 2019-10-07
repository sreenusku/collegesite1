"""
abc
"""
from django.conf.urls import url
from college.views import HomeView
from . import views
app_name = 'college'
urlpatterns = [
    # url(r'^$', views.home, name='home'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^student-application/$', views.student_application, name='student-application'),
    # url(r'^student-application/$', StudentApplicationView.as_view(), name='student-application'),
    url(r'^student-registration/$', views.student_registration, name='student-registration'),
    url(r'^staff-registration/$', views.staff_registration, name='staff-registration'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^/$', views.logout_view, name='logout'),
    url(r'^student_list/(?P<std_reg_id>[0-9]+)/$', views.student_list, name='student-list'),
    url(r'^staff-list/(?P<stf_reg_id>[0-9]+)/$', views.staff_list, name='staff-list'),
    url(r'^student-detail/$', views.student_detail, name='student-detail'),
    url(r'^staff-detail/$', views.staff_detail, name='staff-detail'),
    url(r'^all-staff/$', views.all_staff, name='all-staff'),
    ]

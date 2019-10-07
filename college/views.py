"""
    this is views module for our college app
"""
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


from college.models import StudentApplication, Department, StudentRegistration, StaffRegistration
# Create your views here.


class HomeView(TemplateView):
    """
        here we are writing home view class
    """
    template_name = "college/home.html"
    # def home(request):
    #     """
    #
    #     :param request:
    #     :return:
    #     """
    #     return render(request, 'college/home.html', {})


def student_application(request):
    """

        :param request:
        :return:
        """
    if request.method == "POST":
        StudentApplication.objects.create(
            student_name=request.POST['student-name'],
            email=request.POST['email'],
            dob=request.POST['dob'],
            ssc_doc=request.FILES['ssc-doc'],
            inter_doc=request.FILES['inter-doc'],)
        return HttpResponseRedirect(reverse('college:home'))
    return render(request, 'college/student-application.html', {})


# @login_required
def student_registration(request):
    """

    :param request:
    :return:
    """
    if request.method == "POST":
        # import pdb
        # pdb.set_trace()
        email = request.POST['email']
        print email
        student_app = StudentApplication.objects.get(email=email, is_verified=True)
        print student_app
        user_object = User.objects.create_user(username=request.POST['email'],
                                               first_name=request.POST['first-name'],
                                               last_name=request.POST['last-name'],
                                               email=request.POST['email'],
                                               password=request.POST['password'])
        print user_object
        dept = Department.objects.get(department_name=request.POST['department'])
        print dept
        if student_app.email == user_object.email:
            # import pdb
            # pdb.set_trace()
            StudentRegistration.objects.create(
                application=student_app,
                user=user_object,
                father_name=request.POST['father-name'],
                mother_name=request.POST['mother-name'],
                profile_pic=request.FILES['profile-pic'],
                gender=request.POST['gender'],
                nationality=request.POST['nationality'],
                department=dept)
            return HttpResponseRedirect(reverse('college:home'))
        else:
            return HttpResponse("Access Denied for this page")
    return render(request, 'college/student-registration.html', {})


# @login_required
def staff_registration(request):
    """

    :param request:
    :return:
    """
    if request.method == "POST":
        # import pdb; pdb.set_trace()
        user_object = User.objects.create_user(username=request.POST['email'],
                                               first_name=request.POST['first-name'],
                                               last_name=request.POST['last-name'],
                                               email=request.POST['email'],
                                               password=request.POST['password'])
        dept = Department.objects.get(department_name=request.POST['department'])
        StaffRegistration.objects.create(
            user=user_object,
            gender=request.POST['gender'],
            age=request.POST['age'],
            salary=request.POST['salary'],
            profile_pic=request.FILES['profile-pic'],
            nationality=request.POST['nationality'],
            department=dept)
        return HttpResponseRedirect(reverse('college:home'))
    return render(request, 'college/staff-registration.html', {})


def login_view(request):
    import pdb
    pdb.set_trace()
    """

    :param request:
    :return:
    """
    if request.method == "POST":
        # import pdb
        # pdb.set_trace()
        username = request.POST['email']
        print username
        password = request.POST['password']
        print password
        # s = StudentRegistration.objects.filter(email=username, is_verified=True)
        user = authenticate(request, username=username, password=password)
        print user
        if user is not None:
            login(request, user)
            if hasattr(user, 'studentregistration'):
                return HttpResponseRedirect(reverse('college:student-list', args=(user.id,)))
            elif hasattr(user, 'staffregistration'):
                return HttpResponseRedirect(reverse('college:staff-list', args=(user.id,)))
            # try:
            #     if user.studentregistration.is_student == True:
            #         return HttpResponseRedirect(reverse('college:student-list', args=(user.id,)))
            # except Exception, e:
            #     print "student does not exist"
            # finally:
            #     if user is not None:
            #         login(request, user)
            #         if user.staffregistration.is_staff == True:
            #             return HttpResponseRedirect(reverse('college:staff-list',args=(user.id,)))
        #     if user.studentregistration.is_student==True:
        #         # std_reg_id=StudentRegistration.objects.filter(user.id)
        #         return HttpResponseRedirect(reverse('college:student-list', args=(user.id,)))
        # elif user is not None:
        #     login(request, user)
        #     if user
        #         return HttpResponseRedirect(reverse('college:staff-list', args=(user.id,)))
        else:
            return HttpResponseRedirect(reverse('college:login'))
    return render(request, 'college/login.html', {})


def logout_view(request):
    """

    :param request:
    :return:
    """
    logout(request)
    return HttpResponseRedirect(reverse('college:login', args=()))


@login_required
def student_list(request, std_reg_id):
    """

    :param request:
    :param std_reg_id:
    :return:
    """
    context = User.objects.get(pk=std_reg_id)
    # import pdb
    # pdb.set_trace()
    return render(request, 'college/student-list.html', {'context': context})


@login_required
def staff_list(request, stf_reg_id):
    """

    :param request:
    :param stf_reg_id:
    :return:
    """
    context = User.objects.get(pk=stf_reg_id)
    return render(request, 'college/staff-list.html', {'context': context})


@login_required
def staff_detail(request):
    """

    :param request:
    :return:
    """
    # import pdb
    # pdb.set_trace()
    d = request.user.studentregistration.department
    print d
    staf_list = StaffRegistration.objects.filter(department=d)
    print staf_list
    # for s in staf_list:
    #     print s
    return render(request, 'college/staff-detail.html', {'staf_list': staf_list})


@login_required
def student_detail(request):
    """

    :param request:
    :return:
    """
    b = request.user.staffregistration.department
    std_list = StudentRegistration.objects.filter(department=b)
    return render(request, 'college/student-detail.html', {'std_list': std_list})


@login_required
def all_staff(request):
    """

    :param request:
    :return:
    """
    # import pdb
    # pdb.set_trace()
    stf = StaffRegistration.objects.all()
    return render(request, 'college/all-staff.html', {'stf': stf})

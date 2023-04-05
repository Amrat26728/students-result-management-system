from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from resultmanagementapp.models import FacultyModel, SixResultModel, SevenResultModel, EightResultModel, CoursesModel

# Create your views here.
def home(request):
    faculty = FacultyModel.objects.all()
    data = {
          'faculty': faculty,
          'title': "SRMS | Home",
     }
    return render(request, "index.html", data)

@login_required(login_url='/login')
def result(request):
    data = {
        'title': "SRMS | Result",
    }
    if request.method == "POST":
        username = request.POST.get("username")
        class_name = request.POST.get("class")
        if class_name == "Six":
            results = SixResultModel.objects.all()
            result_check = False
            for result in results:
                if result.username == username:
                    data['username'] = result.username
                    data['name'] = result.name
                    data['eng'] = result.english
                    data['maths'] = result.maths
                    data['science'] = result.science
                    result_check = True
                    break
            if result_check:
                return render(request, "showresult.html", data)
            else:
                return HttpResponse("Result does not found")
        elif class_name == "Seven":
            results = SevenResultModel.objects.all()
            result_check = False
            for result in results:
                if result.username == username:
                    data['username'] = result.username
                    data['name'] = result.name
                    data['eng'] = result.english
                    data['maths'] = result.maths
                    data['science'] = result.science
                    result_check = True
                    break
                else:
                    result_check = False
            if result_check:
                return render(request, "showresult.html", data)
            else:
                return HttpResponse("Result does not found")
        elif class_name == "Eight":
            results = EightResultModel.objects.all()
            result_check = False
            for result in results:
                if result.username == username:
                    data['username'] = result.username
                    data['name'] = result.name
                    data['eng'] = result.english
                    data['maths'] = result.maths
                    data['science'] = result.science
                    result_check = True
                    break
                else:
                    result_check = False
            if result_check:
                return render(request, "showresult.html", data)
            else:
                return HttpResponse("Result does not found")

    return render(request, "result.html")

def courses(request):
    courses = CoursesModel.objects.all()
    data = {
        'title': "SRMS | Courses",
        'courses': courses,
    }
    return render(request, "courses.html", data)

def loginform(request):
    data = {
        'title': "SRMS | Login", 
    }
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        if username and password is not None:
            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return HttpResponse("Something went wrong!")

    return render(request, "login.html", data)

def logout_user(request):
     logout(request)
     return redirect("home")

def  showresult(request):
    data = {
        'title': "SRMS | Show Result", 
    }
    return render(request, "showresult.html", data)
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User

# global my_money
# my_money = 0
# Create your views here.

def main_site(request):
    return render(request, "users/main.html")


def signup_view(request):
    try:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            firstname = request.POST["firstname"]
            lastname = request.POST["lastname"]
            email = request.POST["email"]
            student_id = request.POST["student_id"]
            my_money = request.POST["my_money"]
            user = User.objects.create_user(username, email, password)
            user.last_name = lastname
            user.first_name = firstname
            user.student_id = student_id
            user.my_money = my_money
            user.save()

            return redirect("user:login")
    except:
        return render(request, "users/error.html")

    return render(request, "users/signup.html")

def login_view(request):
    nn =[]
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        use_money = request.POST["use_money"]
        add_money = request.POST["add_money"]
        user = authenticate(username=username, password=password)
        # user_money = User.objects.values('username')
        user_name = User.objects.values_list()
        for i in user_name:
            if username in i:
                nn.append(i)
        for final in nn:
            my_money = int(final[-1])
        if user is not None:
            print("인증성공")
            final_money = str(my_money - int(use_money) + int(add_money))
            user.use_money = use_money
            user.final_money = final_money
            user.my_money = final_money
            user.add_money = add_money
            user.save()
            login(request, user)
        else:
            print("인증실패")
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return redirect("user:login")
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect


# Create your views here.


# home page
def home(request):
    return render(request,"index.html")


from django.shortcuts import render
from django.contrib import messages


def data(request):
    if request.method == 'POST':
        inputDOB = request.POST.get('inputDOB')
        gender = request.POST.get('gender')
        phoneNumber = request.POST.get('PhoneNumber')
        email = request.POST.get('Email')
        address = request.POST.get('Address')
        district = request.POST.get('District')
        account = request.POST.get('Account')

        if not (inputDOB and gender and phoneNumber and email and address and district != "Choose District..." and account != "Choose Account Type..."):
            messages.error(request, 'Please fill in all required fields.')
        else:
            messages.success(request, 'Form submitted successfully.')

    return render(request, 'data.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']

        # Check if fields are empty
        if not username or not password:
            messages.error(request, 'Please fill in both username and password fields.')
            return redirect('/login/#about')

        # Authenticate the user
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('/data/#about')
        else:
            messages.error(request, "We're sorry, but your username or password is not valid. Please try again.")
            return redirect('/login/#about')

    return render(request, "login.html")



#Registeration
def register(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        cpassword = request.POST['password1']

        #checking if data is entered or not
        if not user_name or not password:
            messages.error(request, 'Please fill in all required fields.')
            return redirect('register')

        # Check if the user already exists
        if User.objects.filter(username=user_name).exists():
            messages.error(request, 'User already exists. Please choose a different username.')
            return redirect('register')
        elif password == cpassword:
            user = User.objects.create_user(username=user_name, password=password)
            user.save()
            messages.success(request, 'User Created')
            return redirect('/login/#about')
        else:
            messages.error(request, 'Password and Confirm Password do not match')


    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    messages.success(request, 'You have logged out successfully.')
    return redirect('/')


# ====================================================================






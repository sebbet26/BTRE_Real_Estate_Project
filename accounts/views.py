from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    if request.method == "POST":
        #Login User
        return
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

def register(request):
    if request.method == "POST":
        # Register User
        #messages.error(request, "Testing Error Messages!")
        # Get the data from the form fields
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        # Password match
        if password == password2:
            # Check if username is not taken
            if User.objects.filter(username=username).exists():
                messages.error(request, "That username is taken!")
                return redirect('register')
            else:
                # Check if email is already used
                if User.objects.filter(email=email).exists():
                    messages.error(request, "That email is being used!")
                    return redirect('register')
                else:
                    # Everything looks good
                    newUser = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # Save the new user to the database
                    newUser.save()
                    messages.success(request, "You are now registered and can log in!")
                    return redirect('login')
            
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
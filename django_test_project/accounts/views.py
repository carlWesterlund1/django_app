from asyncio import create_subprocess_exec
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Profile
from .forms import CreateUserProfile


def signup_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            user_profile = Profile() # creates user profile object
            user_profile.user = new_user # sets foreignkey of user profile to the saved user object
            user_profile.save()
            login(request, new_user)  
            return redirect('articles:list')
    else:
        user_form = UserCreationForm()
    return render(request,'accounts/signup.html', {'user_form' : user_form})

def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
          user = form.get_user()
          login(request, user)
          if 'next' in request.POST:
              return redirect(request.POST.get('next'))
          else:
              return redirect('articles:list')
    else:
        form = AuthenticationForm() 
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('articles:list')

@login_required(login_url="/accounts/login/")
def profile_view(request):
        User = get_user_model()
        users = User.objects.all()
        print(users)
        profiles = Profile.objects.all()
        return render(request, 'accounts/profile.html', {'users': users, 'profiles': profiles})

@login_required(login_url="/accounts/login/")
def update_profile_view(request):
    user = request.user
    profile = Profile.objects.get(user_id=user.pk) # gets correct profile based on foreignkey being equal to primary key of user sending request
    if request.method=='POST':
        form = CreateUserProfile(request.POST, instance=profile) # Takes user input data and profile that should be modified and 
        if form.is_valid:
            form.save() # updates profile information
            return redirect('accounts:profile')
    else:
        form = CreateUserProfile(instance=profile)
        return render(request, 'accounts/update_profile.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from . import forms, models


def signup_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = forms.CreateUserProfile(request.POST) # for creating user profile when signing up new user
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            if profile_form.is_valid():
                profile_form.save()    # should save user profile object to database
            return redirect('articles:list')
    else:
        print("else in sign_up")
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
def user_page_view(request):
    #User = get_user_model()
    #users = User.objects.all()
    users = models.UserProfile.objects.all() # retrieves all user profiles
    profile_form = forms.CreateUserProfile   # creates user profile form so that user will be able to update personal information on profile page

    return render(request, 'accounts/user_page.html', {'users': users, 'profile_form': profile_form})

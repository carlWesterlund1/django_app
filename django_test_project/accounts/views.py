from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Profile


def signup_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            user_profile = Profile() # creates user profile object
            user_profile.user = new_user # sets foreignkey of user profile to the created user object
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
def user_page_view(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'accounts/user_page.html', {users: 'users'})

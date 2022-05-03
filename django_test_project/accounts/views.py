from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('articles:list')
    else:
        print("else in sign_up")
        form = UserCreationForm()
    return render(request,'accounts/signup.html', {'form' : form})

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
    # Get data about user to display in user page


    return render(request, 'accounts/user_page.html')

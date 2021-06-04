from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

"""Logout view"""
def logout_view(request):
    logout(request)
    return redirect('auth:login')

def login_view(request):
    error_msn = None
    alert_type = None
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    alert_type = 'alert-success'
                    error_msn = 'Login succesfully'
                    # return redirect('students:path_route_name')
        else:
            alert_type = 'alert-danger'
            error_msn = 'Ups!! something went worong'

    context = {
        'form':form,
        'error_msn':error_msn,
        'alert_type': alert_type,
    }
    return render(request, 'auth/login.html', context)

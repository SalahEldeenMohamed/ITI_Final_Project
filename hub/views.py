from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserRegisterForm,SearchForm
from .models import Doctor

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'hub/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'hub/login.html')

def home(request):
    username = request.user.username if request.user.is_authenticated else 'Guest'
    return render(request, 'hub/home.html', {'username': username})

def home(request):
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            specialization = form.cleaned_data['specialization']
            area = form.cleaned_data['area']
            # Here you would query the doctors matching specialization and area
            doctors = Doctor.objects.filter(specialization=specialization, area=area)
            return render(request, 'hub/search_results.html', {'doctors': doctors})
    return render(request, 'hub/home.html', {'form': form, 'username': request.user.username})

def doctor_details(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    return render(request, 'hub/doctor_details.html', {'doctor': doctor})
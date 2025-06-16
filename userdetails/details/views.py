from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import UserInformationForm
from .models import UserInformation

def home(request):
    if request.method == 'POST':
        form = UserInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserInformationForm()

    submissions = UserInformation.objects.all()
    return render(request, 'details/home.html', {
        'form': form,
        'submissions': submissions,
    })

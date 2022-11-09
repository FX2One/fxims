from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.shortcuts import redirect


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inventory:home')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)

def profile(request):
    return render(request, 'users/profile.html')

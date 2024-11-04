# contact/views.py

from django.shortcuts import render
from .forms import ContactForm
from .models import ContactMessage  # Import the model

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Create a new ContactMessage instance
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            name = form.cleaned_data['name']
            return render(request, 'contact/success.html', {'name': name})
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

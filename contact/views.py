from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('success')  # Redirect to the success page
    else:
        form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form': form})

def success_view(request):
    return render(request, 'contact/success.html')  # Render success page

from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from .models import ModelSiteContents

# Create your views here.
def view_index(request):

    contents = ModelSiteContents.objects.first()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            EmailMessage(
                'Contact Form Submission from {}'.format(name), 
                message,
                'form-response@example.com', # Send from (your website)
                ['test.mailtrap1234@gmail.comm'], # Send to (your admin email)
                [],
                reply_to=[email]
            ).send()
            
            return redirect('success')
    else:
        form = ContactForm()

    return render(request,"index.html",{
        "site_contents": contents,
        "contact_form" : form,
    })

def view_contact_form_success(request):
    return HttpResponse('Success!')
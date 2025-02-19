#main/views.py 

from django.shortcuts import render
from main.forms import ContactUsForm, SearchArticles
from django.core.mail import send_mail
from django.shortcuts import redirect

# Create your views here.
def contact(request):
    #print('Request Method: ', request.method)
    #print('POST data: ', request.POST)

    if request.method == 'POST': 
        # Create instance of form, fill with POST data
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonymous"} via Contact form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['hamestuk.ines@web.de'], 
            )
            return redirect('email-sent')

    else:
        # GET request -> create empty form
        form = ContactUsForm()

    return render(request, 
                  'contact.html',
                  {'form':form})

def search(request):
    #TODO: display all the articles here? 
    form = SearchArticles(request.POST)
    print('in search')
    if form.is_valid():
        
        print(form.cleaned_data)  

    return render(request, 
                  'home.html',
                  {'form':form})
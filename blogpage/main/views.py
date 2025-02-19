#main/views.py 

from django.shortcuts import render
from main.forms import ContactUsForm, SearchArticles, BlogPostForm, SearchForm
from .models import BlogPost, Tags
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


def home_view(request):
    search = SearchForm(request.POST or None)
    blog_post_form = BlogPostForm(request.POST or None)
    blog_posts = BlogPost.objects.all()  # Default: Show all blog posts

    if request.method == "POST":
        if "search_submit" in request.POST:  # If search form is submitted
            if search.is_valid():
                title = search.cleaned_data.get("title")
                tags = search.cleaned_data.get("tags")

                if title:
                    blog_posts = blog_posts.filter(title__icontains=title)

                if tags:
                    tag_names = [tags.strip() for tags in tags.split(",") if tags.strip()]
                    blog_posts = blog_posts.filter(tags__text__in=tag_names).distinct()

        elif "blog_post_submit" in request.POST:  # If blog post form is submitted
            if blog_post_form.is_valid():
                blog_post_form.save()
                return redirect("home")  # Redirect to avoid duplicate submissions

    return render(request, "home.html", {
        "search": search,
        "blog_post_form": blog_post_form,
        "blog_posts": blog_posts,
    })
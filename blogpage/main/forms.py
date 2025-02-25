# main/forms.py

from django import forms
from .models import BlogPost, Tags

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=2000)

class SearchArticles(forms.Form):
    title = forms.CharField(required=False)
    publish_date = forms.DateField(required=False)

class BlogPostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas"
    )
    class Meta: 
        model = BlogPost 
        fields = ["title", "content", "tags"]

    def save(self, commit=True):
        blog_post = super().save(commit=False) 
        if commit: 
            blog_post.save()
            tag_names = self.cleaned_data["tags"].split(",")
            for tag_name in tag_names:
                tag_name = tag_name.strip()
                if tag_name:
                    tag, created = Tags.objects.get_or_create(text=tag_name)
                    blog_post.tags.add(tag)
        return blog_post
    
class SearchForm(forms.Form):
    title = forms.CharField(required=False, max_length=255)
    tags = forms.CharField(required=False, help_text="Search by tags (comma-separated)")

from django.forms import ModelForm

from BlogPosts.models import Blog


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'content', 'cover')

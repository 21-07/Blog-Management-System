from django import forms
from blogapp.models import Blogs

class CreateBlog(forms.ModelForm):
    class Meta:
        model=Blogs
        exclude=('user',)


class UpdateBlog(forms.ModelForm):
    class Meta:
        model=Blogs
        exclude=('user',)

from django import forms
from .models import User,Article,Comment
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
        }
class EditPostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={'class':'form-control'}),
        }
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
        }

from django import forms
from .models import User, Message
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),

        }
class  MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter your message','rows':'3'}),

        }
class MessageEditForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter your message','rows':'3'}),
        }
class MessageReturnForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
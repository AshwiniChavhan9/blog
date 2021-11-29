from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModeForm):

    class Meta():
        model=Post
        field=('autor', 'title','text')

        widgets={
        'title':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model=Comment
        field=('autor','text')

        widgets={
        'author':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})

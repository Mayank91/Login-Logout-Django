from django import forms
from models import Articles

#start of form

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title','body', 'pub_date']
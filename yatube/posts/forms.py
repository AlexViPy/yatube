from django.forms import ModelForm, Textarea
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['group', 'text']
        labels = {
            'group': 'Группа',
            'text': 'Поле для Вашего текста'
        }
        widgets = {
            'text': Textarea(attrs={'cols': 60, 'rows': 20}),
        }
    


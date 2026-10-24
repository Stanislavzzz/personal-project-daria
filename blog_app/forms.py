from django import forms

from blog_app.models import Post


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=200,
        label='Заголовок',
        widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Введите заголовок'})

    )
    content = forms.CharField(
        label="Содержание",
        widget=forms.Textarea(attrs={'class': 'form-control', 'row': 5, 'placeholder': 'Введите содержание'})
    )
    rating = forms.IntegerField(
        min_value=0,
        max_value=100,
        label="Рейтинг",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'rating', 'author', 'tags')
        labels = {
            'title': "Заголовок",
            'content': "Содержание",
            'rating': "Рейтинг",
            'author': "Автор",
            'tags': "Тэги"
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control' , 'placeholder': 'Введите заголовок'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'row': 5, 'placeholder': 'Введите содержание'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

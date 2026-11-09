from django import forms
from django.core.exceptions import ValidationError

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

    def clean_rating(self):
        """Валидация рейтинга."""
        rating = self.cleaned_data.get('rating')
        if rating > 10:
            raise forms.ValidationError("Рейтинг не может быть больше 10")
        return rating

    def clean_title(self):
        """Валидация заголовка."""
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Заголовок не может быть меньше 5 симолов")
        return title

    def clean(self):
        """Общая валидация формы."""
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        title = cleaned_data.get('title')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        if content and title:
            for word in forbidden_words:
                if word in content or word in title:
                    raise forms.ValidationError("Запрещенное слово в тексте или заголовке")


class PostDeleteForm(forms.Form):
    """Форма для удаления поста."""
    confirm = forms.BooleanField(
        label='Подтвердите удаление',
        required=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )


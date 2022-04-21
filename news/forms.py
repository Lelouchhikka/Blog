from django import forms
from news.models import News


class NewsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['author'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['tag'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'

        self.fields['title'].widget.attrs['placeholder'] = 'Название'
        self.fields['description'].widget.attrs['placeholder'] = 'Описание'

    class Meta:
        model = News 
        fields = '__all__'


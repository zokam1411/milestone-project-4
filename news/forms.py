from django import forms
from .models import News


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'
        exclude = ('author',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['introduction'].widget.attrs['placeholder'] = (
            'This will be visible as a first paragraph'
        )
        self.fields['introduction'].widget.attrs['rows'] = 4

        self.fields['content'].widget.attrs['placeholder'] = (
            'You can use HTML tags to format text'
        )

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'

from django import forms
from .models import News, Comment


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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['comment_text'].widget.attrs['placeholder'] = 'Add a comment...'
        self.fields['comment_text'].widget.attrs['rows'] = 4

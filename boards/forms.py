from django import forms
from .models import Topic, Post

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': '请简要介绍一下素材主题'}
        ), 
        max_length=4000,
        help_text='最大长度为 4000 字',
        label='简介'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']
        labels = {'subject': '主题'}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]
        labels = {'message': '内容'}

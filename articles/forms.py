from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    # title = forms.CharField(
    #     label='제목입니다.',
    #     widget=forms.TextInput(
    #         attrs={'class': 'form-control'}
    #     )
    # )

    class Meta:
        model = Article
        # fields = '__all__'
        # fields = ('title', 'content',)
        exclude = ('user', )
        # 코드를 커스터마이징 하고 싶을 때 사용
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control'}),
        # }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        fields = ('content', )
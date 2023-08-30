from django import forms
from pybo.models import Question,Answer,Comment

# modelform은 모델의 데이터를 저장할 수 있는 폼
# 장고 모델 폼은 inner class인 Meta가 필수
# 이 같은 클래스가 장고폼

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields=['content']
        labels={
            'content':'답변내용'
            ,
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields=['content']
        labels={
            'content':'댓글내용'
        }

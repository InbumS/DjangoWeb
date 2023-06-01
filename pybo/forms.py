from django import forms
from pybo.models import Question,Answer

# modelform은 모델의 데이터를 저장할 수 있는 폼
# 모델 폼은 inner class인 Meta가 필수
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
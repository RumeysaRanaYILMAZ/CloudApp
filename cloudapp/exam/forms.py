from django import forms


class QuestionForm(forms.Form):
    question = forms.CharField(label='question', max_length=1000)
    ans_1 = forms.CharField(label='ans_1', max_length=400)
    ans_2 = forms.CharField(label='ans_2', max_length=400)
    ans_3 = forms.CharField(label='ans_3', max_length=400)
    ans_4 = forms.CharField(label='ans_4', max_length=400)
from django import forms

class WordForm(forms.Form):
    word = forms.CharField(label= False, max_length=50,
                           widget=forms.TextInput(attrs={"id": "answer", "placeholder": "Answer", "autofocus": "True"}))
    correct_word = forms.CharField(label=False, max_length=50, 
                                   widget=forms.TextInput(attrs={"id": "correct_answer"}))
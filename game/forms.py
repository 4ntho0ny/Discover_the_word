from django import forms

class WordForm(forms.Form):
    word = forms.CharField(label= False, initial="Answer", max_length=50, widget=forms.TextInput(attrs={"id": "answer"}))
    correct_word = forms.CharField(label=False, max_length=50, widget=forms.TextInput(attrs={"id": "correct_answer"}))
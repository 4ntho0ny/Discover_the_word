from django.shortcuts import redirect, render
import random
import requests
from .forms import WordForm

# Get word list
def get_word_list():
    url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'
    response = requests.get(url)
    words = response.json()
    return words

# Draw word
def random_word():
    list_objects = get_word_list()
    return random.choice(list_objects)

# PAGES OF GAME

def starting_page(request):
    return render(request, "game/starting_page.html")

def validate_answer(form):
    if form.is_valid():
        word = form.cleaned_data["word"].lower().strip()
        correct_answer = form.cleaned_data["correct_word"].lower()
    
        if word == correct_answer:
            return True
        else:
            return False

def play_page(request):
    hint = ""
    correct_word = ""
    context = {}
    wrong_answer = False
    
    # GET METHOD
    if request.method == "GET":
        # RANDOM OBJECT OF API FOR GAME
        obj = random_word()
        hint = obj['dica']
        correct_word = obj['palavra']
        # CREATE A FORM
        form = WordForm(initial={
            "correct_word": correct_word,
            "hint": hint
        })
        
        context["hint"] = hint
        context["form"] = form

    # POST METHOD
    elif request.method == "POST":
        form = WordForm(request.POST)
        response = validate_answer(form)
        
        if not response:
            hint = form.cleaned_data["hint"]
            correct_word = form.cleaned_data["correct_word"]
            form = WordForm(initial={
                "correct_word": correct_word,
                "hint": hint
            })
            context["hint"] = hint
            context["form"] = form
            context["wrong_answer"] = True
        else:
            return redirect("winner_page")
        
    return render(request, "game/game_page.html", context)

def result_page(request):
    return render(request, "game/winner_page.html")
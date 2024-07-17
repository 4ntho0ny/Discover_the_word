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

def play_page(request):
    # RANDOM WORD FOR GAME
    obj = random_word()
    hint_text = obj['dica']
    word_lenght = len(obj['palavra'])
    correct_word = obj['palavra'].upper()
    
    # GET METHOD
    if request.method == "GET":
        print("Entrou no get")
        form = WordForm(initial={
            "correct_word": correct_word
        })
        
        context = {
            "hint": hint_text,
            "word_lenght": word_lenght,
            "form": form
        }
        
        return render(request, "game/game_page.html", context)

def validate_answer(request):
    # POST METHOD
    if request.method == "POST":
        
        form = WordForm(request.POST)
        
        if form.is_valid():
            
            word = form.cleaned_data["word"].upper()
            correct_answer = form.cleaned_data["correct_word"].upper()

            if word == correct_answer:
                # print("Correct answer")
                return redirect("winner_page")
            else:
                # print("Wrong answer")
                return redirect("play_page")

def result_page(request):
    return render(request, "game/winner_page.html")
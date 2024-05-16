from django.shortcuts import render
import random
import requests

def get_word_list():
    url = 'https://raw.githubusercontent.com/guilhermeonrails/api-imersao-ia/main/words.json'
    response = requests.get(url)
    words = response.json()
    return words

def starting_page(request):
    return render(request, "game/starting_page.html")

def play_page(request):
    list_objects = get_word_list()
    obj = random.choice(list_objects)
    hint_text = obj['dica']
    word_lenght = len(obj['palavra'])
    
    return render(request, "game/game_page.html", {
        "hint": hint_text,
        "word_lenght": word_lenght
    })

def result_page(request):
    pass

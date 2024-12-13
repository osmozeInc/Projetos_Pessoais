import pyttsx3
import datetime
import requests


spk = pyttsx3.init()


def Falar(texto):
    spk.say(texto)
    spk.runAndWait()

def dia_de_hoje():
    dia = datetime.datetime.now().strftime("%d/%m/%Y")
    Falar(f"Hoje é dia {dia}")

def contar_piada():
    # URL da JokeAPI (piada aleatória)
    url = 'https://v2.jokeapi.dev/joke/Any?lang=pt'
    
    response = requests.get(url)
    joke = response.json()

    if joke['type'] == 'single':
        Falar(joke['joke'])
    elif joke['type'] == 'twopart':
        Falar(joke['setup'])
        Falar(joke['delivery'])
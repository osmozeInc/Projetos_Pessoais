import speech_recognition as sr
from funcoes_assistentes import *

recognizer = sr.Recognizer()


def Ouvir():
    with sr.Microphone() as source:
        print("Fale\n")
        audio = recognizer.listen(source)

    try:
        texto = recognizer.recognize_google(audio, language='pt-BR')
    except sr.UnknownValueError:
        texto ="não entendi. Repita, por favor."
    except sr.RequestError:
        Falar("Erro ao acessar o serviço de reconhecimento.")
        return "3rr0"

    return texto.lower()
    

def Reconhecer(texto):
    if texto == "não entendi. Repita, por favor.":
        Falar(texto)
    elif texto == "3rr0":
        return 1
    elif texto == "vai dormir" or texto == "não quero nada hoje" or texto == "desliga":
        Falar("ok, até logo!")
        return 1
    
    elif texto == "que dia é hoje" or texto == "qual dia de hoje" or texto == "qual a data de hoje" or texto == "hoje é quando":
        dia_de_hoje()

    elif texto == "conte uma piada" or texto == "outra piada" or texto == "conte uma piada engraçada":
        contar_piada()
    
    return 0


Falar("Pois não?")
while (True):

    texto = Ouvir()
    parada = Reconhecer(texto)

    if parada == 1:
        break

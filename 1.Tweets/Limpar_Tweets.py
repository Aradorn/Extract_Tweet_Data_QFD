import pandas as pd

extracao = pd.read_csv('Saraiva.csv')

lista_respostas = pd.DataFrame(extracao,columns=["Tweet_Text"])
lista_perguntas = extracao["Reply Message"]


frases = lista_perguntas.str.lower()

print(frases[0])



import pandas as pd
from collections import Counter
import numpy as np
from sklearn.model_selection import cross_val_score
import nltk
#nltk.download('stopwords')
#nltk.download('rslp')
#nltk.download('punkt')
from unicodedata import normalize

from remover import *


classificacoes = pd.read_csv('Tweets_Livrarias.csv')
textosPuros = classificacoes['Reply Message']
textosPuros = classificacoes['Reply Message']
textosPuros.dropna(inplace=True)
#-----------------------------

#textosQuebrados = textosPuros.str.lower().str.split(' ')
#dicionario = set()
#for lista in textosQuebrados:
#    dicionario.update(lista)

#--------------------------------

frases = textosPuros.str.lower()
textosQuebrados = [nltk.tokenize.word_tokenize(frase) for frase in frases]

#normalize('NFKD', textosQuebrados).encode('ASCII', 'ignore').decode('ASCII')

frase = textosQuebrados[10]

for palavra in frase:
    print(palavra)




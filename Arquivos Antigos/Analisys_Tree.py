import pandas as pd
from collections import Counter
import numpy as np
from sklearn.model_selection import cross_val_score
import nltk
#nltk.download('stopwords')
#nltk.download('rslp')
#nltk.download('punkt')


classificacoes = pd.read_csv('Tweets_Livrarias.csv')
textosPuros = classificacoes['Reply_Message']
textosPuros = classificacoes['Reply_Message']
textosPuros.dropna(inplace=True)
#-----------------------------

#textosQuebrados = textosPuros.str.lower().str.split(' ')
#dicionario = set()
#for lista in textosQuebrados:
#    dicionario.update(lista)

#--------------------------------

frases = textosPuros.str.lower()
textosQuebrados = [nltk.tokenize.word_tokenize(frase) for frase in frases]

stemmer = nltk.stem.RSLPStemmer()
stopword = nltk.corpus.stopwords.words('portuguese')
dicionario = set()
for lista in textosQuebrados:
    palavrasValidas = [stemmer.stem(palavra) for palavra in lista if palavra not in stopword and len(palavra) > 3]
    dicionario.update(palavrasValidas)


totalDePalavras = len(dicionario)
tuplas = zip(dicionario, range(totalDePalavras))

tradutor = {palavra:indice for palavra,indice in tuplas}

def vetorizar_texto(texto, vetor):
    vetor = [0] * len(tradutor)
    for texto in textosQuebrados:
        for palavra in texto:
            if len(palavra) > 0 and stemmer.stem(palavra) in tradutor:
                posicao = tradutor[palavra]
                vetor[posicao] += 1
    return vetor

vetoresDeTexto = [vetorizar_texto(textosQuebrados, tradutor)for texto in textosQuebrados]

tradutor_indice = {indice:palavra for palavra,indice in tuplas}

vetor_ordenado = sorted(vetoresDeTexto,reverse=True)

print(tradutor_indice[1])
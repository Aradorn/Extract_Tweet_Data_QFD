import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('rslp')

#--------Importar Dados----------
extracao = pd.read_csv('MideaBrasil.csv')
lista_respostas = pd.DataFrame(extracao,columns=["Tweet_Text"])
lista_perguntas = extracao["Reply Message"]

#--------Tratamento de Textos----------

frases = lista_perguntas.str.lower()
frases = [nltk.tokenize.word_tokenize(frase) for frase in frases if frase is str(frase)!='nan']
stemmer = nltk.stem.RSLPStemmer()
stopword = nltk.corpus.stopwords.words('portuguese')
dicionario = set()

for frase in frases:
    palavrasValidas = [stemmer.stem(palavra) for palavra in frase if palavra not in stopword and len(palavra) > 4]
    dicionario.update(palavrasValidas)

totalDePalavras = len(dicionario)
tuplas = zip(dicionario, range(totalDePalavras))
tradutor = {palavra:indice for palavra,indice in tuplas}

def vetorizar_texto(texto, vetor):
    vetor = [0] * len(tradutor)
    for palavra in texto:
        if len(palavra) > 0 and stemmer.stem(palavra) in tradutor:
            posicao = tradutor[stemmer.stem(palavra)]
            vetor[posicao] += 1
    return vetor

vetoresDeTexto = [vetorizar_texto(frase, tradutor) for frase in frases]


#--------Machine Learning----------

#from sklearn.model_selection import train_test_split
#X_treinamento, X_teste= train_test_split(vetoresDeTexto, test_size = 0.3, random_state = 0)

from sklearn.cluster import KMeans

cluster = KMeans(n_clusters = 4)
cluster.fit(vetoresDeTexto)

centroides = cluster.cluster_centers_
previsoes = cluster.labels_

resultado = {'Perguntas':frases,'Respostas':previsoes}
resultado = pd.DataFrame(resultado)

resultado.to_csv("resultado2.csv",sep=';')


lista_palavras = []

for frase in frases:
	for palavra in frase:
		if palavra not in stopword and len(palavra) > 4:
			lista_palavras.append(palavra)

lista_palavras = str(lista_palavras)

from wordcloud import WordCloud
import matplotlib.pyplot as plt
wordcloud = WordCloud(max_font_size=100,width = 1520, height = 535).generate(lista_palavras)
plt.figure(figsize=(16,9))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
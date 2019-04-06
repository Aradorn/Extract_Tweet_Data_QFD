import pandas as pd
import nltk
#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('rslp')

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
    palavrasValidas = [palavra for palavra in frase if palavra not in stopword and len(palavra) > 4]
    dicionario.update(palavrasValidas)

totalDePalavras = len(dicionario)
tuplas = zip(dicionario, range(totalDePalavras))
tradutor = {palavra:indice for palavra,indice in tuplas}

def vetorizar_texto(texto, vetor):
    vetor = [0] * len(tradutor)
    for palavra in texto:
        if len(palavra) > 0 and palavra in tradutor:
            posicao = tradutor[palavra]
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

from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster import cluster_visualizer

#cluster = kmedoids(vetoresDeTexto,[3,12,30])
#cluster.get_medoids()
#cluster.process()
#previsoes = cluster.get_clusters()
#medoides = cluster.get_medoids()
#v = cluster_visualizer()
#v.append_clusters(previsoes, vetoresDeTexto)
#v.append_cluster(medoides, data = vetoresDeTexto, marker = '*', markersize = 15)
#v.show()



resultado = {'Perguntas':frases,'Respostas':previsoes}
resultado = pd.DataFrame(resultado)
resultado.to_csv("resultado2.csv",sep=';')

#--------filtrar resultados-----------
res_zero = resultado[(resultado['Respostas']==0)]
res_um = resultado[(resultado['Respostas']==1)]
res_dois = resultado[(resultado['Respostas']==2)]
res_tres = resultado[(resultado['Respostas']==3)]


#--------Resumir Plavras-----------

def criar_lista(frases,nome):
    lista_palavras = []
    for frase in frases:
        for palavra in frase:
            if palavra not in stopword and len(palavra) > 4 and palavra != 'mideacarrier' and palavra != 'mideabrasil':
                lista_palavras.append(palavra)
    lista_palavras = pd.DataFrame(lista_palavras)
    lista_palavras.to_csv("%s.csv"%nome,sep=";")

#-------------------

criar_lista(res_zero["Perguntas"],"zero")
criar_lista(res_um["Perguntas"],"um")
criar_lista(res_dois["Perguntas"],"dois")
criar_lista(res_tres["Perguntas"],"tres")



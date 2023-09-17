import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('rslp')

class Tratamento:

    def __init__(self, dados):
        self.dados = dados

    # Cria um dataframe
    def criar_dataframe(self):
        dt = pd.DataFrame({'coluna_de_dados': [self.dados]}, index=[0])
        return dt  # Adicione um retorno para o DataFrame

    # Tokeniza por letras
    def tokeniza_por_letras(self):
        tokenizado = nltk.word_tokenize(self.dados)
        return tokenizado  # Adicione um retorno para a lista tokenizada

    # Tokeniza por frases
    def tokeniza_por_sentenca(self):
        token_sentenca = nltk.sent_tokenize(self.dados)
        return token_sentenca  # Adicione um retorno para as sentenças tokenizadas

    # Deixa minusculo
    def minuscula(self):
        mini = str.lower(self.dados)
        return mini  # Adicione um retorno para o texto em minúsculas

    # Retona somente palavras relevantes
    def remover_palavras_comum(self):
        lista_brasileira = stopwords.words('portuguese')
        texto_sem_stopwords = [palavra for palavra in nltk.word_tokenize(self.dados) if palavra.lower() not in lista_brasileira]
        return texto_sem_stopwords  # Adicione um retorno para o texto sem stopwords

    # Executado após remover_palavra_comum(), stemming.
    def stemizar(self):
        stemmer = RSLPStemmer()
        stemizado = [stemmer.stem(palavra) for palavra in nltk.word_tokenize(self.dados, language='portuguese')]
        return stemizado  # Adicione um retorno para as palavras stemizadas

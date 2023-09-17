import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer


nltk.download('punkt')
nltk.download('stopwords')
nltk.download("rslp")

class Tratamento:

    def __init__(self, dados):
        self.dados = dados

    def criar_dataframe(self):
        dt = pd.DataFrame({'coluna_de_dados': [self.dados]}, index=[0])
        return dt

    def tokeniza_por_letras(self):
        tokenizado = nltk.word_tokenize(self.dados)
        return tokenizado

    def tokeniza_por_sentenca(self):
        token_sentenca = nltk.sent_tokenize(self.dados)
        return token_sentenca

    def minuscula(self):
        mini = str.lower(self.dados)
        return mini

    def remover_palavras_comum(self):
        remove = stopwords.words('portuguese')
        texto_sem_stopwords = [palavra for palavra in nltk.word_tokenize(self.dados) if palavra.lower() not in remove]
        return texto_sem_stopwords

    def stemizar(self):
        stemmer = RSLPStemmer()
        stemizado = [stemmer.stem(palavra) for palavra in nltk.word_tokenize(self.dados, language='portuguese')]
        return stemizado
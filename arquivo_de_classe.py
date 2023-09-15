import pandas as pd
import nltk

class Tratamento:

    def __init__(self, dados):
        self.dados = dados

    def criar_dataframe(self):
        # Criando um DataFrame com um índice explícito
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


# Solicita ao usuário um texto de entrada
texto = input('Digite um texto: ')

# Chama a função de tratamento com o texto inserido pelo usuário
usuario = Tratamento(texto)
#x = usuario.criar_dataframe()
#y = usuario.tokeniza_por_letras()
#z = usuario.tokeniza_por_sentenca()
letras_mini = usuario.minuscula()


# Exibe o DataFrame resultante
print(letras_mini)

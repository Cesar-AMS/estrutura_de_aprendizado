from textblob import TextBlob
from googletrans import Translator

class AnalisadorDiario:

    def __init__(self, texto):
        self.texto = texto

    def analisar_sentimento(self):
        # Criar um objeto TextBlob
        blob = TextBlob(self.texto)

        # Analisar o sentimento
        sentimento = blob.sentiment

        # Determinar se o sentimento é positivo, negativo ou neutro
        if sentimento.polarity > 0:
            sentimento_str = "Positivo"
        elif sentimento.polarity < 0:
            sentimento_str = "Negativo"
        else:
            sentimento_str = "Neutro"

        return {
            "sentimento": sentimento_str,
            "polaridade": sentimento.polarity
        }

    def extrair_entidades(self):
        # Criar um objeto TextBlob
        blob = TextBlob(self.texto)

        # Extrair entidades nomeadas
        entidades = blob.noun_phrases

        return {
            "entidades": entidades
        }

    def traduzir_texto(self):

        # traduz o texto
        tradutor = Translator(self.texto)
        traducao = tradutor.translate(self, src='auto', dest='en')
        return traducao


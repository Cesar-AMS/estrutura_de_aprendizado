from textblob import TextBlob

class AnalisadorSentimento:

    def __init__(self, texto):
        self.texto = texto

    def analisar_sentimento(self):
        # Criar um objeto TextBlob
        blob = TextBlob(self.texto)

        # Analisar o sentimento
        sentimento = blob.sentiment

        # Determinar se o sentimento é positivo, negativo ou neutro
        if sentimento.polarity > 0:
            return "Positivo"
        elif sentimento.polarity < 0:
            return "Negativo"
        else:
            return "Neutro"



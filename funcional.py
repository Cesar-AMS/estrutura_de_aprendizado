import nltk
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
from nltk.stem import WordNetLemmatizer
from modelos import AnalisadorSentimento

def preprocess_text(text):
    # Transforma cada letra em um token
    tokenizada = nltk.word_tokenize(text)

    # Remove palavras comuns
    palavras_brasileira = stopwords.words('portuguese')
    palavras_relevantes = [palavra for palavra in tokenizada if palavra.lower() not in palavras_brasileira]

    # Stemming
    stemmer = RSLPStemmer()
    stemizador = [stemmer.stem(palavra) for palavra in palavras_relevantes]

    # Lemmatização
    lemma = WordNetLemmatizer()
    lemmatizado = [lemma.lemmatize(palavra) for palavra in stemizador]

    # Combine todas as transformações em um único texto tratado
    texto_tratado = ' '.join(lemmatizado)

    return texto_tratado

def main():
    # Inseri texto
    texto = input('Digite um texto: ')

    # Pré-processa o texto
    texto_tratado = preprocess_text(texto)

    # Realiza a análise de sentimento
    analise_sentimental = AnalisadorSentimento(texto_tratado)
    resultado = analise_sentimental.analisar_sentimento()
    # Imprime o resultado da análise de sentimento
    print(f"Resultado da análise de sentimento: {resultado}")

if __name__ == "__main__":
    main()

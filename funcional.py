import nltk
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
from nltk.stem import WordNetLemmatizer

def preproces_de_texto(text):
    # Transforma cada letra em um token
    tokenizada = nltk.word_tokenize(text)

    # Remove palavras comuns
    palavras_brasileira = stopwords.words('portuguese')
    palavras_relevantes = [palavra for palavra in tokenizada if palavra.lower() not in palavras_brasileira]

    # Stemming
    stemmer = RSLPStemmer()
    stemizado = [stemmer.stem(palavra) for palavra in palavras_relevantes]

    # Lemmatização
    lemma = WordNetLemmatizer()
    lemmatizado = [lemma.lemmatize(palavra) for palavra in stemizado]

    # Combine todas as transformações em um único texto tratado
    texto_tratado = ' '.join(lemmatizado)

    return texto_tratado

def main():
    # Inseri texto
    texto = input('Digite um texto: ')

    # Pré-processa o texto
    texto_tratado = preproces_de_texto(texto)

    # Imprimir o resultado final
    print(f"Texto tratado: {texto_tratado}")

if __name__ == "__main__":
    main()

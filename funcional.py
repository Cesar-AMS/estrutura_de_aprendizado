import nltk
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

def preprocess_text(text):
    # Transforma cada letra em um token
    tokenizada = nltk.word_tokenize(text)

    # Remove palavras comuns
    letras_brasileira = stopwords.words('portuguese')
    letras_base = [palavra for palavra in tokenizada if palavra.lower() not in letras_brasileira]

    # Stemming
    stemmer = RSLPStemmer()
    stemizador = [stemmer.stem(palavra) for palavra in letras_base]

    # Combine todas as transformações em um único texto tratado
    texto_tratado = ' '.join(stemizador)

    return texto_tratado

def main():
    # Inseri texto
    texto = input('Digite um texto: ')

    # Pré-processa o texto
    texto_tratado = preprocess_text(texto)

    # Imprimir o resultado final
    print(f"Texto tratado: {texto_tratado}")

if __name__ == "__main__":
    main()

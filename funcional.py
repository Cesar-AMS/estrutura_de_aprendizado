import nltk
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

def preprocess_text(text):
    # Transforma cada letra em um token
    tokenizacao = nltk.word_tokenize(text)

    # Remove palavras comuns
    lista_brasileiro = stopwords.words('portuguese')
    remove_letras = [palavra for palavra in tokenizacao if palavra.lower() not in lista_brasileiro]

    # Stemming
    stemmer = RSLPStemmer()
    stemizador = [stemmer.stem(palavra) for palavra in remove_letras]

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

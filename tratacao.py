import nltk
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
from nltk.stem import WordNetLemmatizer

def pre_pro_texto(text):
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

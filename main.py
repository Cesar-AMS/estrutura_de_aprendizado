from funcional import pre_pro_texto
from modelos import AnalisadorSentimento

def main():
    # Inseri texto
    texto = input('Digite um texto: ')

    # Pré-processa o texto
    texto_tratado = pre_pro_texto(texto)

    # Realiza a análise de sentimento
    analise_sentimental = AnalisadorSentimento(texto_tratado)
    resultado = analise_sentimental.analisar_sentimento()

    # Imprime o resultado da análise de sentimento
    print(f"Resultado da análise de sentimento: {resultado}")

if __name__ == "__main__":
    main()

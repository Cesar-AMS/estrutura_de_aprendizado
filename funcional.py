from tratamento import Tratamento



def main():

    texto = input('Digite: ')

    tratamento = Tratamento(texto)
    tokenizacao = tratamento.tokeniza_por_letras()
    mini = tratamento.minuscula()
    remove_letras = tratamento.remover_palavras_comum()
    stemizador = tratamento.stemizar()
    dt = tratamento.criar_dataframe()
    resultado = tokenizacao, mini, remove_letras, stemizador, dt
    return resultado

if __name__ == "__main__":
    main()
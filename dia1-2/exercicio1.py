def nome_invertido(nome):
    for index_letra in range(len(nome)):
        for index in range(len(nome) - index_letra):
            print (nome[index], end="")
        print()

if __name__ == "__main__":
    name = input("Digite um nome: ")
    nome_invertido(name)
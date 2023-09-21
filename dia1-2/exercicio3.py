import random

PALAVRAS = [
    "Antonio", 
    "Tunico", 
    "Tonhão"
    ]

COUNT = 3

def retrieve_words(file):
    return [word.strip() for word in file]

def embaralhar_palavras(palavras):
    palavra_escolhida = random.choice(palavras)
    palavra_embaralhada = "".join(random.sample(palavra_escolhida, len(palavra_escolhida)))
    return palavra_escolhida, palavra_embaralhada

def tentativas():
    chances = []
    for index in range(COUNT):
        chance = input("Adivihe a palavra: ")
        chances.append(chance)
    return chances
    

def checar_game(palavra_secreta, chances):
    if palavra_secreta in chances:
        print(f"Você venceu: {palavra_secreta}")
    else:
        print(f"Você perdeu: {palavra_secreta}")
    
   

if __name__ == "__main__":
    with open("words.txt") as file:
        words = retrieve_words(file)
    palavra_escolhida, palavra_embaralhada = embaralhar_palavras(file)
    print(f"A palavra embalharada é: {palavra_embaralhada}")
    chances = tentativas()
    checar_game(palavra_escolhida, chances)
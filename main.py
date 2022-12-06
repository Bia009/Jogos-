
import random


def jogar():

    imprime_abertura()
    palavra_secreta = gerar_palavra_secreta()

    letras_acertadas = inic_letras_acertada(palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0


    while not enforcou and not acertou :

        chute = chutar()

        if chute in palavra_secreta:
            i = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[i] = letra
                i += 1
        else:
            erros += 1
            print(f'__ERROS {erros}__')
            if erros == 6:
                print(" _____\n"
                      "|    |\n"
                      "|    O\n"
                      "|   '|'\n"
                      "|   ¨ ¨\n")

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if acertou:
        print('Você ganhou!')
    else:
        print('|----Você perdeu----|')
        print(f'a fruta é: {palavra_secreta}')

    print("Fim do jogo")

def imprime_abertura():
    print('_________________________________________')
    print('|     Bem-vindo ao jogo da Forca        |')
    print('-----------------------------------------')

def gerar_palavra_secreta():
    arquivo = open("Teste.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inic_letras_acertada(palavra):
    return ["_" for letra in palavra]

def chutar():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute
if __name__ == '__main__':
    jogar()

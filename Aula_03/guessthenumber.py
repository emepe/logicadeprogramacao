import random

perguntaNome = "\nQual é o seu nome?\n\nR.: "
perguntaNumero = "\nDigite um número de 0 a 100:\n\nR.: "
recorde = 101

while True:
    palpitesPassados = []
    numeroTentativas = 1

    nome = input(perguntaNome)
    print(f"\n\nSeja bem vindo(a), {nome}!")
    numero = int(input(perguntaNumero))


    numeroAleatorio = random.randint(0,100)

    while numero != numeroAleatorio:

        if numero in palpitesPassados:
            print("Esse numero já foi...")

        else:
            palpitesPassados.append(numero)
        
            numeroTentativas += 1 #numero_tentativas = numero_tentativas + 1
            

            if numero > numeroAleatorio:  
                    print("\n\nMuito alto, tente um número menor...")

            else:
                    print("\n\nMuito baixo, tente um número maior....")

    numero = int(input(perguntaNumero))

    if numeroTentativas < recorde:
        recorde = numeroTentativas


    print(f"\nAcertoooouuu!!! Conseguiu em {numeroTentativas} tentativas!\n\nO seu recorde, até você dar F5, é de {recorde} tentativas!")



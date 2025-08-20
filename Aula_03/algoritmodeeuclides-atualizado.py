pergunta1 = "\nDigite o primeiro número:\n\nR.:"
pergunta2 = "\nDigite o segundo número:\n\nR.:"

numero1 = int(input(pergunta1))
numero2 = int(input(pergunta2))

while numero1 != numero2:
    if numero1 > numero2:
        numero1 = numero1 - numero2
        
    else:
        numero2 = numero2 - numero1

print(f"\nPrimeiro número: {numero1}\nSegundo número: {numero2}")
    
    # sdfdsf



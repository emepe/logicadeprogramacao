notas_e_moedas = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05]

# Qual o valor a receber? 8,20

# Qual o valor que foi recebido? 10,00

# O troco é:
    # 1 nota(s) de 1 real(is)
    # 1 moeda(s) de 50 centavo(s)
    # 1 moeda(s) 25 centavo(s)
    # 1 moeda(s) 5 centavo(s)

a_receber = float(input("\nQual o valor à receber?\n\nR.: "))
recebido = float(input("\nQual foi o valor recebido?\n\nR.: "))

diferenca = recebido - a_receber
17.
for valor in notas_e_moedas:
    quantidade_de_itens = 0
    if valor <= diferenca: 
        quantidade_de_itens += 1
        diferenca -= valor

    if quantidade_de_itens> 0:
        print(f'\n{quantidade_de_itens} itens de {valor}\n')
    
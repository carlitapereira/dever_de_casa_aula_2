     #Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
    # Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
    #que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

#input tamanho em metros quadrados
#uma lata de tinta pinta 3 metros quadrados
#cada lata de tinta tem 18l
#informar quantidade de latas e preco total

quantidade_de_metros_quadrados = float(input("Informe a quantidade de metros quadrados"))
quantidade_pitanda_por_litro  = 3
quantidade_de_litros_por_lata = 18
valor_da_lata = 80

Metros_pintados_por_lata = quantidade_de_litros_por_lata * quantidade_pitanda_por_litro
quantidade_de_latas_a_serem_compradas = quantidade_de_metros_quadrados / Metros_pintados_por_lata
valor_a_ser_pago = quantidade_de_latas_a_serem_compradas * valor_da_lata

print("É necessário comprar",quantidade_de_latas_a_serem_compradas,"latas de tinta.")
print("O valor do orçamento é:",valor_a_ser_pago,"Reais")
# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;

quantidade_de_metros_quadrados = float(input("Informe a quantidade de metros quadrados"))
quantidade_pitanda_por_litro  = 6
quantidade_de_litros_por_lata = 18
valor_da_lata = 80
quantidade_de_litro_por_galao = 3.6
valor_do_galao = 25

Metros_pintados_por_lata = quantidade_de_litros_por_lata * quantidade_pitanda_por_litro
quantidade_de_latas_a_serem_compradas = quantidade_de_metros_quadrados / Metros_pintados_por_lata
valor_a_ser_pago_em_latas = quantidade_de_latas_a_serem_compradas * valor_da_lata
metros_pintados_por_galao = quantidade_de_litro_por_galao * quantidade_pitanda_por_litro
quantidade_de_galoes_a_serem_comprados = quantidade_de_metros_quadrados / metros_pintados_por_galao
valor_a_se_pago_em_galoes = quantidade_de_galoes_a_serem_comprados * valor_do_galao

print("voce tem duas opções:")
print("comprar",quantidade_de_latas_a_serem_compradas,"latas, por ",valor_a_ser_pago_em_latas,"Reais")
print("ou")
print("comprar",quantidade_de_galoes_a_serem_comprados,"galões, por",valor_a_se_pago_em_galoes,"Reais")


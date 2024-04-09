quantidade_de_bananas = float(input("Insira a quantidade de bananas que você comprou "))
quantidade_de_macas = float(input("Insira a quantidade de maçãs que você comprou "))
quantidade_de_mangas = float(input("Insira a quantidade de mangas que você comprou"))

def quantidade_de_frutas_compradas_na_feira():
    total_de_frutas_compradas_na_feira = quantidade_de_bananas + quantidade_de_macas + quantidade_de_mangas
    return total_de_frutas_compradas_na_feira
quantidade_de_frutas_compradas_na_feira

print("No total, você comprou ", quantidade_de_frutas_compradas_na_feira, "frutas na feira")
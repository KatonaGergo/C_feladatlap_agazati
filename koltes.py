money_amount = int(input("Írd ide, hogy mennyi pénzed van:"))
money_willing_to_spend = int(input("Írd ide, hogy mennyit szeretnél költeni:"))

while money_amount > 0:
    if money_willing_to_spend > money_amount:
        print("Nincs elég pénzed!")
        break
    else:
        money_amount -= money_willing_to_spend
        print(f"Ennyi pénzed maradt: {money_amount}")
        money_willing_to_spend = int(input("Írd ide, hogy mennyit szeretnél költeni: "))
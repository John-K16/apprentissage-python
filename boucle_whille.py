nombre = int(input("Entrez un nombre :"))
combien = int(input("Combien de tours voulez-vous :"))
tour = 0
resultat = []
while tour < combien :
    tour = tour + 1
    total = tour * nombre
    resultat.append(total)

    print(f"Tour : {tour} multiplier par {nombre} est : {total}")
print(f"VOICI LA LISTE DE TOTAUX : {resultat}")

print("-----------------------------------------------------------------")
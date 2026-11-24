nombre = int(input("Entrer un nombre :"))
combien = int(input("combien de tours voulez-vous :"))
resultat = []
for tour in range(1, combien + 1) :
    total = nombre * tour
    resultat.append(total)

    print(f"TOUR : {tour} multiplier par : {nombre} est : {total}")
print(f"VOICI LA LISTE DE TOTAUX {resultat}")

print("--------------------------------------------------------------------------")

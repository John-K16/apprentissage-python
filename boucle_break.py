nombre = int(input("Entrez un nombre :"))
combien = int(input("combien de tour :"))
resultat = []

for tour in range(1, combien + 1) :
    total = nombre * tour
    resultat.append(total)

    print(f"TOUR {tour} multiplier par {nombre} est : {total}")

print(f"voici ma liste {resultat}")

print("------------------------------------------------------")
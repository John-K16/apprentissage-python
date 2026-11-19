nombre =int(input("Inserez un nombre :"))   
tour = 0
resultat = []
while  tour < 8: 
    tour = tour + 1
    total = nombre ** tour
    resultat.append(total)
    print(f" TOUR : {tour} {nombre} puissance de {tour} est : {total}")
    

print(f"voici ma liste: {resultat}")
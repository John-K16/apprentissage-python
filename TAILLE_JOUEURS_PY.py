admis = 0
total= 0

while True:
    taille = float(input("Entrer votre taille :"))
    age = int(input("Entrer votre age :"))
    total = total + 1

    if taille == 0:
        print("Fin du recrutement !")
        break

    if taille >= 1.80 and 18 <= age <= 21 :
        print("Vous etes admis")
        admis = admis + 1

        print("-----------------------------------------------")
    else :
        print("Vous n'etes pas admis.")

    print(f"pour l'instant {admis} joueur (s) admis sur {total} testés")
    print(f"pourcentage :{admis * 100 / total} % ")

    print("--------------------------------------------------")
for i in range(2):
    villes = ["LUSAMBO", "KINDU", "MBUJIMAYI"]
    ville = input("Entrer une ville :").strip().upper()
    if ville not in villes :
        print("ville non autorisée")
        print("----------------------------------------------")
    else :
        print("ville autorisée")
        print("----------------------------------------------")

for i in range(3):
    jour = input("Entrer le jour :").strip().upper()
    jours_feries = ["SAMEDI", "DIMANCHE"]
    if jour in jours_feries :
        print("C'est un jour férié")
    else :
        print("Le marché est opérationnel")
        print("-----------------------------------------------")
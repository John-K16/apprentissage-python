for i in range(4):
    societe =("GARDAWORD")
    offre_emploi = ("Agent de sécurité")
    communes_recquises =["GOMBE", "KINSHASA", "LIMETE", "MASINA"]
    langues_parlees_ecrites_recquises = ["français", "lingala"]
    niveau_etude_minimum = ["D6", "Licence", "Master"]
    taille = float(input("Entrer votre taille :"))
    age = int(input("Entrer votre age :"))
    langue = input("Entrer votre langue :").strip().upper()
    commune = input("Entrer votre commune :").strip().upper()
    niveau_etude = input("Quel est votre niveau d'etude :").strip().upper()

    if taille >= 1.60 and 18 <= age <= 35 and commune in communes_recquises and langue in langues_parlees_ecrites_recquises and niveau_etude in niveau_etude_minimum :

        print(f"La societé {societe} vous souhaite la bienvenue et vous informe que vous avez été (e) embaucher au poste d'{offre_emploi} ")

        print("-----------------------------------------------------------------------------------")

    else :
        print("Vous n'etes pas retenu")

        print("-----------------------------------------------------------------------------------")

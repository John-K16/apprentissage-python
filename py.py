societe = "KMTA"
poste = input("Pour quel poste postulez-vous :")
nombre_postes = 4

nombre_candidats_retenus = 0
sont_retenus = []

while nombre_candidats_retenus < nombre_postes :
    nombre_candidats_retenus = nombre_candidats_retenus + 1
    

    nom = input("Nom du candidat :")
    sont_retenus.append(nom)

    print(f" le Groupe {societe} a le reel plaisir de vous annoncé que vous avez été embaucher au poste du {poste} ")
    print(f"LISTE DE CADINDATS RETENUS {sont_retenus}")
    print(f"NOMBRE DES CANDIDATS RETENUS : {nombre_candidats_retenus}")

    print("----------------------------------------------------------------------------------------------------------------------------------")
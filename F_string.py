for i in range(4):

    nom=input("Entrer votre nom :")
    age=int(input("Entrer votre age :"))
    pays=input("Entrer votre pays :").strip().upper()

    pays_afrique=["NIGERIA", "ANGOLA", "NIGER", "RDC", "DRC", "RD.CONGO", "RD CONGO", "REPUBLIQUE DEMOCRATIQUE DU CONGO", "ALGERIE", "ANGOLA", "BENIN", "BOTSWANA", "BURKINA FASO", "BURUNDI", "CAP VERT", "CAMEROUN", "CENTRAFRIQUE", "TCHAD", "COMORES", "CONGO", "RDC", "RD.CONGO", "RD CONGO", "DRC", "REPUBLIQUE DEMOCRATIQUE DU CONGO", "DJIBOUTI", "EGYPTE", "GUINEE EQUATORIALE", "ERYTHREE", "ESWATINI", "ETHIOPIE", "GABON", "GAMBIE", "GHANA", "GUINEE", "GUINEE-BISSAU", "COTE D'IVOIRE", "KENYA", "LESOTHO", "LIBERIA", "LIBYE", "MADAGASCAR", "MALAWI", "MALI", "MAURITANIE", "MAURICE", "MAROC", "MOZAMBIQUE", "NAMIBIE", "NIGER", "NIGERIA", "OUGANDA", "RWANDA", "SAO TOME ET PRINCIPE", "SENEGAL", "SEYCHELLES", "SIERRA LEONE", "SOMALIE", "AFRIQUE DU SUD", "SOUDAN DU SUD", "SOUDAN", "TANZANIE", "TOGO", "TUNISIE", "ZAMBIE", "ZIMBABWE"]

    print(f"je m'appelle {nom}")
    print(f"j'ai {age} ans")
    print(f"je viens de {pays}")

    if  pays in pays_afrique:
        print("vous n'etes pas éligible")
    else:
        print("vous etes éligible")

    print("-----------------------------------------")
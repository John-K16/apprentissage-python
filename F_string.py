for i in range(4):

    nom=input("Entrer votre nom :")
    age=int(input("Entrer votre age :"))
    pays=input("Entrer votre pays :")

    print(f"je m'appelle {nom}")
    print(f"j'ai {age} ans")
    print(f"je viens de {pays}")

    if pays == ("RDC"):
        print("vous n'etes pas éligible")
    else:
        print("vous etes éligible")

        print("-----------------------------------------")
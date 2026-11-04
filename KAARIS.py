for i in range(4):

    nombre_01=int(input("Entrer un nombre: "))
    nombre_02=int(input("Entrer un nombre: "))

    if nombre_02 == 0:
            print("impossible de diviser par 0!")
    else:
            #icion inser toutes les opérations

        puissance=nombre_01**nombre_02
        produit=nombre_01*nombre_02
        division=nombre_01/nombre_02
        division_entiere=nombre_01//nombre_02
        modulo=nombre_01%nombre_02

   
        print(nombre_01,"puissance de", nombre_02,"est", puissance)
        print(nombre_01, "produit de", nombre_02, "est", produit)
        print(nombre_01, "division entière de", nombre_02, "est", division_entiere)
        print(nombre_01, "modulo de", nombre_02, "est", modulo)
        print(nombre_01,"divisé par", nombre_02, "est", division)

    print("-------------------------------------------------")
    
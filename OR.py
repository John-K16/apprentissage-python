for i in range(5):
    filiale = ("KMTA Cloud")
    elements= ["ELEMENT1," "ELEMENT2", "ELEMENT3", "ELEMENT4"]
    elements.extend(["ELEMENT5", "ELEMENT6", "ELEMENT7"])
    villes_requises = ["KINSHASA", "KANANGA", "KINDU"]

    element = input("Entrer un element :").strip().upper()
    ville = input("Entrer une ville :").strip().upper()



    if element in elements or ville in villes_requises :
        print(f"La filiale du KMTA GROUP, {filiale} vous souhaite une bonne utilisation")
        
        print("-------------------------------------------------")
    elif "ELEMENT2" in elements :
            elements.remove("ELEMENT2")
    else :
        print("Vous n'etes pas autoriser d'utiliser ce servicre")

        print('-----------------------------------------------------------')

while True:
    note = int(input("Entrer une note : "))
    if note >= 18 and note <= 20 :
     print (" TRES BIEN ")
    elif note >= 16 and note <=17:
        print("BIEN ")
    elif note >=10:   
        print("PASSABLE ")
    else:
       print("ECHEC")


       print("---------------------------------------------")

nb_de_courses_par_vehicule_par_mois = int(input(" Entrez le nombre des courses par mois :"))
montant_par_course = int(input(" Entrez la l'argent gagné par course :"))

course = 0
resultat = []

while course < nb_de_courses_par_vehicule_par_mois :
    course = course + 1
    montant_accumulé_par_vehicule_par_mois = course * montant_par_course
    resultat.append(montant_accumulé_par_vehicule_par_mois)

    print(f" course {course} le montant accumulé apres chaque course est : {montant_accumulé_par_vehicule_par_mois}")

print(f"VOICI LES MONTANTS PAR MOIS : {resultat}")
print("------------------------------------------------------------------------------------------------------------------------------")

# Saisie du numérateur
while True:
    # Valid que l'entrez est un nombre entier
    try:
        numerateur =int(input("Entrez le numérateur: "))
        break  #La conversion fonctionne!! on sort de du while loop avec le break et va a l'étape suivante
    except ValueError:
        print("Oups veuillez entrez un nombre entier pour numérateur")


# Saisir de denomnateur
while True:
    # valide que l'entrez est un nombre entier
    try:
        denominateur = int(input("Entrez le dénominateur: "))
        # on valide que c'est pas zero avant de proceder
        if denominateur != 0:
            break #La conversion fonctionne!! on sort de du while loop avec le break et va a l'étape suivante
        else :
            # Si égale a zéro on print le message d'erreur
            print("Erreur division par zéro!! veuillez entrez un autre valeur ")
    except ValueError:
        print("Oups veuillez entrez un nombre entier pour dénominateur")

#On imprime le resultat!            
print("le resultat de la division est : " + str(numerateur / denominateur ))




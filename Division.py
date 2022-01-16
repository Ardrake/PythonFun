# Saisie du numérateur
while True:
    # Valid que l'entrez est un nombre entier
    try:
        numerateur =int(input("Entrez le numerateur: "))
        break  #on sort de du while loop et va a l'étape suivante
    except ValueError:
        print("Oups veuillez entrez un nombre entier")


# Saisir de denomnateur
while True:
    # valide que l'entrez est un nombre entier
    try:
        denominateur = int(input("Entrez le dénominateur: "))
        if denominateur != 0:
            break # On sort de la loop et on va a l'étape suivante
        else :
            # Si égale a zéro on print le message d'erreur
            print("Erreur division par zéro!! veuillez entrez un autre valeur ")
    except ValueError:
        print("Oups veuillez entrez un nombre entier")

#On imprime le resultat!            
print("le resultat de la division est : " + str(numerateur / denominateur ))




def estPremier():

    while True:
    # Valid que l'entrez est un nombre entier
        try:
            n=int(input("Entrez un nombre:"))
            break  #La conversion fonctionne!! on sort de du while loop avec le break et va a l'étape suivante
        except ValueError:
            print("Oups veuillez entrez un nombre entier")
    # On test si c'est un nombre entier et on exclut 1, 1 et tous ce qui est plus petit
    if n > 1:
        for i in range(2 , n):
            # on valide le modulo ou restant de la division si aucun restant ca ce divise par un autre nombre 
            # donc c'Est pas un nombre premier on break et affiche le resultat
            if(n % i)==0:
                print(n,"Est pas un nombre premier")
                break
        else:
            # si ca divise par rien d'autre donc c'est un nombre premier et on print le resultat
            print(n,"Est un nombre premier")
    else:
        # exclut 0,1 et tous les chiffre negatif
        print(n,"Est ni un, ni l'autre")



estPremier()
def estPremier(num):
    # On test si c'est un nombre entier et on exclut 1, 1 et tous ce qui est plus petit
    if n > 1:
        for i in range(2 , n):
            # on valide le modulo ou restant de la division si aucun restant ca ce divise par un autre nombre 
            # donc c'Est pas un nombre premier on break et affiche le resultat
            if(n % i)==0:
                return False
        else:
            # si ca divise par rien d'autre donc c'est un nombre premier et on print le resultat
            return True
    else:
        # exclut 0,1 et tous les chiffre negatif
        return False

n=int(input("Entrez un nombre:"))

if estPremier(n):
    print(n,"Est un nombre premier")
else:
    print(n,"Est pas un nombre premier")


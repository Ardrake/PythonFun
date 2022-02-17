texte = "salut Polytechnique. j'apprends la programation! Comment ca va?"
poncutation = ['!', '?', '.']

# On recherche la ponctuation dans la string et declare les debut et fin de string
# on fait une string de chacune et ensuite on append la string a la liste phrase.
phrase = []
start = 0
index = 0
for letter in texte:
    index += 1
    if letter in poncutation:
        print ("Index debut:", start, "- Index fin:", index) 
        phrase.append(texte[start:index])
        start = index + 1
        
print(phrase)

# Pour chaque phrase on capitalize le premier caractère 
# On reconstruit le texte avec la caps dans une variable resultat on commence la string avec le " 
# et on remet un espace la fin
resultat = ''

for p in phrase:
     resultat += p.capitalize() + " "
     
print (resultat)

# on rajoute les appostrophe au texte et enleve l'espace vide a la fin
print ('"' + resultat[:-1]+ '"')

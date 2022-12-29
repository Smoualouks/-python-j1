import sys

# Affichage de tous les arguments (type liste) fournis en ligne de commande

print(type(sys.argv)) # argv c'est une liste propre au sys
 
# Affichage  du carré de la valeur saisie par le de premier argument
# Pas de vérification des entrées, érreur possible.

arg1 = int(sys.argv[1])
print(arg1 * arg1)
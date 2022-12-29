#  saisie d'un entier , pour afficher sa table de multiplication

n = int( input("enter un nombre entier:"))
count = 0

if n in range(0, 10001):

   for count in range(0,n):
    print(n*count)

else:
    print(" SVP, entrer un nombre entre 0 et 1000 !")
#  saisie d'un entier , pour afficher sa table de multi
from sys import argv

n = int(argv[1])  # apprcoeh optimiste, pas de vérif de saisie.

if n < 0 or n > 1000:
    print("Doit être compris entre 0 et 1000")
    exit(1)
for i in range(11):
    print(" %d x %d = %d " % (n, i, n*i))
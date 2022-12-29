# print("Donne-moi ton âge:")
# age = input()
# print("Tu as donc: ", age, "ans") # içi la , sépare entre les argument de fct print

print("Tapez un entier, je calcule son carré")
# n = input()
n =  int(input())
# square = n * n    # ooops err car n en entrée input est du str et non pas nombre.
square = int(n) * int(n)  # n étant srt , on cast en int avant pr le calcul

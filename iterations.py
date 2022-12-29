# La boucle while:

count = 0
while count < 5:
    print("Bonjour")
    count += 1  # incrémentation de 1
count2 = 5
while count2 > 0:
    print("Bye", count2)
    count2 -= 1 # décémentation de 1

# La boucle for .. in

for i in range(100):
    print("coucou", i)
    if i == 5:  # sortie de boucle prématurée
        break

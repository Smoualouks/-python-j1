postCodes = [
    67200, 75012, 68520, 15000, 75020,
    67200, 75012, 68520, 15000, 75020,
    67200, 75012, 68520, 15000, 75020,
    67275, 75012, 68520, 17750, 75020,
    75007, 75012, 68520, 75000, 75020
]

# combien de codes postaux parisiens ?
# 1. varriable d'accumulation
# 2. parcourir la liste
# 3. recher de ce qui commence par 75
# 4. incrém accu

numParis = 0



for postCode in postCodes:
    # Approche num 1:
#     if postCode >= 75000 and postCode <= 75999:
#         numParis += 1

# print("Nomre de codes postaux parisiens: ", numParis)

# Approche 2 ( start with):

  postCodeStr = str(postCode)
  dpt = postCodeStr[:2]  # indice 0 et 1. 2 exclus même que [0:2] ça s'appelle slicing
  if dpt == "75":
    numParis += 1
print("Nomre de codes postaux parisiens: ", numParis)

# Autre exemple de slicing:
# Affichage des 3 derniers codes postaux de la liste initiale:

print(postCodes[-3:])   # les 3 derniers.

for p in postCodes[-3:]:
    print (p)
    
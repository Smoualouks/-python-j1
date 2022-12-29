t = ()
print (type (t)) # tuple

coordsGps = (45.9632, 21.7891)
print(coordsGps)
print(" Latitude", coordsGps[0])
print(" Longitude", coordsGps[1])  

# coordsGps[0] = 46.7777      ---->erreur  car on ne peut écaser coordsGps[0], c'est mode read only
# l.append ajoute un élément à la liste.  append n'éxiste pas pour les tuples.
# coordsGps.append ---> erreur.

lat, lng = coordsGps # tuple unpacked
print(lat, lng)
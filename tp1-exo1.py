# static verios
#SECRET=85
import random

# random version (bestween 1 and 10)
SECRET = random.randint(1, 10)

# infinie loop

while True:
  answer =  input("Devine mon chiffre secret: ")
  if int(answer) == SECRET:
    break
  if int(answer) > SECRET:
    print("Mon chiffre est plus petit")
  else:
      print("Mon chiffre est plus grand")
    
print("Bravo ! Le chiffre secret à deviner était bien:", SECRET)
     

  

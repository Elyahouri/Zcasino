import math
import random

somme = int(input("Vous avez quelle somme en poche"))


while somme>0 :
    bet = int(input("Vous misez combien?"))
    while bet>somme :
        bet = int(input("Vous n'avez pas assez d'argent. Veuillez miser moins."))

    while bet==0 :
        bet = int(input("Vous devez miser plus! Du coup, vous misez combien?"))

    somme = somme - bet    
    number = int(input("Et vous misez sur quel numéro?"))
    while number>49 or number<0:
        number = int(input("Ce numéro n'est pas sur la roue. Veuillez en choisir un autre"))

    roue = random.randint(0,49)

    if roue == number:
        somme = somme+bet*3
        print("Le numéro est",roue,", vous avez donc gagné",bet*3,"€, vous avez donc",somme,"€ en poche")
    elif roue%2 == number%2:
        if roue%2 == 0:
            color = "rouge"
        else:
             color = "noir"
        somme = somme+bet+(math.ceil(bet/2))
        print("Le numéro", roue,"est de couleur",color,", comme le votre. Vous avez gagnez"
              ,(math.ceil(bet/2)),"€,vous avez donc",somme,"€ en poche")
    elif somme>0 :
        print("Dommage, vous avez perdu",bet,"€, il vous reste donc maintenant",somme,". Réessayez!")
    
if somme==0 :
    print("Vous n'avez pas d'argent ! Dommage ! Espèce de pauvre WSH")

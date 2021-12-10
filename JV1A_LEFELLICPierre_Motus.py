liste_mots=["castor", "cinema", "chance", "manger", "dormir", "cerise", "destin", "festin", "patate", "citron"]

import random
mot=liste_mots[random.randint(0,9)]

masque=[]
for i in range(6):
    masque.append(i)

print("Trouvez les lettres de ce mot :", masque, "\n\n")

points=0
chances=8

bonnes_lettres=[]
mauvaises_lettres=[]

bien_place=[0,1,2,3,4,5]



while points<6 and chances>0:


    
    stop=False
    while stop==False:
        lettre=input("Donnez une lettre simple minuscule : ")
        if len(lettre)==1 and ord(lettre)>96 and ord(lettre)<124:
            stop=True
            
    stop=False
    while stop==False:
        position=0
        position=int(input("Donnez sa position : "))
        if position<6 and position>=0:
            stop=True



    erreur=True
    for i in range(6):
        if lettre==mot[i]:
            erreur=False

    if erreur==True:
        print("Cette lettre n'est pas dans le mot.")

        ajouter=True
        for i in range(len(mauvaises_lettres)):
            if lettre==mauvaises_lettres[i]:
                ajouter=False
        if ajouter==True:
            chances=chances-1
            mauvaises_lettres.append(lettre)
        
    else:
        if bien_place[position]!="V":
            masque[position]=lettre
        
        ajouter=True
        for i in range(len(bonnes_lettres)):
            if lettre==bonnes_lettres[i]:
                ajouter=False
        if ajouter==True:
            bonnes_lettres.append(lettre)
            
        if (masque[position]!=mot[position] and erreur==False) or lettre!=masque[position] :
            if lettre==masque[position]:
                masque[position]="(" + masque[position] + ")"
            print("Cette lettre n'est pas à la bonne place.")
        else:
            points=points+1
            print("Cette lettre est à la bonne place.")
            bien_place[position]="V"


            
    print(masque,"Il vous reste", chances, "chances.\n\n")
    print("Lettres incorrectes :", mauvaises_lettres)
    print("Lettres correctes :", bonnes_lettres)



if chances==0:
    print("\nVous avez perdu !")
else:
    print("\nVous avez gagné !")

#j'ai mal compris, il faut demander un mot et pas une lettre

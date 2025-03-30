# -*- coding: utf-8 -*-
from tkinter import font as tkfont
from tkinter import *
import random
import math

def recuit():
    global tournee, liste_ville
    N=len(tournee)
    nombre_de_recuits=5000
    marge_recuit=0.05
    proba_recuit=0.1
    min_longueur=longueur_chemin(tournee, liste_ville)
    for step in range(nombre_de_recuits):
        r1=random.randint(0,N-2)
        r2=random.randint(r1,N-1)
        #On essaye d'échanger les villes d'indice r1 et r2 de la tournée
        tournee_bis=A_COMPLETER
        #Si la longueur de la nouvelle tournée est plus courte que l'ancienne, on met à jour tournee
        if A_COMPLETER :
            A_COMPLETER
        #Sinon, si la longueur de la nouvelle tournée est un peu plus longue que l'ancienne (d'un facteur marge_recuit), on met à jour tournee avec une probabilité proba_recuit
        elif A_COMPLETER :
            A_COMPLETER
    dessine_chemin()
    return
    
         
def dessine_chemin():
    global tournee,liste_ville, img
    can1.create_image(0, 0, image=img, anchor=NW)
    for k in range(len(tournee)-1):
        x1,y1=liste_ville[tournee[k]]
        x2,y2=liste_ville[tournee[k+1]]
        can1.create_oval(x1-2, y1-2,x1+2, y1+2,fill="red")
        can1.create_line(x1,y1,x2,y2)
    x1,y1=liste_ville[tournee[-1]]
    x2,y2=liste_ville[tournee[0]]
    can1.create_oval(x1-2, y1-2,x1+2, y1+2,fill="red")
    can1.create_line(x1,y1,x2,y2)
    return

def longueur_chemin(tournee,liste_ville):
    longueur=0
    for k in range(len(tournee)-1):
        x1,y1=liste_ville[tournee[k]]
        x2,y2=liste_ville[tournee[k+1]]
        longueur+=math.sqrt((x2-x1)**2+(y2-y1)**2)
    x1,y1=liste_ville[tournee[-1]]
    x2,y2=liste_ville[tournee[0]]
    longueur+=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return longueur  
    
# Programme principal
# ###################
fen1 = Tk()
# création d'un widget 'Canvas' à la taille de l'image
can1 = Canvas(fen1, width =500, height =500, bg ='white')
can1.grid(column=1)

#Affichage du fond de carte
img = PhotoImage(file='carte_de_france.png')
can1.create_image(0, 0, image=img, anchor=NW)

# Coeficient du point 0,0 du graphique 
#latitude -> y , longitude -> x
base_latitude = 42.517769
base_longitude = -4.71223
# Coefficient pour dessiner une carte de 500 points sur 500 :
echelle_latitude = 0.016816
echelle_longitude = 0.02605

f = open('villes_fr_coords.csv',"r")
liste_ville = {}
for l in f:
    # on éclate les données des villes
    ville,latitude,longitude,region,h = l.split(',')
    # on garde les villes de + de 100 000 habitants
    # on les représente par un rond rouge sur la carte
    if int(h) > 100000:
        liste_ville[ville] = [int((float(longitude) - base_longitude) / echelle_longitude), int(500-(float(latitude) - base_latitude) / echelle_latitude)]    
        can1.create_oval(liste_ville[ville][0]-2, liste_ville[ville][1]-2,liste_ville[ville][0]+2, liste_ville[ville][1]+2,fill="red")
f.close()

# tournee initiale = liste aléatoire de toutes les villes
tournee = (random.sample(list(liste_ville.keys()), len(liste_ville)))
print(tournee)

#Tournée initiale
dessine_chemin()

# création du bouton Recuit
b1=Button(fen1,text='Recuit',command=recuit)
b1.grid(column=2)

# création du bouton Quitter
b1=Button(fen1,text='Quitter',command=fen1.destroy)
b1.grid(column=2)


# démarrage :
fen1.mainloop()

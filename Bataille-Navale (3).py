# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 21:57:41 2017

@author: Group
"""

import tkinter as tk

#==============================================================================
hauteurcadre=500
largeurcadre=500
taillejeu="1000x1000"
global positionbateau
positionbateau=[]
l=largeurcadre/11
h=hauteurcadre/11 
#==============================================================================

master = tk.Tk()
master.title("Bataille Navale")
master.geometry(taillejeu)
tk.Frame(master).grid()
cadre=tk.Canvas(master, width=hauteurcadre, height=largeurcadre,bg="white")
cadre.grid(column=0, row=0)
cadre2=tk.Canvas(master, width=hauteurcadre, height=largeurcadre,bg="white")
cadre2.grid(column=1, row=0)



def grille():   #def grille
    l=largeurcadre/11
    h=hauteurcadre/11
    lettre=["A","B","C","D","E","F","G","H","I","J","H"]

    for i in range(11):
        cadre.create_line(l*i,0,l*i,hauteurcadre)
        cadre.create_line(0,h*i,hauteurcadre,h*i)
        cadre.create_text(largeurcadre/22,l*i+(3*largeurcadre/22),text=i+1)
        cadre.create_text(l*i+(3*hauteurcadre/22),hauteurcadre/22,text=lettre[i])
        
        cadre2.create_line(l*i,0,l*i,hauteurcadre)
        cadre2.create_line(0,h*i,hauteurcadre,h*i)
        cadre2.create_text(largeurcadre/22,l*i+(3*largeurcadre/22),text=i+1)
        cadre2.create_text(l*i+(3*hauteurcadre/22),hauteurcadre/22,text=lettre[i])
  
def position(x,y):  #def des quatres coins d'une case
    posx0=(x*l)
    posx1=(x+1)*l
    posy0=(y*h)
    posy1=(y+1)*h
    return posx0,posx1,posy0,posy1
  
def colorier_une_case(x,y):  #fonction qui colorie une case
    posx0,posx1,posy0,posy1=position(x,y)
    cadre.create_rectangle(posx0,posy0,posx1,posy1,fill="grey")    

def attack(x,y):    #fait une croix dans la case
    #legalattack(x,y)    
    posx0,posx1,posy0,posy1=position(x,y)
    cadre.create_line(posx0,posy0,posx1,posy1,fill="red")
    cadre.create_line(posx0,posy1,posx1,posy0,fill="red")


def legalattack(x,y):   #teste si le joueur n'a pas deja attaqué à cet endroit
    pass

    
def choix_de_positions(event): #prendre les clicks de l'utilisateus et convertir en position(1 à 10)
    x=(event.x)
    y=(event.y)
    for i in range(1,12):
        if i*l/11<x<(i+1)*l:
            x=i
            break
    for i in range(1,12):
        if i*h/11<y<(i+1)*h:
            y=i
            break
    colorier_une_case(x,y)
   # stockagebateau(une_position(x,y))
    
def delete_choix_de_positions(event):
    x=(event.x)
    y=(event.y)
    for i in range(11):
        if i*l/11<x<(i+1)*l:
            x=i
            break
    for i in range(11):
        if i*h/11<y<(i+1)*h:
            y=i
            break
    posx0,posx1,posy0,posy1=position(x,y)
    cadre.create_rectangle(posx0,posy0,posx1,posy1,fill="white")    
    
def une_position(x,y):
    placex=[]
    placey=[]
    for i in range (10):
        placex.append(0)
        placey.append(0)
        if x==i:
            placex[i-1]=1
        if y==i:
            placey[i-1]=1
    return placex,placey
    
def stockagebateau(x,y):    #peut etre utiliser la meme fonction mais 2 liste pour bateau et attaque
    placex,placey=une_position(x,y)
    case=[placex,placey]
    a=n=z=0
                        
    for i in range(len(positionbateau)):
        l1=positionbateau[i]
        a=0
        for n in range(2):
            l2bateau=l1[n]
            l2nouveau=case[n]
            for z in range(len(l2bateau)):
                if l2bateau[z]==l2nouveau[z]:
                    a=a+1
    if a==2*(len(placex)):
        return "Un bateau s'y situe déjà "
    else:
        positionbateau.append([placex,placey])
    
    
def legalité():
    pass


class case:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        
    def __repr__(self):
        return str(self.x) + ','+str(self.y)

cases=[]
for i in range(9):
    cases.append([])
    for j in range(9):
        cases[i].append(case(i,j))


master.bind("<Button-1>", choix_de_positions)
master.bind("<Button-3>", delete_choix_de_positions)

grille()

master.mainloop()

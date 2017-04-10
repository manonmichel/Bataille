# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 21:57:41 2017

@author: Group
"""

import tkinter as tk

#==============================================================================
hauteurcadre=350
largeurcadre=350
taillejeu="800x800"
global positionbateau
positionbateau=[]
l=largeurcadre/11
h=hauteurcadre/11 
#==============================================================================

master = tk.Tk()
master.title("Bataille Navale")
master.geometry(taillejeu)

master.rowconfigure(0, weight=15)
master.rowconfigure(1, weight=1)
master.rowconfigure(2, weight=15)

cadre1 = tk.Canvas(master, width=hauteurcadre, height=largeurcadre,bg="white")
cadre1.grid(column=1,row=0)
cadre2= tk.Canvas(master, width=hauteurcadre, height=largeurcadre,bg="white")
cadre2.grid(column=1,row=2)
empty1=tk.Label(master)
empty1.grid(column=0,row=1)
empty2=tk.Label(master)
empty2.grid(column=1,row=1)
boatframe=tk.Canvas(master, width=450, height=300)
boatframe.grid(column=0,row=2, sticky="N")

def boat_selection():
    l=largeurcadre/11
    #h=hauteurcadre/11
    
    b5_coord = (l+300),10, (l+300),50, (l+50),50, (l+50),10
    b4_coord = (l+270),80, (l+270),120, (l+80),120, (l+80),80
    b3_coord = (l+240),150, (l+240),190, (l+110),190, (l+110),150
    b2_coord = (l+210),220, (l+210),260, (l+140),260, (l+140),220
    
    """
    for i in range (2,5): 
        bi=boatframe.create_polygon(bi_coord, fill="blue")
        def clicked_bi(event):
            print("Boat i selected")
            boatframe.create_polygon(bi_coord, fill="grey")
        boatframe.tag_bind(bi,"<Button-1>",clicked_bi)
    """
    
    b5=boatframe.create_polygon(b5_coord, fill="blue")
    b4=boatframe.create_polygon(b4_coord, fill="blue")
    b3=boatframe.create_polygon(b3_coord, fill="blue")
    b2=boatframe.create_polygon(b2_coord, fill="blue")
    
    def clicked_b5(event):
        print("Boat 5 selected")
        boatframe.create_polygon(b5_coord, fill="grey")
    def clicked_b4(event):
        print("Boat 4 selected")
        boatframe.create_polygon(b4_coord, fill="grey")
    def clicked_b3(event):
        print("Boat 3 selected")
        boatframe.create_polygon(b3_coord, fill="grey")
    def clicked_b2(event):
        print("Boat 2 selected")
        boatframe.create_polygon(b2_coord, fill="grey")
        
    boatframe.tag_bind(b5,"<Button-1>",clicked_b5)
    boatframe.tag_bind(b4,"<Button-1>",clicked_b4)
    boatframe.tag_bind(b3,"<Button-1>",clicked_b3)
    boatframe.tag_bind(b2,"<Button-1>",clicked_b2) 
        
            
def grille():   #def grille
    l=largeurcadre/11
    h=hauteurcadre/11
    lettre=["A","B","C","D","E","F","G","H","I","J","H"]

    for i in range(11):
        cadre1.create_line(l*i,0,l*i,hauteurcadre)
        cadre1.create_line(0,h*i,hauteurcadre,h*i)
        cadre1.create_text(largeurcadre/22,l*i+(3*largeurcadre/22),text=i+1)
        cadre1.create_text(l*i+(3*hauteurcadre/22),hauteurcadre/22,text=lettre[i])
        
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
    cadre1.create_rectangle(posx0,posy0,posx1,posy1,fill="grey")    

def attack(x,y):    #fait une croix dans la case
    #legalattack(x,y)    
    posx0,posx1,posy0,posy1=position(x,y)
    cadre1.create_line(posx0,posy0,posx1,posy1,fill="red")
    cadre1.create_line(posx0,posy1,posx1,posy0,fill="red")


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
    if y<400:
        cadre1.create_rectangle(posx0,posy0,posx1,posy1,fill="white")  
    if y>400:
        cadre2.create_rectangle(posx0,posy0,posx1,posy1,fill="white")  
    
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
    print(a)
    if a==2*(len(placex)):
        return "Un bateau s'y situe déjà "
    else:
        positionbateau.append([placex,placey])
    
    
def legalité():
    pass


play=tk.Button(master, text="Jouer", width="10", height="4")
play.grid(column=0, row=0)


master.bind("<Button-1>", choix_de_positions)
master.bind("<Button-3>", delete_choix_de_positions)

grille()
boat_selection()

"""
def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

master.bind('<Button-1>', motion)
"""

master.mainloop()

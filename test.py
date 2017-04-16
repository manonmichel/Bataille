import tkinter as tk
import random
#==============================================================================
taillejeu="500x500"
hauteurcadre=500
largeurcadre=500
l=largeurcadre/10
h=hauteurcadre/10
#==============================================================================

master = tk.Tk()
master.title("Bataille Navale")
master.geometry(taillejeu)
tk.Frame(master).grid()
cadre=tk.Canvas(master, width=hauteurcadre, height=largeurcadre,bg="white")
cadre.grid(column=0, row=0)


class case:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.bateau=False
        self.case_attaquee=False
        self.xdebut=x*l
        self.xfin=(x+1)*l
        self.ydebut=y*h
        self.yfin=y*h+h
        self.draw()
    def __repr__(self):
        return str(self.x) + ','+str(self.y)
    
    def draw(self):
        rect=cadre.create_rectangle(self.xdebut,self.ydebut,self.xfin,self.yfin, fill=self.color())
        if self.bateau==True and self.attacked==True:
            cadre.create_line(self.xdebut,self.ydebut,self.xfin,self.yfin,fill="red") 
            cadre.create_line(self.xdebut,self.yfin,self.xfin,self.ydebut,fill="red")
        
        cadre.tag_bind(rect, "<Button-1>", self.click)

    def boat(self):
        if self.bateau==False:
            self.bateau=True
            self.draw()
        else:
            self.bateau=False
            self.draw()
"""    def color(self):
        couleur="white"
        if self.bateau==True:
            couleur="grey"
            if self.case_attaquee==True:
                couleur="red" #(C'est ou que tu execute la fonction?(si c'est dans draw, faut mettre un if "red" le truc et une break))
        elif self.case_attaquee==True:
            couleur="black"
        return couleur"""

    def color(self):
        couleur="white"
        if self.bateau==True:
            couleur="grey"
        if self.case_attaquee and self.bateau:
            couleur="red"
        elif self.case_attaquee==True and self.bateau==False:
            couleur="blue"
        return couleur
    
    def attacked(self):
        if self.case_attaquee==False:
            self.case_attaquee=True
            self.draw()
        else:
            self.case_attaquee=False
            self.draw()
    
    def click(self, event):
        self.attacked()
        print(self.case_attaquee and self.bateau)
        
                    
"""                   
def placer_boats(event):    #a mettre dans la classe boat
    n=2
    erreurplacement="placer le bateau en une ligne"
    erreurnb="vous ne pouvez que placer tant de bateau"
    if n==2:
        for i in range (2):
        return 

    if n==3:
        pass
    if n==4:
        pass
    if n==5:
        pass
        
def rancoord(): #renvoie 2 ran
    a=random.randrange(1,9,1)
    b=random.randrange(1,9,1)
    return a,b
  
def attacked_all(liste):
    for i in range(9):
        for j in range(9):
            if liste[i][j].case_attaquee==False:
                return False
    return True
    
    
class ai:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.bateau=False
        self.case_attaquee=False
        self.xdebut=x*l
        self.xfin=(x+1)*l
        self.ydebut=y*h
        self.yfin=y*h+h
       # self.draw()
        
    def __repr__(self):
        return str(self.x) + ','+str(self.y)
        
        
    def aiattack():
        global sens
        a,b=rancoord()
        if attacked_all(cases)== True:
            return False
        while cases[a][b].case_attaquee==True:
            print(cases[a][b].case_attaquee)
            a,b=rancoord()
        cases[a][b].attacked()
        #while [a][b].bateau==True:
        #  if class bateau.bateaucoulee==True:
        #   ai()
        
        c=[0,0,-1,+1]
        d=[1,-1,0,0]
        try:
            for i in range(4):    
                if cases[a+c[i]][b+d[i]].case_attaquee==False:
                    sens="vertical"
                    cases[a+c[i]][b+d[i]].attacked()
                    break
                    
                elif cases[a-1][b].case_attaquee==False:
                    sens="vertical"
                    cases[a-1][b].attacked()
                    break
                elif cases[a][b+1].case_attaquee==False:
                    sens="horizontal"
                    cases[a][b+1].attacked()
                    break
                elif cases[a][b-1].case_attaquee==False:
                    cases[a][b-1].attacked()
                    sens="horizontal"
                    break
                else:
                    while cases[a][b].case_attaquee==True:
                        a,b=rancoord()                
        except IndexError:
            pass
"""


caseadversaire=[]
cases=[]
for i in range(9):
    cases.append([])
    caseadversaire.append([])
    for j in range(9):
        cases[i].append(case(i,j))
        caseadversaire[i].append(adversaire(i,j))


def changement(event):
    cases[0][0].boat()
    print('jello')

master.bind("<Button-1>", changement)

Bouton2 = tk.Button(master, text = 'Placer bateau2', command = placer_boats).grid(row=2, column=1)

master.mainloop()



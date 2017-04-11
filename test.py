import tkinter as tk

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
        
    def check_surrounding(self): #check s'il n'y a pas de bateau autour
        for i in range(-1,1):
            for j in range(-1,1):
                a=self.x+i
                b=self.y+j
                c=case(a,b)
                if c.bateau==True:
                    return False

cases=[]
for i in range(9):
    cases.append([])
    for j in range(9):
        cases[i].append(case(i,j))

def changement(event):
    cases[0][0].boat()
    print('jello')

master.bind("<Button-1>", changement)

master.mainloop()



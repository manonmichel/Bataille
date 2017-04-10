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
        #if self.color=="red":
            #cadre.create_line(self.xdebut,self.ydebut,self.xfin,self.yfin,fill="red") ik it's sketchy, c'est juste que idk how you update your thing
            #cadre.create_line(self.xdebut,self.yfin,self.xfin,self.ydebut,fill="red")
            #break
        cadre.create_rectangle(self.xdebut,self.ydebut,self.xfin,self.yfin, fill=self.color())

    def boat(self):
        if self.bateau==False:
            self.bateau=True
            self.draw()
        else:
            self.bateau=False
            self.draw()
    def color(self):
        couleur="white"
        if self.bateau==True:
            couleur="grey"
            if self.case_attaquee==True:
                couleur="red" #(C'est ou que tu execute la fonction?(si c'est dans draw, faut mettre un if "red" le truc et une break))
        elif self.case_attaquee==True:
            couleur="black"
        return couleur
    
    def attacked(self):
        if self.case_attaquee==False:
            self.case_attaquee=True
            self.draw()
        else:
            self.case_attaquee=False
            self.draw()


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



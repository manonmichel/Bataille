import tkinter as tk
import random
#==============================================================================
taillejeu="1080x1080"
hauteurcadre=800
largeurcadre=400
l=largeurcadre/10
h=hauteurcadre/10
sens="none"
#==============================================================================

master = tk.Tk()
master.title("Bataille Navale")
master.geometry(taillejeu)
tk.Frame(master).grid()
cadre=tk.Canvas(master, width=largeurcadre, height=hauteurcadre,bg="white")
cadre.grid(column=0, row=0)


class case:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.bateau=False
        self.case_attaquee=False        
        self.xdebut=x*l
        self.xfin=(x+1)*l
        self.ydebut=y*(h/2)+hauteurcadre/2
        self.yfin=y*(h/2)+(h/2)+hauteurcadre/2
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
        self.boat()
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
"""
   
def rancoord(): #renvoie 2 ran
    a=random.randrange(0,9,1)
    b=random.randrange(0,9,1)
    return a,b
  
def attacked_all():
    for i in range(9):
        for j in range(9):
            if cases[i][j].case_attaquee==False:
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
        self.ydebut=y*(h/2)
        self.yfin=y*(h/2)+(h/2)
        self.draw()
        
    def __repr__(self):
        return str(self.x) + ','+str(self.y)
        
    def draw(self):
        rect=cadre.create_rectangle(self.xdebut,self.ydebut,self.xfin,self.yfin, fill=self.color())
        if self.bateau==True and self.attacked==True:
            cadre.create_line(self.xdebut,self.ydebut,self.xfin,self.yfin,fill="red") 
            cadre.create_line(self.xdebut,self.yfin,self.xfin,self.ydebut,fill="red")
            
        cadre.tag_bind(rect, "<Button-1>", self.click)
        
    def click(self, event):
        case.attacked(self)
        print(self.case_attaquee and self.bateau)
        
    def color(self):
        couleur="white"
        if self.bateau==True:
            couleur="grey"
        if self.case_attaquee and self.bateau:
            couleur="red"
        elif self.case_attaquee==True and self.bateau==False:
            couleur="blue"
        return couleur
            
    def aiattack():
        global sens
        if attacked_all()== True:
            return False
        try:    
            if sens=="vertical":
                pass
            if sens=="horizontal":
                pass
            else:   
                a,b=rancoord()
                while cases[a][b].case_attaquee==True:
                    a,b=rancoord()
                    cases[a][b].attacked()
            
            
                #while [a][b].bateau==True:
                #  if class bateau.bateaucoulee==True:
                #   ai()
        
                c=[-1,+1]
                d=[0,0]

                for i in range(2):    
                    if cases[a+c[i]][b+d[i]].case_attaquee==False:
                        cases[a+c[i]][b+d[i]].attacked()
                        if cases[a+c[i]][b+d[i]].bateau==True:
                            sens="horizontal"
                            break
                    if cases[a+d[i]][b+c[i]].case_attaquee==False:
                        cases[a+d[i]][b+c[i]].attacked()
                        if cases[a+d[i]][b+c[i]].bateau==True:
                            sens="vertical"
                            break
        except IndexError:
            pass       
        



caseadversaire=[]
cases=[]
for i in range(9):
    cases.append([])
    caseadversaire.append([])
    for j in range(9):
        cases[i].append(case(i,j))
        caseadversaire[i].append(ai(i,j))
      

    
#================== Selectable boats ================================
boatframe=tk.Canvas(master, width=450, height=300)
boatframe.grid(column=1,row=0, sticky="N")

def boat_selection():
    l=largeurcadre/10
    h=hauteurcadre/10
    
    b5_coord = (l+300),(h-40), (l+300),h, (l+50),h, (l+50),(h-40)
    b4_coord = (l+270),(h+30), (l+270),(h+70), (l+80),(h+70), (l+80),(h+30)
    b3_coord = (l+240),(h+100), (l+240),(h+140), (l+110),(h+140), (l+110),(h+100)
    b2_coord = (l+210),(h+170), (l+210),(h+210), (l+140),(h+210), (l+140),(h+170)
    
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

boat_selection()
#====================================================================
"""
def changement(event):
    cases[0][0].boat()
    print('jello')
master.bind("<Button-1>", changement)
"""
#Bouton2 = tk.Button(master, text = 'Placer bateau2', command = placer_boats).grid(row=2, column=1)
ai = tk.Button(master, text = 'ai', command = ai.aiattack).grid(row=0, column=1)

master.mainloop()



import tkinter as tk
import random
#==============================================================================
taillejeu="1080x1080"
hauteurcadre=800
largeurcadre=400
l=largeurcadre/10
h=hauteurcadre/10
sens="none"
ships=[]
#==============================================================================

master = tk.Tk()
master.title("Bataille Navale")
master.geometry(taillejeu)
tk.Frame(master).grid()
cadre=tk.Canvas(master, width=largeurcadre, height=hauteurcadre,bg="white")
cadre.grid(column=0, row=0)

orientation='N'#ffaudra voir si on le fait rester à ce que cest ou si on le fait revenir a N
game_mode=False

def gamemode():        #Seperates the moment of boat placement from the game play
    global game_mode
    game_mode=True
"""   
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
        global game_mode
        global orientation
        if game_mode==False:
            if self.check_surrounding()==False:
                print('Boats can not be adjacent.')
            else:
                global ships
                ships.append(ship(3,orientation))
                bateau_selectionne=ships[len(ships)-1]
                bateau_selectionne.placement(self.x, self.y)
        else:   
            self.attacked()
            print(self.case_attaquee and self.bateau)
                  
    def check_self(self):
        if self.bateau==True:
            return False
        else:
            return True
            
            
    def check_surrounding(self): #check s'il n'y a pas de bateau autour
        xcoordinate=[-1,0,0,+1]
        ycoordinate=[0,+1,-1,0]
        for i in range(4):
            try:
                adjacent_case=cases[(self.x+xcoordinate[i])][self.y+(ycoordinate[i])]
                print(adjacent_case)
                if adjacent_case.bateau==True:
                    return False
            except:
                    IndexError
        return True
                
                 
    def checks(self):
        return self.check_self() and self.check_surrounding()
        

                  
class ship:
    def __init__(self,l,orient):
        self.length=l
        self.orientation=orient
        self.endroits=[]
    
    def __repr__(self):
        return str(self.length)
        
    def placement(self,x,y):
        for i in range(self.length):
            if self.orientation=='S':  #vérifie que le bateau rentre dans le cadre
                if y+self.length>9:
                    return 'Erreur'
                else:
                    cases[x][y+i].boat()  # what if one of the cases is already a boat
                    self.cases(x,y+i)
            elif self.orientation=='E':
                if x-self.length<-1:
                    return 'Erreur'
                else:
                    cases[x-i][y].boat()
                    self.cases(x,y+i)
            elif self.orientation=='N':
                if y-self.length<-1:
                    return 'Erreur'
                else:
                    cases[x][y-i].boat()
                    self.cases(x,y+i)
            elif self.orientation=='W':
                if x+self.length>9:
                    return 'Erreur'
                else:
                    cases[x+i][y].boat()
                    self.cases(x,y+i)
                    
    def cases(self,x,y):
        self.endroits.append(cases[x][y])
 
"""
def sens(event):
    global ships
    global orientation
    if orientation=='N':
        orientation='E'
        print(orientation)
    elif orientation=='E':
        orientation='S'
        print(orientation)
    elif orientation=='S':
        orientation='W'
        print(orientation)
    elif orientation=='W':
        orientation='N'
        print(orientation)                  
                  
"""
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
                  
def ranai():
    return random.randrange(1,4,1)
                  
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
        print(sens)
        if attacked_all()== True:
            return False
        try:    
            if sens=="vertical":
                pass
                #liste1=[1,-1,2,-2,3,-3,4,-4,5,-5]
                #liste2=[0,0,0,0,0,0,0,0,0,0,0,0]
                #while ship not False:
                    #for i in range n:
                        #try:
                            #cases[][liste1[i]]
                        #except IndexError:
            if sens=="horizontal":
                pass
            if sens=="unknown":
                try:
                    essai=False
                    while essai==False:
                        if cases[casebatx+1][casebaty].case_attaquee==True and cases[casebatx-1][casebaty].case_attaquee==True and cases[casebatx][casebaty+1].case_attaquee==True and cases[casebatx][casebaty-1].case_attaquee==True:
                            essai=True
                            a,b=rancoord()
                            while cases[a][b].case_attaquee==True:
                                a,b=rancoord()
                                cases[a][b].attacked()
                                sens="none"
                        random=ranai()
                        if random==1:
                            if cases[casebatx+1][casebaty].case_attaquee==False:
                                cases[casebatx+1][casebaty].attacked()
                                essai=True
                                if cases[casebatx+1][casebaty].bateau==True:
                                    sens="horizontal"
                                else:
                                    sens="unknown"
                                
                        if random==2:
                            if cases[casebatx-1][casebaty].case_attaquee==False:
                                cases[casebatx-1][casebaty].attacked()
                                essai=True
                                if cases[casebatx-1][casebaty].bateau==True:
                                    sens="horizontal"
                                else:
                                    sens="unknown"
                        if random==3:
                            if cases[casebatx][casebaty+1].case_attaquee==False:
                                cases[casebatx][casebaty+1].attacked()
                                essai=True
                                if cases[casebatx][casebaty+1].bateau==True:
                                    sens="vertical"
                                else:
                                    sens="unknown"
                        if random==4:
                            if cases[casebatx][casebaty-1].case_attaquee==False:
                                cases[casebatx][casebaty-1].attacked()
                                essai==True
                                if cases[casebatx][casebaty-1].bateau==True:
                                    sens="vertical"
                                else:
                                    sens="unknown"
                except IndexError: 
                    pass
            else:   
                a,b=rancoord()
                while cases[a][b].case_attaquee==True:
                    a,b=rancoord()
                cases[a][b].attacked()
            
            
                #while [a][b].bateau==True:
                #  if class bateau.bateaucoulee==True:
                #   ai()
                essai=False
                if cases[a][b].bateau==True:
                    while essai==False:
                        if cases[a][b-1].case_attaquee==True and cases[a][b+1].case_attaquee==True and cases[a-1][b].case_attaquee==True and cases[a+1][b].case_attaquee==False:
                            sens="none"
                            essai=True
                            a,b=rancoord()
                            while cases[a][b].case_attaquee==True:
                                a,b=rancoord()
                                cases[a][b].attacked()
                        random=ranai()
                        if random==1:
                            if cases[a+1][b].case_attaquee==False:
                                cases[a+1][b].attacked()
                                essai=True
                                if cases[a+1][b].bateau==True:
                                    sens="horizontal"
                                else:
                                    sens="unknown"
                                
                        if random==2:
                            if cases[a-1][b].case_attaquee==False:
                                cases[a-1][b].attacked()
                                essai=True
                                if cases[a-1][b].bateau==True:
                                    sens="horizontal"
                                else:
                                    sens="unknown"
                        if random==3:
                            if cases[a][b+1].case_attaquee==False:
                                cases[a][b+1].attacked()
                                essai=True
                                if cases[a][b+1].bateau==True:
                                    sens="vertical"
                                else:
                                    sens="unknown"
                        if random==4:
                            if cases[a][b-1].case_attaquee==False:
                                cases[a][b-1].attacked()
                                essai=True
                                if cases[a][b-1].bateau==True:
                                    sens="vertical"
                                else:
                                    sens="unknown"
                    global casebatx
                    global casebaty
                    casebatx=a
                    casebaty=b
                        
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

selectable=True #variable qui assure que seulement un bateau soit séléctionné à la fois
bl=0

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
        global bl
        global selectable 
        if selectable==True:
            selectable=False
            print("Boat 5 selected")
            boatframe.create_polygon(b5_coord, fill="grey")
            rotate_north(event)
            bl=5
        else: 
            print("Veuillez placer le bateau avant de selectionner un autre.")
    def clicked_b4(event):
        global bl
        global selectable 
        if selectable==True:
            selectable=False
            print("Boat 4 selected")
            boatframe.create_polygon(b4_coord, fill="grey")
            rotate_north(event)
            bl=4
        else: 
            print("Veuillez placer le bateau avant de selectionner un autre.")
    def clicked_b3(event):
        global bl
        global selectable 
        if selectable==True:
            selectable=False
            print("Boat 3 selected")
            boatframe.create_polygon(b3_coord, fill="grey")
            rotate_north(event)
            bl=3
        else: 
            print("Veuillez placer le bateau avant de selectionner un autre.")
    def clicked_b2(event):
        global bl
        global selectable 
        if selectable==True:
            selectable=False
            print("Boat 2 selected")
            boatframe.create_polygon(b2_coord, fill="grey")
            rotate_north(event)
            bl=2
        else: 
            print("Veuillez placer le bateau avant de selectionner un autre.")
    
    def rotate_north(event): #Default orientation
        global orientation
        cadre.configure(cursor='sb_up_arrow')
        boatframe.configure(cursor='sb_up_arrow')
        orientation='N'
    def rotate_east(event):
        global orientation
        cadre.configure(cursor='sb_left_arrow')
        boatframe.configure(cursor='sb_left_arrow')
        orientation='E'
    def rotate_south(event):
        global orientation
        cadre.configure(cursor='sb_down_arrow')
        boatframe.configure(cursor='sb_down_arrow')
        orientation='S'
    def rotate_west(event):
        global orientation
        cadre.configure(cursor='sb_right_arrow')
        boatframe.configure(cursor='sb_right_arrow')
        orientation='W'
    
    boatframe.tag_bind(b5,"<Button-1>",clicked_b5)
    boatframe.tag_bind(b4,"<Button-1>",clicked_b4)
    boatframe.tag_bind(b3,"<Button-1>",clicked_b3)
    boatframe.tag_bind(b2,"<Button-1>",clicked_b2)

    master.bind('<Left>', rotate_east)
    master.bind('<Up>', rotate_north)
    master.bind('<Down>', rotate_south)
    master.bind('<Right>', rotate_west)
    
    def place(event):
        global orientation
        global bl
        global selectable
        global ships
        if selectable==False:
            s=ship(bl,orientation)    #ne fonctionne pas encore 
            s.placement(event.x, event.y)
            selectable=True
        else:
            print('Please select a boat to place.')
     
    cadre.bind('<Button-1>', place)

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
play=tk.Button(master, text="Jouer", width="10", height="2", command=gamemode).grid(column=2, row=0)

master.mainloop()

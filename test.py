import tkinter as tk
import random
#==============================================================================
taillejeu="1080x1080"
hauteurcadre=800
largeurcadre=400
l=largeurcadre/11
h=hauteurcadre/11
sens="none"
direction="none"
casebatx=0
casebaty=0
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
    cadre.configure(cursor='boat')
    master.configure(cursor='boat')
    boatframe.configure(cursor='boat')

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
            
            """def place(event):
    global orientation
    global bl
    global selectable
    global ships
    if selectable==False:
        s=ship(bl,orientation)    #ne fonctionne pas encore 
        s.placement(event.x, event.y)
        selectable=True
    else:
        print('Please select a boat to place.')"""
    
    def click(self, event):
        global game_mode
        global orientation
        global bl
        global selectable
        global ships
        environs=True
        if selectable==False:
            if game_mode==False:
                ships.append(ship(bl,orientation))
                bateau_selectionne=ships[len(ships)-1]
                bateau_selectionne.projet(self.x,self.y)
                for i in range(len(bateau_selectionne.projection)):
                    print(bateau_selectionne.projection[i])
                    print(bateau_selectionne.projection[i].check_surrounding())
                    if bateau_selectionne.projection[i].check_surrounding()==False:
                        print('Boats can not be adjacent.')
                        environs=False
                if environs==True:
                    if bateau_selectionne.check_placement(self.x, self.y)==False:
                        print('Boat out of area.')
                    else:
                        bateau_selectionne.placement(self.x, self.y)
                        selectable=True
            else:   
                self.attacked()
                print(self.case_attaquee and self.bateau)
        else:
             print('Please select a boat to place.')
         
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
        self.projection=[]
    def __repr__(self):
        return str(self.length)
    
    def check_placement(self, x, y):
        if self.orientation=='S':  #vérifie que le bateau rentre dans le cadre
            if y+self.length>10:
                return False
        elif self.orientation=='E':
            if x-self.length<-1:
                return False
        elif self.orientation=='N':
            if y-self.length<-1:
                return False
        elif self.orientation=='W':
                if x+self.length>10:
                    return False
        
    def projet(self, x,y):
        for i in range(self.length):
            if self.orientation=='S':  
                self.cases(self.projection,x,y+i)
            elif self.orientation=='E':
                self.cases(self.projection,x-i,y)
            elif self.orientation=='N':
                self.cases(self.projection,x,y-i)
            elif self.orientation=='W':
                self.cases(self.projection,x+i,y)
                    
    def placement(self,x,y):
        for i in range(self.length):
            if self.orientation=='S':  
                cases[x][y+i].boat()  
                self.cases(self.endroits,x,y+i)
            elif self.orientation=='E':
                cases[x-i][y].boat()
                self.cases(self.endroits,x-i,y)
            elif self.orientation=='N':
                cases[x][y-i].boat()
                self.cases(self.endroits,x,y-i)
            elif self.orientation=='W':
                cases[x+i][y].boat()
                self.cases(self.endroits,x+i,y)
                    
    def cases(self,liste,x,y):
        liste.append(cases[x][y])
        
    def bateau_en_vie(self):
        level=0
        for i in range(self.length):
            if self.endroits[i].case_attaquee==False:
                level=level+1
        return level/self.length
 

def rancoord(): #renvoie 2 chiffres random
    a=random.randrange(0,10,1)
    b=random.randrange(0,10,1)
    return a,b
                  
def ranai():    #renvoie un chiffre random entre 1 et 4
    return random.randrange(1,5,1)
                  
def attacked_all(): #check si toutes les cases ont été attaqué
    for i in range(9):
        for j in range(9):
            if cases[i][j].case_attaquee==False:
                return False
    return True
class shipai:
    def __init__(self,l,orient):
        self.length=l
        self.orientation=orient
        self.endroits=[]
        self.projection=[]
    def __repr__(self):
        return str(self.length)
    
    def check_placement(self, x, y):
        if self.orientation=='S':  #vérifie que le bateau rentre dans le cadre
            if y+self.length>10:
                return False
        elif self.orientation=='E':
            if x-self.length<-1:
                return False
        elif self.orientation=='N':
            if y-self.length<-1:
                return False
        elif self.orientation=='W':
                if x+self.length>10:
                    return False
        
    def projet(self, x,y):
        for i in range(self.length):
            if self.orientation=='S':  
                self.cases(self.projection,x,y+i)
            elif self.orientation=='E':
                self.cases(self.projection,x-i,y)
            elif self.orientation=='N':
                self.cases(self.projection,x,y-i)
            elif self.orientation=='W':
                self.cases(self.projection,x+i,y)
                    
    def placement(self,x,y):
        for i in range(self.length):
            if self.orientation=='S':  
                caseadversaire[x][y+i].boat()  
                self.cases(self.endroits,x,y+i)
            elif self.orientation=='E':
                caseadversaire[x-i][y].boat()
                self.cases(self.endroits,x-i,y)
            elif self.orientation=='N':
                caseadversaire[x][y-i].boat()
                self.cases(self.endroits,x,y-i)
            elif self.orientation=='W':
                caseadversaire[x+i][y].boat()
                self.cases(self.endroits,x+i,y)
                    
    def cases(self,liste,x,y):
        liste.append(caseadversaire[x][y])

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
        
    def placeboats():
        global ships
        global orientation
        listea=[5,4,3,3,2,2,2]
        for i in range(len(listea)):
            while shipai.checkplacement==False:
                random=ranai()
                if random==1:
                    orientation="N"
                elif random==2:
                    orientation="E"
                elif random==3:
                    orientation="S"
                elif random==4:
                    orientation="W"
                shipai.placement(rancoord(),listea[i])
            
    def aiattack():
        global sens
        global direction
        global casebatx
        global casebaty
        global ships
        print(direction)
        print(sens)
        if attacked_all()== True:
            return False
            
        try:    
            if sens=="vertical":
                essai=False
                if ships[quel_bateau(cases[casebatx][casebaty])].bateau_en_vie()== 0:
                    sens="none"
                    direction="none"
                else:
                    while essai==False:
                        try:
                            if direction=="haut":
                                while essai==False:
                                    if cases[casebatx][casebaty-1].case_attaquee==False: 
                                        cases[casebatx][casebaty-1].attacked()
                                        essai=True
                                    elif cases[casebatx][casebaty-2].case_attaquee==False:
                                        cases[casebatx][casebaty-2].attacked()
                                        essai=True
                                    elif cases[casebatx][casebaty-3].case_attaquee==False: 
                                        cases[casebatx][casebaty-3].attacked()
                                        essai=True
                                    elif cases[casebatx][casebaty-4].case_attaquee==False: 
                                        cases[casebatx][casebaty-4].attacked()
                                        essai=True

                            else:
                                if cases[casebatx][casebaty+1].case_attaquee==False: 
                                    cases[casebatx][casebaty+1].attacked()
                                    essai=True
                                    if cases[casebatx][casebaty+1].bateau==False:
                                        direction="haut"
                                        
                                elif cases[casebatx][casebaty+2].case_attaquee==False: 
                                    cases[casebatx][casebaty+2].attacked()
                                    essai=True
                                    if cases[casebatx][casebaty+2].bateau==False:
                                        direction="haut"
                                        
                                elif cases[casebatx][casebaty+3].case_attaquee==False:
                                    cases[casebatx][casebaty+3].attacked()
                                    essai=True
                                    if cases[casebatx][casebaty+3].bateau==False:
                                        direction="haut"
                                        
                                elif cases[casebatx][casebaty+4].case_attaquee==False:
                                    cases[casebatx][casebaty+4].attacked()
                                    essai=True
                                    if cases[casebatx][casebaty+4].bateau==False:
                                        direction="haut"
                                        

                        except IndexError:
                            pass
            
            if sens=="horizontal":
                essai=False
                if ships[quel_bateau(cases[casebatx][casebaty])].bateau_en_vie()== 0:
                    sens="none"
                    direction="none"
                else:
                    while essai==False:
                        try:
                            if direction=="gauche":
                                while essai==False:
                                    if cases[casebatx-1][casebaty].case_attaquee==False:
                                        cases[casebatx-1][casebaty].attacked()
                                        essai=True
                                    elif cases[casebatx-2][casebaty].case_attaquee==False: 
                                        cases[casebatx-2][casebaty].attacked()
                                        essai=True
                                    elif cases[casebatx-3][casebaty].case_attaquee==False: 
                                        cases[casebatx-3][casebaty].attacked()
                                        essai=True
                                    elif cases[casebatx-4][casebaty].case_attaquee==False:
                                        cases[casebatx-4][casebaty].attacked()
                                        essai=True
                            else:
                                if cases[casebatx+1][casebaty].case_attaquee==False: 
                                    cases[casebatx+1][casebaty].attacked()
                                    essai=True
                                    if cases[casebatx+1][casebaty].bateau==False:
                                        direction="gauche"
                                        
                                elif cases[casebatx+2][casebaty].case_attaquee==False:
                                    cases[casebatx+2][casebaty].attacked()
                                    essai=True
                                    if cases[casebatx+2][casebaty].bateau==False:
                                        direction="gauche"
                                        
                                elif cases[casebatx+3][casebaty].case_attaquee==False:
                                    cases[casebatx+3][casebaty].attacked()
                                    essai=True
                                    if cases[casebatx+3][casebaty].bateau==False:
                                        direction="gauche"
                                        
                                elif cases[casebatx+4][casebaty].case_attaquee==False: 
                                    cases[casebatx+4][casebaty].attacked()
                                    essai=True
                                    if cases[casebatx+4][casebaty].bateau==False:
                                        direction="gauche"
                                        

                        except IndexError:
                            pass
                            
            if sens=="unknown":
                try:
                    essai=False
                    while essai==False:
                        random=ranai()
                        if cases[casebatx+1][casebaty].case_attaquee==True and cases[casebatx-1][casebaty].case_attaquee==True and cases[casebatx][casebaty+1].case_attaquee==True and cases[casebatx][casebaty-1].case_attaquee==True:
                            essai=True
                            a,b=rancoord()
                            while cases[a][b].case_attaquee==True:
                                a,b=rancoord()
                                cases[a][b].attacked()
                                sens="none"
                        elif random==1:
                            if cases[casebatx+1][casebaty].case_attaquee==False:
                                cases[casebatx+1][casebaty].attacked()
                                if cases[casebatx+1][casebaty].bateau==True:
                                    sens="horizontal"
                                else:
                                    sens="unknown"
                                essai=True
                                
                                
                        elif random==2:
                            if cases[casebatx-1][casebaty].case_attaquee==False:
                                cases[casebatx-1][casebaty].attacked()
                                if cases[casebatx-1][casebaty].bateau==True:
                                    sens="horizontal"
                                else:
                                    sens="unknown"
                                essai=True
                        elif random==3:
                            if cases[casebatx][casebaty+1].case_attaquee==False:    #probleme
                                cases[casebatx][casebaty+1].attacked()
                                if cases[casebatx][casebaty+1].bateau==True:
                                    sens="vertical"
                                else:
                                    sens="unknown"
                                essai=True
                        elif random==4:
                            if cases[casebatx][casebaty-1].case_attaquee==False:
                                cases[casebatx][casebaty-1].attacked()
                                essai==True
                                if cases[casebatx][casebaty-1].bateau==True:
                                    sens="vertical"
                                else:
                                    sens="unknown"
                                essai=True
                                
                except IndexError: 
                    pass
                
            elif sens=="none":   
                a,b=rancoord()
                while cases[a][b].case_attaquee==True:
                    a,b=rancoord()
                cases[a][b].attacked()
                essai=False
            
                if cases[a][b].bateau==True:
                    sens="unknown"
                    casebatx=a
                    casebaty=b
                        
        except IndexError:
            pass    
        
        


caseadversaire=[]
cases=[]
for i in range(10):
    cases.append([])
    caseadversaire.append([])
    for j in range(10):
        cases[i].append(case(i,j))
        caseadversaire[i].append(ai(i,j))
      

    
#================== Selectable boats ================================
boatframe=tk.Canvas(master, width=450, height=300)
boatframe.grid(column=1,row=0, sticky="N")

selectable=True #variable qui assure que seulement un bateau soit séléctionné à la fois
bl=0


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

nb_5=boatframe.create_text((l+320),(h-20), text='x 1')
nb_4=boatframe.create_text((l+290),(h+50), text='x 1')
nb_3=boatframe.create_text((l+260),(h+120), text='x 2')
nb_2=boatframe.create_text((l+230),(h+190), text='x 3')
 
compteur_b3=0
compteur_b2=0
   
def clicked_b5(event):
    global bl
    global selectable 
    if selectable==True:
        selectable=False
        print("Boat 5 selected")
        boatframe.itemconfigure(1, fill="grey")
        rotate_north(event)
        bl=5
        boatframe.itemconfigure(5, text='x 0')
    else: 
        print("Veuillez placer le bateau avant de selectionner un autre.")

def clicked_b4(event):
    global bl
    global selectable 
    if selectable==True:
        selectable=False
        print("Boat 4 selected")
        boatframe.itemconfigure(2, fill="grey")
        rotate_north(event)
        bl=4
        boatframe.itemconfigure(6, text='x 0')
    else: 
        print("Veuillez placer le bateau avant de selectionner un autre.")
def clicked_b3(event):
    global bl
    global selectable 
    global compteur_b3
    if selectable==True:
        print("Boat 3 selected")
        selectable=False
        if compteur_b3==0: 
            boatframe.itemconfigure(3, fill='#A9CCE3')
            boatframe.itemconfigure(7, text='x 1')
        elif compteur_b3==1:
            boatframe.itemconfigure(3, fill='grey')
            boatframe.itemconfigure(7, text='x 0')
        rotate_north(event)
        bl=3    
        compteur_b3=compteur_b3+1
    else: 
        print("Veuillez placer le bateau avant de selectionner un autre.")
def clicked_b2(event):
    global bl
    global selectable 
    global compteur_b2
    if selectable==True:
        print("Boat 2 selected")
        selectable=False
        if compteur_b2==0: 
            boatframe.itemconfigure(4, fill='#5DADE2')
            boatframe.itemconfigure(8, text='x 2')
        elif compteur_b2==1:
            boatframe.itemconfigure(4, fill='#A9CCE3')
            boatframe.itemconfigure(8, text='x 1')
        elif compteur_b2==2:
            boatframe.itemconfigure(4, fill='grey')
            boatframe.itemconfigure(8, text='x 0')        
        rotate_north(event)
        bl=2    
        compteur_b2=compteur_b2+1
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
    


#====================================================================
def quel_bateau(case):
    for i in range(len(ships)):
        for j in range(len(ships[i].endroits)):
            print(ships[i].endroits[j])
            if ships[i].endroits[j]==case:
                return i #ca te renvoie l'indice du bateau, genre cest le seul moyen de dire "quel bateau" cest
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

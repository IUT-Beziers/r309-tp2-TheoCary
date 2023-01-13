from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

root = Tk(); root.geometry( "1700x800" )
root.title("tkinter packet tracer")
c = Canvas( root, width = 1600, height = 700, bg = "white" ); c.pack()

### traçage de ligne


def ligne(event):
    color='black'
    x1, y1=(event.x-1),(event.y-1)
    x2, y2=(event.x+1),(event.y+1)
    c.create_oval(x1,y1,x2,y2, fill=color, outline=color)

c.bind("<B3-Motion>", ligne)

##### création d'une barre de tâche pour afficher les équipements réseaux

barre = Frame(root, bg='blue')    
barre.pack(fill=X)

##### Compression des images pour les faire apparaitre dans la barre

img9 = Image.open("routeur.png") 
image9=img9.resize((40,30))
uImg9 = ImageTk.PhotoImage(image9)            # utilisation de PIL

img10 = Image.open("switch.png")
image10=img10.resize((40,30))
uImg10 = ImageTk.PhotoImage(image10)

img11 = Image.open("pc.png")
image11=img11.resize((40,30))
uImg11 = ImageTk.PhotoImage(image11)

img12 = Image.open("telephone.png")
image12=img12.resize((40,30))
uImg12 = ImageTk.PhotoImage(image12)

img13 = Image.open("help.png")
image13=img13.resize((40,30))
uImg13 = ImageTk.PhotoImage(image13)

class barre1(Button):            # création d'une classe obligatoire pour utiliser grid
    def test(self):
        print("")

##### routeur

def apparition():                           # fait apparaitre l'image aux coordonnées choisis

    global image1
    c.create_image(100,200, image = image1)

global image1
image1 = PhotoImage(file ="routeur.png")  # modifie le bouton par l'image routeur

boutonR=barre1(barre, text= 'ROUTEUR', image=uImg9)
boutonR.grid(row=0, column=1)                               # place le bouton sur la barre
boutonR['command'] = apparition                             # appel de la fonction apparition 
              

##### pc
def apparition2():

    global image2
    c.create_image(100,200, image = image2)

global image2
image2 = PhotoImage(file = "pc.png")

boutonP=barre1(barre, text= 'PC',image=uImg11)
boutonP.grid(row=0, column=3)
boutonP['command'] = apparition2


##### switch
def apparition3():

    global image3
    c.create_image(100,200, image = image3)

global image3
image3 = PhotoImage(file = "switch.png")

boutonS=barre1(barre, text= 'SWITCH',image=uImg10)
boutonS.grid(row=0, column=2)
boutonS['command'] = apparition3


#### téléphone

def apparition4():

    global image4
    c.create_image(100,200, image = image4)

global image4
image4 = PhotoImage(file = "telephone.png")

boutonT=barre1(barre, text= 'TELEPHONE',image=uImg12)
boutonT.grid(row=0, column=4)
boutonT['command'] = apparition4

#### bouton reset

class reset1(Button):
    print("")

def reset():
    c.delete(ALL)

boutonReset=reset1(barre, text="RESET")
boutonReset.grid(row=0, column=9)
boutonReset['command'] = reset

#### Raccourci clavier (Control + lettre)


root.bind_all("<R>", lambda a: apparition()) # routeur
root.bind_all("<P>", lambda a: apparition2()) #pc 
root.bind_all("<S>", lambda a: apparition3()) #switch
root.bind_all("<T>", lambda a: apparition4()) #telephone

### bouton help 


def help():
    fen=Tk()
    fen.title("Aide")
    fen.geometry("800x50")
    texteLabel = Label(fen,
    text = "Pressez les touches maj + S, R, P, T pour faire apparître les items suivants : switch, routeur, pc et téléphone \n \n Utilisez le clic droit pour tracer une ligne entre les items")
    texteLabel.pack()
    fen.mainloop()

    #win= Toplevel(root, text="ouee") # test avec toplevel

boutonH=barre1(barre, text= 'HELP',image=uImg13)
boutonH.grid(row=0, column=8)
boutonH['command'] = help


### Deplacement des images

class MainFrame:
    
    def __init__( self, image2):
        self.__image2 = image2
        self.__x, self.__y = 250,250
        self.__picture0 = c.create_image( self.__x, self.__y,image =  self.__image2)
        self.__move = False
        c.bind( "<Button-1>", self.startMovement )
        c.bind( "<ButtonRelease-1>", self.stopMovement )
        c.bind( "<Motion>", self.movement )

    def startMovement( self, event ):
        self.__move = True
        self.initi_x = c.canvasx(event.x) 
        self.initi_y = c.canvasy(event.y) 
        #print('startMovement init', self.initi_x, self.initi_y)
        self.movingimage = c.find_closest(self.initi_x, self.initi_y, halo=5) # récupération de l'ID de l'objet canvas où se trouve le pointeur de la souris 
        #print(self.movingimage)
        #print(c.find_all()) 

    def stopMovement( self, event ):
        self.__move = False

    def movement( self, event ):
        if self.__move:
            end_x = c.canvasx(event.x) 
            end_y = c.canvasy(event.y) 
            # mise à jour avec une nouvelle localisation
            deltax = end_x - self.initi_x 
            deltay = end_y - self.initi_y
            self.initi_x = end_x 
            self.initi_y = end_y
            #print('movement init', self.initi_x, self.initi_y)
            c.move(self.movingimage, deltax, deltay) # déplacement de l'item 

if __name__ == "__main__":      
    img0=PhotoImage()
    MainFrame(img0)
    mainloop() 


root.mainloop()
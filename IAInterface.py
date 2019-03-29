from anytree import Node, RenderTree
from tkinter import *
 
from PIL import Image, ImageTk

B1= ["oie", "renard","foin"]
element=["oie", "renard","foin"]
B2= []
barque =[]
Etat=(barque, B1, B2)

def manger (x, y):
    if ( x== "renard" and y== "oie" ) or (y== "renard" and x== "oie" ):
        return True
    if ( x== "foin" and y== "oie" ) or (y== "foin" and x== "oie" ):
        return True
    return False 

def restSafe (B1):
    
    for k1 in B1:
        for k2 in B1:
            if (k1!= k2 and manger(k1, k2)):
                return False
    return True
        
def transporter(barque ,x, F):
    if (x in F):
        T = F.copy()
        T.remove(x)
        if len(barque)==0 and restSafe(T):
            barque.append(x)
            F.remove(x)
            return True

def parcourEnProfondeur(le):
    
    pile = []
     
    pile.append(e0)
    
    while (len(pile)!=0):
        node= pile.pop()
        
        le.append(node.name)
        if (EtatFianale(node.name)):
            print("---------------------------------------")
            break
        else:
            children = node.children
            i=0
            while (i < len(children)):
                pile.append(children[0])
                i=i+1
        
 


        

    
   
    
        
def passerA(barque,B):
    if len(barque)!=0:
        B.append(barque[0])
        barque.clear()

def EtatFianale(e):
    if (len(e[2])==3):
        return True
    return False 

def copy(etat):
    return( etat[0].copy(),etat[1].copy(),etat[2].copy())


def displaytree (node):
    for pre, fill, node in RenderTree(node):
        print("%s%s" % (pre, node.name))
    
def returnImaga(etat):
    b1 = etat[1]
    b2 = etat[2]
    bq= etat[0]
    if ( "oie" in b1 and "foin" in b1 and "renard" in b1):
        return "e0.JPG"
    if ( "oie" in bq and "foin" in b1 and "renard" in b1):
        return "e1.JPG"
    if ( "oie" in b2  and "foin" in b1 and "renard" in b1):
        return "e2.JPG"
    if ( "renard" in bq  and "foin" in b1 and "oie" in b2):
        return "e3.JPG"
    if ( "renard" in b2  and "foin" in b1 and "oie" in b2):
        return "e4.JPG"
    if ( "oie" in bq  and "foin" in b1 and "renard" in b2):
        return "e5.JPG"
    if ( "oie" in b1  and "foin" in b1 and "renard" in b2):
        return "e6.JPG"
    if ( "oie" in b1  and "foin" in bq and "renard" in b2):
        return "e7.JPG"
    if ( "oie" in b1  and "foin" in b2 and "renard" in b2):
        return "e8.JPG"
    if ( "oie" in bq  and "foin" in b2 and "renard" in b2):
        return "e9.JPG"
    if ( "oie" in b2  and "foin" in b2 and "renard" in b2):
        return "e10.JPG"

        
#print ("-------------Etat 0-------------")
e0= Node(copy(Etat))
#print ("-------------Etat 1-------------")
B=B1.copy()
for e in element :  
    transporter(barque,e ,B1)
e1=Node(copy(Etat), parent= e0 ,children=[])

#print ("-------------Etat 2-------------")
passerA(barque ,B2)
e2=Node(copy(Etat),  parent= e1 ,children=[] )

i=0
listEtat=[]
#print ("-------------Etat 3-------------")

for e in element :
    Bc1= B1.copy()
    Bc2= B2.copy()
    if transporter(barque,e ,Bc1) == True:
        Etat =(barque, Bc1,Bc2)
        e3=Node(copy(Etat),  parent= e2 ,children=[] )
        i=i+1
        passerA(barque , Bc2)
        e4=Node(copy(Etat),  parent= e3 ,children=[] )
        listEtat.append(e4)
        barque.clear()
j=0
t=""
for e in listEtat:
    Etat= copy(e.name)
    for i in Etat[2]:
        transporter(Etat[0],i, Etat[2])
        ei= Node(copy(Etat), parent= e)
        passerA(Etat[0],Etat[1])
        e= Node(copy(Etat), parent= ei)
        listEtat[j]=e
        j=j+1
        t= i
j=0

for e in listEtat:
    Etat= copy(e.name)
    for i in Etat[1]:
        if(i != t):
            transporter(Etat[0],i, Etat[1])
            ei= Node(copy(Etat), parent= e)
            passerA(Etat[0],Etat[2])
            e= Node(copy(Etat), parent= ei)
            listEtat[j]=e
            j=j+1
            t= i

j=0
t=""
for e in listEtat:
    Etat= copy(e.name)
     
    for i in Etat[1]:
            transporter(Etat[0],i, Etat[1])
            ei= Node(copy(Etat), parent= e)
            passerA(Etat[0],Etat[2])
            e= Node(copy(Etat), parent= ei)
            listEtat[j]=e
            j=j+1
            t= i

    



lE=[]
lt=[]
lt.append(1)
parcourEnProfondeur(lE)

def fNext():
    
    i=lt[0]
    lt.clear()
    i =i+1
    if( 11 <= i):
        i=10
    im = returnImaga(lE[i])
    path = "image/"+im
    print(i)
    root.photo = ImageTk.PhotoImage(Image.open(path))
    vlabel.configure(image=root.photo)
    
    lt.append(i)
    print ("updated")
    
    
def fPrivious():
    
    i=lt[0]
    lt.clear()
    i =i-1
    if (i < 0):
        i=0
    
    im = returnImaga(lE[i])
    path = "image/"+im
    print(i)
    root.photo = ImageTk.PhotoImage(Image.open(path))
    vlabel.configure(image=root.photo)
    lt.append(i)
    print ("updated")
    
root = tk.Tk()

photo = "image/e0.jpg"

root.photo = ImageTk.PhotoImage(Image.open(photo))


vlabel=tk.Label(image=root.photo)
vlabel.pack()

b2=tk.Button(root,text="Next",command=fNext)
b2.pack()
b3=tk.Button(root,text="Privious",command=fPrivious)
b3.pack()

root.mainloop()

 
root.mainloop()



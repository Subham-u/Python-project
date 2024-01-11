from tkinter import *
from PIL import Image ,ImageTk
import os
from time import strftime

#Main screen
screen=Tk()
screen.title('Subham Mahapatra Games')
#screen.iconbitmap('Icons//logo.ico')
screen.geometry('590x650+100+50')
screen.minsize(750,500)
screen.maxsize(750,500)
#screen.maxsize(590,650)


img = Image.open('/Users/subhammahapatra/Desktop/Project/mainback.jpg')
img = ImageTk.PhotoImage(img.resize((745,490)))

img1 = Image.open('/Users/subhammahapatra/Desktop/Project/f.png')
img1 = ImageTk.PhotoImage(img1.resize((80,80)))

img2 = Image.open('/Users/subhammahapatra/Desktop/Project/k.png')
img2 = ImageTk.PhotoImage(img2.resize((80,80)))

img3 = Image.open('/Users/subhammahapatra/Desktop/Project/icotic.png')
img3 = ImageTk.PhotoImage(img3.resize((100,100)))

label1 = Label(screen,image = img)
label1.place(x=0,y=0)

#commands
def ninja_game():
    os.system('python3 /Users/subhammahapatra/Desktop/Project/fruit_game/ninja.py')

def knife_fight():
    os.system('python3 /Users/subhammahapatra/Desktop/Project/Knife-Hit-PyGame-master/knife.py')

def tic_tac():
    os.system('python3 /Users/subhammahapatra/Desktop/Project/tic.py')



B1=Button(screen,image= img1 ,padx=10,pady=1,font=('Algerian',20) ,command=ninja_game)
B1.place(x=560,y=350)


B2=Button(screen,image= img2,padx=10,pady=1,font=('Algerian',20) ,command=knife_fight)
B2.place(x=100,y=350)

B3=Button(screen,image= img3,padx=10,pady=1,font=('Algerian',20) ,command=tic_tac)
B3.place(x=330,y=220)


def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)
  
# Styling the label widget so that clock
# will look more attractive
lbl = Label(screen, font = ('calibri', 25, 'bold'),
            background = 'red',
            foreground = 'white')
  
# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor = 'center')
lbl.place(x=285,y=150)
time()
#B3=Button(screen,text= 'ice ball',padx=53,pady=1,font=('Algerian',20) ,command=ice_ball)
#B3.place(x=400,y=350)

screen.configure()


screen.mainloop()
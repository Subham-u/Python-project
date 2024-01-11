from tkinter import *
from PIL import Image ,ImageTk
import os
from time import strftime
import socket
import threading

#Main screen
screen=Tk()
screen.title('Subham Mahapatra Games')
#screen.iconbitmap('Icons//logo.ico')
screen.geometry('590x650+100+50')
screen.minsize(750,500)
screen.maxsize(750,500)
#screen.maxsize(590,650)
hostname=socket.gethostname()
print(hostname)  
IPAddr=socket.gethostbyname(hostname)
print(IPAddr)
HOST=IPAddr

img = Image.open('/Users/subhammahapatra/Desktop/Project/ticback.jpg')
img = ImageTk.PhotoImage(img.resize((745,490)))

img1 = Image.open('/Users/subhammahapatra/Desktop/Project/icotic.png')
img1 = ImageTk.PhotoImage(img1.resize((100,100)))


label1 = Label(screen,image = img)
label1.place(x=0,y=0)

label2 = Label(screen,text = "HOST",font="/Users/subhammahapatra/Desktop/Project/fruit_game/comic.ttf")
label2.place(x=590,y=350)

label3 = Label(screen,text = "CLINT",font="/Users/subhammahapatra/Desktop/Project/fruit_game/comic.ttf")
label3.place(x=120,y=350)

label4 = Label(screen,text = "Id: "+HOST,font = ('calibri', 20, 'bold'),
            background = 'white',
            foreground = 'blue')
label4.place(x=275,y=130)



#commands
def host_game():
    os.system('python3 /Users/subhammahapatra/Desktop/Project/TicTacToe-main/server.py')

def clint_fight():
    os.system('python3 /Users/subhammahapatra/Desktop/Project/TicTacToe-main/client.py')



B1=Button(screen,image= img1 ,padx=10,pady=1,font=('Algerian',20) ,command=host_game)
B1.place(x=560,y=220)


B2=Button(screen,image= img1,padx=10,pady=1,font=('Algerian',20) ,command=clint_fight)
B2.place(x=100,y=220)

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)
  
# Styling the label widget so that clock
# will look more attractive
lbl = Label(screen, font = ('calibri', 25, 'bold'),
            background = 'blue',
            foreground = 'white')
  
# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor = 'center')
lbl.place(x=295,y=210)
time()

screen.configure()


screen.mainloop()
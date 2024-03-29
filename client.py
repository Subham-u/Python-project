import pygame
import os,sys
from grid_multi import Grid
import socket
import threading
import tkinter as tk
from PIL import Image ,ImageTk
import os

HOST = None

def get_ip():
    global HOST
    HOST = str(entry.get())
    screen.quit()

#Main screen
screen=tk.Tk()
screen.title('SMP Games')
#screen.iconbitmap('Icons//logo.ico')
screen.geometry('250x70+100+50')
screen.config(bg ='pink')
#screen.minsize(750,500)
screen.maxsize(750,500)
label1 = tk.Label(screen , text = 'ENTER friends ID:' ,bg ='pink')
label1.place (x=0,y=0)
entry = tk.Entry(screen )
entry.place(x=100 , y=0)
label2 = tk.Label(screen , text = 'ENTER friends ID:' ,bg ='pink')
label2.place (x=0,y=20)
entry1 = tk.Entry(screen )
entry1.place(x=100 , y=20)

button = tk.Button(screen , text = 'Connect' ,command = get_ip)
button.place(x=100 ,y=30)

screen.mainloop()

def create_thread(target):
    thread=threading.Thread(target=target)
    thread.daemon=True
    thread.start()


pygame.init()
#HOST='192.168.102.85'
PORT=9009

connection_established=False
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    sock.connect((HOST,PORT))
    connection_established=True
except :
    pass



surface=pygame.display.set_mode((600,630))
pygame.display.set_caption('Tic-Tac-Toe')

grid=Grid()
running=True
player="O"
turn=False
playing="True"

def receive_data():
    global turn,connection_established
    while True:
        try:
            data=sock.recv(1024).decode()
            data=data.split('-')
            x,y=int(data[0]),int(data[1])
            if data[2]=='Yourturn':
                turn=True
            if data[3] =="False":
                grid.game_over=True
            while playing!="True":
                pass        #busywait
            if grid.get_cell_value(x,y)==0:
                grid.set_cell_value(x,y,"X")
        except :
            print('Remote connection terminated')
            grid.clear_grid()
            connection_established=False
            grid.game_over=True
            break

create_thread(receive_data)

def status_bar():
    font = pygame.font.Font('/Users/subhammahapatra/Desktop/Project/TicTacToe-main/assets/04b19.ttf', 16)
    if not connection_established:
        whoturn ="Not connected to opponent-exit(escape)"
    elif grid.game_over:
        if grid.winner !=0:
            whoturn= " winner = " + player + " | press space to clear "
        else:
            whoturn="Game over | press space to clear"
    elif turn==True:
        whoturn="Your Turn" 
    else:
        whoturn="Opponent Turn"    
    text = font.render(f'Player O |  {whoturn}', True, (0,100,0),) 
    textRect = text.get_rect() 
    textRect.center = (300, 615)
    surface.blit(text, textRect)


while running and HOST != None:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running=False
            pygame.display.quit()
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not grid.game_over:
            if pygame.mouse.get_pressed()[0]:
                if turn and not grid.game_over:
                    pos = pygame.mouse.get_pos()
                    cellx,celly=pos[0]//200,pos[1]//200
                    grid.set_mouse_input(cellx,celly,player)
                    if grid.game_over:
                        playing="False"
                    send_data='{}-{}-{}-{}'.format(cellx,celly,'Yourturn',playing).encode()
                    sock.send(send_data)
                    turn=False

            if grid.game_over:
                print("Game over")

        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and grid.game_over:
                grid.clear_grid()
                grid.game_over=False
                playing="True"
                print("restart")
                if not connection_established:
                    grid.game_over=True

            elif event.key ==pygame.K_ESCAPE:
                running=False

    surface.fill((255,160,122))
    grid.draw(surface)
    status_bar()    
    pygame.display.flip()
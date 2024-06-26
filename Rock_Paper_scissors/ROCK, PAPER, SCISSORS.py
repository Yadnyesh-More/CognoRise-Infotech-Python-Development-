#Module import
import random 
from customtkinter import *
from PIL import Image
from tkinter.messagebox import askyesno
from tkinter import messagebox

#Window Declared
root = CTk()
root.geometry('800x700')
root.resizable(False,False)
root.title("Rock Paper Sciccor Game")
set_appearance_mode("Dark")

#Variables
comp_op = ('ROCK','PAPER',"SCICCORS")
user_var = StringVar()
comp_var = StringVar()
winner_var = StringVar()
uscore_var = IntVar()
cscore_var = IntVar()
round_var = IntVar()

global user_score ,comp_score,round_count
user_score = 0
comp_score = 0
round_count = 1
round_var.set(round_count)

#functions
def winner():
    global user_score ,comp_score

    if user_var.get() == comp_var.get():
        print("Tie !!!")
        winner_var.set('Tie !!!!')

    elif (user_var.get() == 'ROCK' and  comp_var.get() == 'SCICCORS') or \
        (user_var.get() == 'PAPER' and comp_var.get() == 'ROCK') or \
        (user_var.get() == 'SCICCORS' and comp_var.get() == 'PAPER'):
            print("user winner")
            winner_var.set('User Win !!!!')    
            user_score += 10
            uscore_var.set(user_score)

    else:
        print("Computer Win !!!")
        winner_var.set('Computer Win !!!!')
        comp_score += 10
        cscore_var.set(comp_score)

    if comp_score == 70 or user_score == 70:
        if comp_score == user_score:
            messagebox.showinfo('RESULT',"MATCH IS TIE !!!!!")
        elif user_score > comp_score:
            messagebox.showinfo('RESULT',"USER WIN MATCH !!!!!")
            restart()
        else:
            messagebox.showinfo('RESULT',"COMPUTER WIN MATCH !!!!!")
            restart()
        

def rock_choice():
    user_var.set('ROCK')
    comp_choice = random.choice(comp_op)
    comp_var.set(comp_choice)
    rock_but.configure(fg_color="red")
    rock_but.configure(state='disabled')
    paper_but.configure(state='disabled')
    sciccors_but.configure(state='disabled')
    round_but.configure(state="active")
    winner()


def paper_choice():
    user_var.set('PAPER')
    comp_choice = random.choice(comp_op)
    comp_var.set(comp_choice)
    paper_but.configure(fg_color="red")
    paper_but.configure(state='disabled')
    rock_but.configure(state='disabled')
    sciccors_but.configure(state='disabled')
    round_but.configure(state="active")
    winner()

def sciccors_choice():
    user_var.set('SCICCORS')
    comp_choice = random.choice(comp_op)
    comp_var.set(comp_choice)
    sciccors_but.configure(fg_color="red")
    sciccors_but.configure(state='disabled')
    rock_but.configure(state='disabled')
    paper_but.configure(state='disabled')
    round_but.configure(state="active")
    winner()

def nextround():
    global round_count
    round_count+=1
    round_var.set(round_count)
    rock_but.configure(state='active',fg_color='#7AB2B2')
    paper_but.configure(state='active',fg_color='#7AB2B2')
    sciccors_but.configure(state='active',fg_color='#7AB2B2')

    user_var.set('')
    comp_var.set('')
    winner_var.set('')
    round_but.configure(state="disabled")

def Exit():
    exit_game = askyesno(title='confirmation',message='Are you sure that you want to quit game?')

    if exit_game:
        root.destroy()

def restart():
    global user_score ,comp_score,round_count
    rock_but.configure(state='active',fg_color="#7AB2B2",text_color="Black",hover_color="#FF204E")
    paper_but.configure(state='active',fg_color="#7AB2B2",text_color="Black",hover_color="#FF204E")
    sciccors_but.configure(state='active',fg_color="#7AB2B2",text_color="Black",hover_color="#FF204E")

    user_var.set('')
    comp_var.set('')
    winner_var.set('')
    round_count= 1
    user_score = 0
    comp_score = 0 
    round_var.set(round_count)
    uscore_var.set(user_score)
    cscore_var.set(comp_score)

def gameloop():
    head.destroy()
    instruction.destroy()
    inst_lab.destroy()
    rules.destroy()
    rul_lab.destroy()
    next.destroy()
    note.destroy()
    note_lab.destroy()

    global rock_but,paper_but,sciccors_but,round_but

    heading = CTkLabel(root,text= "WELCOME TO ROCK PAPER SCICCOR GAME ",font=("Arieal", 20,"italic","bold","underline"))
    heading.place(x=190,y=10)

    round_lab = CTkLabel(root,text="Round :",font=("Arieal", 20, "bold","underline"))
    round_lab.place(x=15,y=50)

    round_ent = CTkEntry(root,textvariable=round_var,font=("Arieal", 18, "bold"),state="disabled",width=100)
    round_ent.place(x=100,y=50)

    choice = CTkLabel(root,text="Choice Any One : ",font=("Arieal", 20, "bold","underline"))
    choice.place(x=100,y=100)

    rock_but = CTkButton(root,text = "ROCK",font=("Arieal", 16, "bold"),fg_color="#7AB2B2",text_color="Black",hover_color="#FF204E",command=rock_choice)
    rock_but.place(x=310,y=100)

    paper_but = CTkButton(root,text = "PAPER",font=("Arieal", 15, "bold"),fg_color="#7AB2B2",text_color="Black",hover_color="#FF204E",command=paper_choice)
    paper_but.place(x=460,y=100)

    sciccors_but = CTkButton(root,text = "SCICCORS",font=("Arieal", 15, "bold"),fg_color="#7AB2B2",text_color="Black",hover_color="#FF204E",command=sciccors_choice)
    sciccors_but.place(x=610,y=100)

    user_img = CTkImage(light_image=Image.open("user.png"),size=(35,35))
    user = CTkLabel(root,text="",image=user_img)
    user.place(x=155,y=187)

    user_lab = CTkLabel(root,text="User Choice :",font=("Arieal", 15, "bold",'underline'),width=15)
    user_lab.place(x=200,y=190)

    vs_lab = CTkLabel(root,text="VS",font=("times",40,"bold","italic","underline"),text_color="#C6EBC5")
    vs_lab.place(x=370,y=190)

    comp_img = CTkImage(light_image=Image.open("computer-game.png"),size=(35,35))
    comp = CTkLabel(root,text="",image=comp_img)
    comp.place(x=455,y=187)

    computer_lab = CTkLabel(root,text="Computer Choice :",font=("Arieal", 15, "bold",'underline'),width=15)
    computer_lab.place(x=500,y=190)

    user_ent = CTkEntry(root,textvariable=user_var,font=("Arieal", 18, "bold"),state="disabled",width=150)
    user_ent.place(x=170,y=250)


    comp_ent = CTkEntry(root,textvariable=comp_var,font=("Arieal", 18, "bold"),state="disabled",width=150)
    comp_ent.place(x=490,y=250)

    score_lab = CTkLabel(root,text="SCORE : ",font=("Arieal", 16, "bold","underline"))
    score_lab.place(x=10,y=360)

    uscore_ent = CTkEntry(root,textvariable=uscore_var,font=("Arieal", 18, "bold"),state="disabled",width=150)
    uscore_ent.place(x=130,y=360)

    cscore_ent = CTkEntry(root,textvariable=cscore_var,font=("Arieal", 18, "bold"),state="disabled",width=150)
    cscore_ent.place(x=530,y=360)

    winner_lab = CTkLabel(root,text="WINNER !!",font=("Arieal", 16, "bold",'underline'))
    winner_lab.place(x=380,y=440)

    winner_res = CTkEntry(root,textvariable = winner_var,state="disabled",font=("Arieal", 18, "bold"),width=150)
    winner_res.place(x=340,y=480)

    round_but = CTkButton(root,text="Next Round",font=("Arieal", 16, "bold"),fg_color="#F99417",hover_color="#FFC470",command=nextround)
    round_but.place(x=340,y=540)

    exit_but = CTkButton(root,text="EXIT",font=("Arieal", 16, "bold"),command=Exit)
    exit_but.place(x=530,y=590)
        
    restart_but = CTkButton(root,text="RESTART",font=("Arieal", 16, "bold"),fg_color="#4F6F52",hover_color="#0A6847",text_color="black",command=restart)
    restart_but.place(x=150,y=590)  

#LABELS , BUTTON , HOMEPAGE 

head = CTkLabel(root,text= "WELCOME TO ROCK PAPER SCICCOR GAME ",font=("Arieal", 30, "bold"),bg_color="orange")
head.pack(fill=X,pady=5)

instruction = CTkLabel(root,text="INSTRUCTION :",font=("Arieal", 20, "bold","underline"))
instruction.place(x=10,y=70)

inst_lab = CTkLabel(root,text="\n1. Choose your move: At the start of each round, you will be prompted to choose your move between Rock, Paper, or Scissors. You can make your selection by clicking the name of your move in the window .\n\n2. Computer move: After you have made your selection, the computer will make its move. The result of the round will then be displayed on the screen .\n\n3. Repeat: The game continues for multiple rounds, and you can choose a different move each time if you wish if not then click same button. The player with the most wins at the end of the game is the winner.",bg_color="#40A578",text_color="black",wraplength=750,font=('CourierNew', 19))
inst_lab.place(x=30,y=110)

rules = CTkLabel(root,text="RULES :",font=("Arieal", 21, "bold","underline"))
rules.place(x=10,y=375)

rul_lab = CTkLabel(root,text="1. Rock beats Scissors\n\n2.Scissors beats Paper\n\n3. Paper beats Rock.",bg_color="#40A578",text_color="black",font=('arieal',20))
rul_lab.place(x=50,y=425)

note = CTkLabel(root,text="NOTE :",font=("Arieal", 20, "bold","underline"))
note.place(x=10,y=560)

note_lab = CTkLabel(root,text="The first player to reach a total of 100 ,will be the winner of the game.",bg_color="#40A578",text_color="black",font=('arieal',20))
note_lab.place(x=30,y=620,anchor='w')

next = CTkButton(root,text="NEXT ->",font=("Arieal", 16, "bold"),command=gameloop,fg_color="#5AB2FF")
next.place(x=630,y=660)

#WINDOW END 
root.mainloop()
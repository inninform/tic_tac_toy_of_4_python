import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tk_msg
import time
program = Tk()
program.title("player 1")
def replay():
    i = 0
    num = len(list_button)+1
    while i<num:
        list_button[i].config(text="",state=ACTIVE)
        i+=1
    var.set(1)

def winner_player1():
    winner_check = "XXXX"
    c1 = btn1.cget("text")
    c2 = btn2.cget("text")
    c3 = btn3.cget("text")
    c4 = btn4.cget("text")
    c5 = btn5.cget("text")
    c6 = btn6.cget("text")
    c7 = btn7.cget("text")
    c8 = btn8.cget("text")
    c9 = btn9.cget("text")
    c10 = btn10.cget("text")
    c11 = btn11.cget("text")
    c12 = btn12.cget("text")
    c13 = btn13.cget("text")
    c14 = btn14.cget("text")
    c15 = btn15.cget("text")
    c16 = btn16.cget("text")
    c17 = btn17.cget("text")
    c18 = btn18.cget("text")
    c19 = btn19.cget("text")
    c20 = btn20.cget("text")
    c21 = btn21.cget("text")
    c22 = btn22.cget("text")
    c23 = btn23.cget("text")
    c24 = btn24.cget("text")
    c25 = btn25.cget("text")
    n = 1
    if c1+c2+c3+c4==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c2+c3+c4+c5==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c6+c7+c8+c9==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c7+c8+c9+c10==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c11+c12+c13+c14==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c12+c13+c14+c15==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c16+c17+c18+c19==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c17+c18+c19+c20==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c21+c22+c23+c24==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c22+c23+c24+c25==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c1+c6+c11+c16==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c6+c11+c16+c21==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c2+c7+c12+c17==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c7+c12+c17+c22==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c3+c8+c13+c18==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c8+c13+c18+c23==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c4+c9+c14+c19==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c9+c14+c19+c24==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c5+c10+c15+c20==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c10+c15+c20+c25==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c1+c7+c13+c19==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c7+c13+c19+c25==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c5+c9+c13+c17==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c9+c13+c17+c21==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c2+c8+c14+c20==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c4+c8+c12+c16==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c10+c14+c18+c22==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c6+c12+c18+c24==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
def winner_player2():
    winner_check = "OOOO"
    c1 = btn1.cget("text")
    c2 = btn2.cget("text")
    c3 = btn3.cget("text")
    c4 = btn4.cget("text")
    c5 = btn5.cget("text")
    c6 = btn6.cget("text")
    c7 = btn7.cget("text")
    c8 = btn8.cget("text")
    c9 = btn9.cget("text")
    c10 = btn10.cget("text")
    c11 = btn11.cget("text")
    c12 = btn12.cget("text")
    c13 = btn13.cget("text")
    c14 = btn14.cget("text")
    c15 = btn15.cget("text")
    c16 = btn16.cget("text")
    c17 = btn17.cget("text")
    c18 = btn18.cget("text")
    c19 = btn19.cget("text")
    c20 = btn20.cget("text")
    c21 = btn21.cget("text")
    c22 = btn22.cget("text")
    c23 = btn23.cget("text")
    c24 = btn24.cget("text")
    c25 = btn25.cget("text")
    n = 2
    if c1+c2+c3+c4==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c2+c3+c4+c5==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c6+c7+c8+c9==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c7+c8+c9+c10==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c11+c12+c13+c14==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c12+c13+c14+c15==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c16+c17+c18+c19==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c17+c18+c19+c20==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c21+c22+c23+c24==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c22+c23+c24+c25==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c1+c6+c11+c16==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c6+c11+c16+c21==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c2+c7+c12+c17==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c7+c12+c17+c22==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c3+c8+c13+c18==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c8+c13+c18+c23==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c4+c9+c14+c19==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c9+c14+c19+c24==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c5+c10+c15+c20==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c10+c15+c20+c25==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c1+c7+c13+c19==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c7+c13+c19+c25==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c5+c9+c13+c17==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c9+c13+c17+c21==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c2+c8+c14+c20==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c4+c8+c12+c16==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c10+c14+c18+c22==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
    elif c6+c12+c18+c24==winner_check:
        tk_msg.showinfo(f" {n} the winner is the player {n}")
        replay()
def func_XO(index_list_button):
    if know() == 1:
        list_button[index_list_button].config(text="X",font=20,fg="red")
        var.set(0)
        program.title("player 2")
        winner_player1()
    elif know() == 0:
        list_button[index_list_button].config(text="O",font=20,fg="blue")
        var.set(1)
        program.title("player 1")
        winner_player2()
    list_button[index_list_button].config(state=DISABLED)

def know():
    #print(var.get())
    return var.get()
var = IntVar()
checkbox_Know = ttk.Checkbutton(program,variable=var,onvalue=True,offvalue=False)
checkbox_Know.grid(row=5,column=2,sticky='snew')
checkbox_Know.config(state=ACTIVE,command=know)
var.set(1)
var.get()
#print(var.get())

btn1 = Button(program,text='')
btn1.grid(row=0,column=0,ipadx=40,ipady=40,sticky='snew')
btn1.config(command=lambda v=0: func_XO(v))
btn2 = Button(program,text='')
btn2.grid(row=0,column=1,ipadx=40,ipady=40,sticky='snew')
btn2.config(command=lambda v=1: func_XO(v))
btn3 = Button(program,text='')
btn3.grid(row=0,column=2,ipadx=40,ipady=40,sticky='snew')
btn3.config(command=lambda v=2: func_XO(v))
btn4 = Button(program,text='')
btn4.grid(row=0,column=3,ipadx=40,ipady=40,sticky='snew')
btn4.config(command=lambda v=3: func_XO(v))
btn5 = Button(program,text='')
btn5.grid(row=0,column=4,ipadx=40,ipady=40,sticky='snew')
btn5.config(command=lambda v=4: func_XO(v))

btn6 = Button(program,text='')
btn6.grid(row=1,column=0,ipadx=40,ipady=40,sticky='snew')
btn6.config(command=lambda v=5: func_XO(v))
btn7 = Button(program,text='')
btn7.grid(row=1,column=1,ipadx=40,ipady=40,sticky='snew')
btn7.config(command=lambda v=6: func_XO(v))
btn8 = Button(program,text='')
btn8.grid(row=1,column=2,ipadx=40,ipady=40,sticky='snew')
btn8.config(command=lambda v=7: func_XO(v))
btn9 = Button(program,text='')
btn9.grid(row=1,column=3,ipadx=40,ipady=40,sticky='snew')
btn9.config(command=lambda v=8: func_XO(v))
btn10 = Button(program,text='')
btn10.grid(row=1,column=4,ipadx=40,ipady=40,sticky='snew')
btn10.config(command=lambda v=9: func_XO(v))

btn11 = Button(program,text='')
btn11.grid(row=2,column=0,ipadx=40,ipady=40,sticky='snew')
btn11.config(command=lambda v=10: func_XO(v))
btn12 = Button(program,text='')
btn12.grid(row=2,column=1,ipadx=40,ipady=40,sticky='snew')
btn12.config(command=lambda v=11: func_XO(v))
btn13 = Button(program,text='')
btn13.grid(row=2,column=2,ipadx=40,ipady=40,sticky='snew')
btn13.config(command=lambda v=12: func_XO(v))
btn14 = Button(program,text='')
btn14.grid(row=2,column=3,ipadx=40,ipady=40,sticky='snew')
btn14.config(command=lambda v=13: func_XO(v))
btn15 = Button(program,text='')
btn15.grid(row=2,column=4,ipadx=40,ipady=40,sticky='snew')
btn15.config(command=lambda v=14: func_XO(v))

btn16 = Button(program,text='')
btn16.grid(row=3,column=0,ipadx=40,ipady=40,sticky='snew')
btn16.config(command=lambda v=15: func_XO(v))
btn17 = Button(program,text='')
btn17.grid(row=3,column=1,ipadx=40,ipady=40,sticky='snew')
btn17.config(command=lambda v=16: func_XO(v))
btn18 = Button(program,text='')
btn18.grid(row=3,column=2,ipadx=40,ipady=40,sticky='snew')
btn18.config(command=lambda v=17: func_XO(v))
btn19 = Button(program,text='')#,command=lambda v=18: func_XO(v))
btn19.grid(row=3,column=3,ipadx=40,ipady=40,sticky='snew')
btn19.config(command=lambda v=18: func_XO(v))
btn20 = Button(program,text='')
btn20.grid(row=3,column=4,ipadx=40,ipady=40,sticky='snew')
btn20.config(command=lambda v=19: func_XO(v))

btn21 = Button(program,text='')
btn21.grid(row=4,column=0,ipadx=40,ipady=40,sticky='snew')
btn21.config(command=lambda v=20: func_XO(v))
btn22 = Button(program,text='')
btn22.grid(row=4,column=1,ipadx=40,ipady=40,sticky='snew')
btn22.config(command=lambda v=21: func_XO(v))
btn23 = Button(program,text='')
btn23.grid(row=4,column=2,ipadx=40,ipady=40,sticky='snew')
btn23.config(command=lambda v=22: func_XO(v))
btn24 = Button(program,text='')
btn24.grid(row=4,column=3,ipadx=40,ipady=40,sticky='snew')
btn24.config(command=lambda v=23: func_XO(v))
btn25 = Button(program,text='')
btn25.grid(row=4,column=4,ipadx=40,ipady=40,sticky='snew')
btn25.config(command=lambda v=24: func_XO(v))

list_button = [btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12,btn13,btn14,btn15,btn16,btn17,btn18,btn19,btn20,btn21,btn22,btn23,btn24,btn25]

lab_player1 = Label(program,text="player 1 : X")
lab_player1.grid(row=6,column=0)
lab_player1.config()
lab_player2 = Label(program,text="player 2 : O")
lab_player2.grid(row=6,column=4)
lab_player2.config()
replay_button = Button(program,text="replay")
replay_button.grid(row=7,column=2,sticky="snew",pady=40,padx=20)
replay_button.config(command=replay)
program.mainloop()
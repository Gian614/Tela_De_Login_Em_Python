from tkinter import *
import webbrowser
import time

def abrir_youtube():
    email = en_email.get()
    password = en_senha.get()
    
    
    if email == "teste@gmail.com" and password == "123456":
        webbrowser.open("https://www.youtube.com/watch?v=S9uPNppGsGo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0")
        master.destroy()
        time.sleep(0.3)
    else:
        
        messagebox.showerror("Error", "Invalid email or password")

def create_email():
    email = en_email.get()
   

def create_password():
    password = en_senha.get()
    

master = Tk()
master.title("Portal de alunos")
master.geometry("490x560+610+153")
master.iconbitmap(default="icones\\ico.ico")
master.resizable(width=1, height=1)

esconda_senha = StringVar()
img_fundo = PhotoImage(file="imagens\\fundo.png")
img_botao = PhotoImage(file="imagens\\LOGIN.png")

def new_func(master, img_fundo):
    Lab_fundo = Label(master, image=img_fundo)
    return Lab_fundo

Lab_fundo = new_func(master, img_fundo)
Lab_fundo.pack()

en_email = Entry(master, bd=2, font=("Calibri", 15), justify=CENTER)
en_email.place(width=425, height=85, x=32, y=155)

en_senha = Entry(master, textvariable=esconda_senha, show="*", bd=2, font=("Calibri", 15), justify=CENTER)
en_senha.place(width=425, height=85, x=32, y=320)

bt_entrar = Button(master, bd=0, image=img_botao, command=abrir_youtube)
bt_entrar.place(width=118, height=64, x=186, y=489)

bt_create_email = Button(master, text="teste@gmail.com", command=create_email)
bt_create_email.pack()

bt_create_password = Button(master, text="123456", command=create_password)
bt_create_password.pack()

master.mainloop()

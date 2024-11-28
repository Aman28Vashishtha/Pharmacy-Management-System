from tkinter import *
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import os


def main():
    app= Tk()
    ob= LoginPage (app)
    app.mainloop()

class LoginPage:
    def __init__(self,win):
        self.win =win 
        self.win.geometry ("1350x750")
        self.win.title("Pharmacy Management System | Login")

        self.title_lbl=Label(self.win,text ="Pharmacy Management System", bg="red",fg="yellow",bd=8,relief=GROOVE, font=("Arial",25,"bold"))
        self.title_lbl.pack(side=TOP,fill=X)

        self.login_lbl= Label (self.win,text ="Login", bg="blue",fg="yellow",bd=8,relief=GROOVE, font=("Arial",25,"bold"))
        self.login_lbl.pack(side=TOP,fill=X)

        self.main_frame= Frame(self.win,bg="lightgrey",bd=10,relief=RIDGE)
        self.main_frame.place(x=320,y=185,width=720,height=470)

        self.entry_frame= LabelFrame(self.main_frame, text="Enter Detail",bg="lightgrey",bd=8, relief=RIDGE,font=("Arial", 18))
        self.entry_frame.pack(side=TOP,fill=BOTH)

        #====================== Text Variables ===============#

        username=StringVar()
        password=StringVar()


        #=====================================================#

        self.username_lbl=Label(self.entry_frame,text="Username",font=("Arial",15),bg="lightgrey")
        self.username_lbl.grid(row=0,column=0,padx=2,pady=2)

        self.username_ent= Entry (self.entry_frame,border=9,textvariable= username,font=("Arial",15))
        self.username_ent.grid(row=0,column=1,padx=2,pady=2)

        self.password_lbl=Label(self.entry_frame,text="Password",font=("Arial",15),bg="lightgrey")
        self.password_lbl.grid(row=1,column=0,padx=2,pady=2)

        self.password_ent= Entry (self.entry_frame,border=9,textvariable= password,font=("Arial",15))
        self.password_ent.grid(row=1,column=1,padx=2,pady=2)

        self.fals_frame1= Frame(self.entry_frame, bd=0,bg="lightgrey")

        self.button_frame = LabelFrame(self.main_frame,text="Options",bg="lightgrey",bd=8,relief=RIDGE,font=("Arial",18))
        self.button_frame.pack(side=TOP,fill=BOTH)

        self.dum1_lbl= Label(self.button_frame, text="", bg="lightgrey")
        self.dum1_lbl.grid(row=0,column=1,padx=10)

        #=========== Functions ================#

        def run_program():
            os.system('main.py')

        def submit_func():
            if username.get()=="" or password.get()=="":
                pass
            else:
                print("Wrong Credentials")
        
        def reset_func():
            username.set("")
            password.set("")

        def exit_func():
            sef.win.destroy()

        #======================================#
        

        #=================Buttons==============#

        self.submit_btn=Button(self.button_frame,text="Submit",border=8,font=("Arial",15),width=15,command=run_program)
        self.submit_btn.grid(row=0,column=1,padx=8,pady=4)

        self.reset_btn=Button(self.button_frame,text="Reset",border=8,font=("Arial",15),command=reset_func)
        self.reset_btn.grid(row=0,column=2,padx=8,pady=6)

        self.exit_btn=Button(self.button_frame,text="Reset",border=8,font=("Arial",15),command=exit_func)
        self.exit_btn.grid(row=0,column=3,padx=8,pady=6)
        
        #=======================================#




if __name__== "__main__":
    main()

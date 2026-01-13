from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from attendance import Attendance
from face_recognition import Face_Recognition




class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("face Recognition System")

        title_label=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="skyblue")
        title_label.place(x=0,y=0,width=1530,height=48)

        img_top=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\bg3.jpg")
        img_top=img_top.resize((1530,720), Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_label=Label(self.root,image=self.photoimg_top)
        f_label.place(x=0,y=55,width=1530,height=720)

# ======================================================================================================frame
        main_frame = Frame(f_label,bg="white",bd=2)
        main_frame.place(x=500,y=0,width=500,height=600)


        img_top1=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\shariqua.jpg")
        img_top1=img_top1.resize((200,200), Image.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_label=Label(main_frame,image=self.photoimg_top1)
        f_label.place(x=300,y=0,width=200,height=200)

# =================================================================================================================developer
        dev1_label=Label(main_frame,text="hello !! my name is Shariqua",font=("times new roman",18,"bold"),bg="white")
        dev1_label.place(x=0,y=5)
        dev2_label=Label(main_frame,text="DBATU Computer Engineering Student\n This is my Seminar Project for 2nd year\nMy guide name is Prof.Pramod Patil",font=("times new roman",13,"bold"),bg="white")
        dev2_label.place(x=0,y=40)

        # ==============================================================================================
        img2=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\loginBg.jpg")
        img2=img2.resize((500,300), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_label=Label(main_frame,image=self.photoimg2)
        f_label.place(x=0,y=210,width=500,height=300)








if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
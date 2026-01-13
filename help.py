from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
from train import Train
from attendance import Attendance
from face_recognition import Face_Recognition




class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("face Recognition System")

        title_label=Label(self.root,text="Help Desk",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_label.place(x=0,y=0,width=1530,height=55)

        img_top=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\img__1.jpg")
        img_top=img_top.resize((1530,720), Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_label=Label(self.root,image=self.photoimg_top)
        f_label.place(x=0,y=55,width=1530,height=720)

        dev1_label=Label(f_label,text="Email:khanshariqua1020@gmail.com",font=("times new roman",20,"bold"),bg="white")
        dev1_label.place(x=550,y=300)


if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os
import tkinter
from time import strftime
from datetime import datetime
from train import Train
from attendance import Attendance
from face_recognition import Face_Recognition
from developer import Developer
from help import Help




class face_recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("face Recognition System")


        #1st
        img=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\u.jpg")
        img=img.resize((500,130), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_label=Label(self.root,image=self.photoimg)
        f_label.place(x=0,y=0,width=500,height=130)
        #2nd
        img1=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\unnamed.jpg")
        img1=img1.resize((500,130), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=500,y=0,width=500,height=130)
        #3rd
        img2=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\university.jpg")
        img2=img2.resize((500,130), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_label=Label(self.root,image=self.photoimg2)
        f_label.place(x=1000,y=0,width=550,height=130)


        #for bg
        img3=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\bg.jpg")
        img3=img3.resize((1530,710), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_label=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_label.place(x=0,y=0,width=1530,height="130")

        # ======================================================================================
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)
        lbl=Label(title_label,font=("times new roman",14,'bold'),background="white",fg="blue")
        lbl.place(x=0,y=0,width=110,height=50)
        time()


        #stu btn
        img4=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\gettyimages-1022573162.jpg")
        img4=img4.resize((220,220), Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="black")
        b1_1.place(x=200,y=300,width=220,height=40)

        #detect face
        img5=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\f_det.jpg")
        img5=img5.resize((220,220), Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face detector",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="black",command=self.face_data)
        b1_1.place(x=500,y=300,width=220,height=40)

        #attendance
        img6=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\attendence1.jpeg")
        img6=img6.resize((220,220), Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="black",command=self.attendance_data)
        b1_1.place(x=800,y=300,width=220,height=40)

        #help
        img7=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\helpdesk.jpg")
        img7=img7.resize((220,220), Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="black",command=self.help_data)
        b1_1.place(x=1100,y=300,width=220,height=40)

        #train
        img8=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\Train.jpg")
        img8=img8.resize((220,220), Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="blue",fg="black")
        b1_1.place(x=200,y=580,width=220,height=40)

        #photo
        img9=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\sample.jpg")
        img9=img9.resize((220,220), Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="black")
        b1_1.place(x=500,y=580,width=220,height=40)

        #developer
        img10=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\dev.jpg")
        img10=img10.resize((220,220), Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="black",command=self.developer_data)
        b1_1.place(x=800,y=580,width=220,height=40)

        #exit
        img11=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\exi.jpg")
        img11=img11.resize((220,220), Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="black",command=self.iExit)
        b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile(r"C:\Users\Lenovo\Desktop\new--pro\ImagesOfFaces")

    # ===============================================================================================
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("face Recognition","Do you want to exit this window",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

        #=================function button=========================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)
        







       
 




    





if __name__ == "__main__":
    root=Tk()
    obj=face_recognition_system(root)
    root.mainloop()

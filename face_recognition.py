from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np
import os
from time import strftime
from datetime import datetime
import csv


class Face_Recognition:
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x710+0+0")
        self.root.title("Face Recognition System")
        self.face_data=[]

        title_label = Label(self.root, text="Face Recognition", font=("times new roman", 35, "bold"), bg="white", fg="navyblue")
        title_label.place(x=0, y=0, width=1530, height=53)

        img_top = Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\face_detector1.jpg")
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_label = Label(self.root, image=self.photoimg_top)
        f_label.place(x=0, y=55, width=650, height=700)

        img_left = Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\face1.jpg")
        img_left = img_left.resize((950, 700), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_label = Label(self.root, image=self.photoimg_left)
        f_label.place(x=650, y=55, width=950, height=700)

        b1_1 = Button(f_label, text="Face Recognition", cursor="hand2", font=("times new roman", 18, "bold"), bg="white", fg="navyblue", command=self.face_recog)
        b1_1.place(x=360, y=620, width=200, height=40)
# =======================================================================
    def mark_attendance(self,i,r,n,d):
        with open(r"C:\Users\Lenovo\Desktop\new--pro\Attendance_1.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]

            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%month/%Y")
                dtString=now.strftime("%H:%m:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},present")






    # =============================================================================
    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, color, text, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

        coord = []

        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)

            id, predict = clf.predict(gray_image[y:y + h, x:x + w])
            confidence = int((100 * (1 - predict / 300)))

            conn = mysql.connector.connect(host="localhost", username="root", password="shariquak$789", database="face_recognizer")
            my_cursor = conn.cursor()

            my_cursor.execute("select student_id from student where student_id=" + str(id))
            i = my_cursor.fetchone()
            i = "+".join(i) if i else "Unknown"

            my_cursor.execute("select name from student where student_id=" + str(id))
            n = my_cursor.fetchone()
            n = "+".join(n) if i else "Unknown"

            my_cursor.execute("select roll_no from student where student_id=" + str(id))
            r = my_cursor.fetchone()
            r = "+".join(r) if r else "Unknown"

            my_cursor.execute("select dep from student where student_id=" + str(id))
            d = my_cursor.fetchone()
            d = "+".join(d) if d else "Unknown"

            if confidence > 70:
                cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                self.mark_attendance(i,r,n,d)
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, "Unknown face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

            coord = [x, y, w, h]

        return coord

    def recognize(self, img, clf, faceCascade):
        coord = self.draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
        return img

    def face_recog(self):
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\Users\Lenovo\Desktop\new--pro\classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                messagebox.showerror("Error", "Failed to access the camera")
                break

            img = self.recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to DBATU", img)

            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()



















# from tkinter import*
# from tkinter import ttk
# from PIL import Image,ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2
# import sys
# import dlib
# import numpy as np
# import os



# class Face_Recognition_s:
#     def __init__(self,root):
#         self.root=root
#         self.root.geometry("1530x710+0+0")
#         self.root.title("face Recognition System")

#         title_label=Label(self.root,text="Face Recognition",font=("times new roman",35,"bold"),bg="white",fg="navyblue")
#         title_label.place(x=0,y=0,width=1530,height=53)

#         img_top=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\face_detector1.jpg")
#         img_top=img_top.resize((650,700), Image.LANCZOS)
#         self.photoimg_top=ImageTk.PhotoImage(img_top)

#         f_label=Label(self.root,image=self.photoimg_top)
#         f_label.place(x=0,y=55,width=650,height=700)

#         img_left=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\face1.jpg")
#         img_left=img_left.resize((950,700), Image.LANCZOS)
#         self.photoimg_left=ImageTk.PhotoImage(img_left)

#         f_label=Label(self.root,image=self.photoimg_left)
#         f_label.place(x=650,y=55,width=950,height=700)

#         b1_1=Button(f_label,text="Face Recognition",cursor="hand2",font=("times new roman",18,"bold"),bg="white",fg="navyblue")
#         b1_1.place(x=360,y=620,width=200,height=40)

#         # ===================================================face recognition

#         def face_recog(self):
#             def draw_boundry(img,classifier,ScaleFactor,minNeighbors,color,text,clf):
#                 gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#                 features=classifier.detectMultiScale(gray_image,ScaleFactor,minNeighbors)

#                 coord=[]

#                 for (x,y,w,h) in features:
#                     cv2.rectangle(img(x,y),(x+w,y+h),(0,255,0),3)

#                     id,predict=clf.predict(gray_image[y:y+h,x:x+w])
#                     confidence=int((100*(1-predict/300)))

#                     conn=mysql.connector.connect(host="localhost",username="root",password="shariquak$789",database="face_recognizer")
#                     my_cursor=conn.cursor()
#                     my_cursor.execute("select name from student where student_id="+str(id))
#                     i=my_cursor.fetchone()
#                     i="+".join(i)

#                     my_cursor.execute("select roll_no from student where student_id="+str(id))
#                     r=my_cursor.fetchone()
#                     r="+".join(r)

#                     my_cursor.execute("select dep from student where student_id="+str(id))
#                     d=my_cursor.fetchone()
#                     d="+".join(d)

#                     if confidence>77:
#                         cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                         cv2.putText(img,f"Name:{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                         cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                     else:
#                         cv2.rectangle(img(x,y),(x+w,y+h),(0,0,255),3)
#                         cv2.putText(img,"Unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
#                     coord=[x,y,w,h]

#                 return coord

#             def recognize(img,clf,faceCascade):
#                 coord=draw_boundry(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
#                 return img

#             faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#             clf=cv2.face.LBPHFaceRecognizer_create()
#             clf.read(r"C:\Users\Lenovo\Desktop\new--pro\classifier.xml")


#             video_cap=cv2.VideoCapture(0)

#             while True:
#                 ret,img=video_cap.read()
#                 img=recognize(img,clf,faceCascade)
#                 cv2.imshow("welcome to DBATU",img)

#                 if cv2.waitKey(1)==13:
#                     break
#                 video_cap.release()
#                 cv2.destroyAllWindows()
                



# if __name__ == "__main__":
#     root=Tk()
#     obj=Face_Recognition_s(root)
#     root.mainloop()
# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2
# import dlib
# import numpy as np
# import os

# class Face_Recognition_s:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x710+0+0")
#         self.root.title("Face Recognition System")

#         title_label = Label(self.root, text="Face Recognition", font=("times new roman", 35, "bold"), bg="white", fg="navyblue")
#         title_label.place(x=0, y=0, width=1530, height=45)

#         # Add additional GUI components here
#         # Example: A frame to contain buttons
#         self.main_frame = Frame(self.root, bd=2, bg="white")
#         self.main_frame.place(x=20, y=60, width=1480, height=620)

#         # Example: Button to start face recognition
#         self.recog_btn = Button(self.main_frame, text="Start Face Recognition", command=self.face_recognition, font=("times new roman", 20, "bold"), bg="navyblue", fg="white")
#         self.recog_btn.place(x=10, y=10, width=300, height=50)

#         # Example: Display area for results
#         self.result_label = Label(self.main_frame, text="Results:", font=("times new roman", 20, "bold"), bg="white", fg="black")
#         self.result_label.place(x=10, y=70, width=200, height=50)
        
#     def connect_db(self):
#         # Establish connection to the MySQL database
#         try:
#             self.conn = mysql.connector.connect(
#                 host="localhost",
#                 user="root",
#                 password="shariquak$789",
#                 database="face_recognizer"
#             )
#             self.cursor = self.conn.cursor()
#             messagebox.showinfo("Success", "Connected to the database successfully")
#         except mysql.connector.Error as err:
#             messagebox.showerror("Error", f"Error connecting to the database: {err}")

#     def face_recognition(self):
#         # Add face recognition code here
#         pass

# if __name__ == "__main__":
#     root = Tk()
#     obj = Face_Recognition_s(root)
#     root.mainloop()

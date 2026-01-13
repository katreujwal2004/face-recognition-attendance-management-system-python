from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import sys
import dlib
import numpy as np
from train import Train


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("face Recognition System")



        #====================variable===================
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_roll_no=StringVar()
        self.var_id=StringVar()
        self.var_div=StringVar()
        self.var_gen=StringVar()
        self.var_dob=StringVar()
        self.var_dep=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_photo=StringVar()
        


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

        title_label=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_label.place(x=0,y=0,width=1530,height=45)

        main_frame = Frame(bg_img,bg="white",bd=2)
        main_frame.place(x=10,y=55,width=1500,height=600)


        #left label frame

        Left_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        
        img_l=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\university.jpg")
        img_l=img_l.resize((720,130), Image.LANCZOS)
        self.photoimg_l=ImageTk.PhotoImage(img_l)

        f_label=Label(Left_frame,image=self.photoimg_l)
        f_label.place(x=5,y=0,width=720,height=130)

        #current course info
        current_course=LabelFrame(Left_frame,bg="white",bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course.place(x=5,y=135,width=720,height=115)


        #department
        dep_label=Label(current_course,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("select department","computer","information technology","civil engineering","electrical engineering","mechenical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        #course
        course_label=Label(current_course,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("select course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("select year","2024","2025","2026","2027")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_course,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course,textvariable=self.var_sem,font=("times new roman",12,"bold"),width=17,state="readonly")
        semester_combo["values"]=("select semester","1","2","3","4","5","6")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)



        #class student information
        class_student=LabelFrame(Left_frame,bg="white",bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student.place(x=5,y=250,width=720,height=300)

        #student id
        studentId_label=Label(class_student,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentId_entry=ttk.Entry(class_student,textvariable=self.var_id,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,sticky=W)

        #student name
        student_name_label=Label(class_student,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_student,textvariable=self.var_name,width=20,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class div
        class_div_label=Label(class_student,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student,textvariable=self.var_div,font=("times new roman",12,"bold"),width=18,state="readonly")
        div_combo["values"]=("A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # class_div_entry=ttk.Entry(class_student,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll no
        rollNo_label=Label(class_student,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        rollNo_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollNo_entry=ttk.Entry(class_student,textvariable=self.var_roll_no,width=20,font=("times new roman",12,"bold"))
        rollNo_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #gender
        gender_label=Label(class_student,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gen_combo=ttk.Combobox(class_student,textvariable=self.var_gen,font=("times new roman",12,"bold"),width=18,state="readonly")
        gen_combo["values"]=("FEMALE","MALE","OTHER")
        gen_combo.current(0)
        gen_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # gender_entry=ttk.Entry(class_student,textvariable=self.var_gen,width=20,font=("times new roman",12,"bold"))
        # gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


        #dob
        dob_label=Label(class_student,text="Date Of Birth:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email
        emailId_label=Label(class_student,text="Email ID:",font=("times new roman",12,"bold"),bg="white")
        emailId_label.grid(row=3,column=00,padx=10,pady=5,sticky=W)

        emailId_entry=ttk.Entry(class_student,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        emailId_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone no
        phone_no_label=Label(class_student,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_no_entry=ttk.Entry(class_student,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
        address_label=Label(class_student,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        adress_entry=ttk.Entry(class_student,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        adress_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        #teacher
        teacher_label=Label(class_student,text="Teacher:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buton
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(class_student,variable=self.var_radio1,text="take a photo sample",value="Yes")
        radiobutton1.grid(row=6,column=0)

        radiobutton2=ttk.Radiobutton(class_student,variable=self.var_radio1,text="No photo sample",value="No")
        radiobutton2.grid(row=6,column=1)

        #button frame
        btn_frame=Frame(class_student,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=715,height=70)

        save_button=Button(btn_frame,text="SAVE",command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_button.grid(row=0,column=0)

        update_button=Button(btn_frame,text="Update",width=19,font=("times new roman",12,"bold"),bg="blue",fg="white",command=self.update_data)
        update_button.grid(row=0,column=1)

        delete_button=Button(btn_frame,text="DELETE",width=19,font=("times new roman",12,"bold"),bg="blue",fg="white",command=self.delete_data)
        delete_button.grid(row=0,column=2)

        reset_button=Button(btn_frame,text="RESET",width=19,font=("times new roman",12,"bold"),bg="blue",fg="white",command=self.reset_data)
        reset_button.grid(row=0,column=3)

        take_photo_button=Button(btn_frame,text="Take  Photo",command=self.generate_dataset,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_button.grid(row=1,column=1)

        update_photo_button=Button(btn_frame,text="Update Photo",width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_button.grid(row=1,column=2)


        #right label frame

        right_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        img_r=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\banner.jpg")
        img_l=img_r.resize((720,130), Image.LANCZOS)
        self.photoimg_r=ImageTk.PhotoImage(img_r)

        f_label=Label(right_frame,image=self.photoimg_r)
        f_label.place(x=5,y=0,width=720,height=130)

        #==========================search system============================================

        search_frame=LabelFrame(right_frame,bg="white",bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo["values"]=("select","Roll_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_button=Button(search_frame,text="Search",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_button.grid(row=0,column=3,padx=4)

        showAll_button=Button(search_frame,text="show all",width=13,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_button.grid(row=0,column=4)

        #===================table frame=====================================
        table_frame=Frame(right_frame,bg="white",bd=2,relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,columns=("name","course","year","sem","roll_no","id","division","gen","dob","dep","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("name",text="Name",)
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semeter")
        self.student_table.heading("roll_no",text="Roll_No")
        self.student_table.heading("id",text="Student_ID")
        self.student_table.heading("division",text="Division")
        self.student_table.heading("gen",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("email",text="EMAIL")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("name",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("roll_no",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("division",width=100)
        self.student_table.column("gen",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("dep",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        self.reset_data()
        # self.update_data()
        

    #================func declare===============
    def add_data(self):
        if self.var_name.get()=="" or self.var_dep.get()=="select department" or self.var_course.get()=="select course" or self.var_year.get()=="select year" or self.var_sem.get()=="select semester" or self.var_id.get()=="" or self.var_div.get()=="" or self.var_roll_no.get()=="" or self.var_gen.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="shariquak$789",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_name.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_sem.get(),
                                                                                                                self.var_roll_no.get(),
                                                                                                                self.var_id.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_gen.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_photo.get()
                                                                                                                ))                                                                                                               
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student Detail has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
 # ===========================Fetch data form database to table ================================

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="shariquak$789",database="face_recognizer")
        mycursor = conn.cursor()

        mycursor.execute("select * from student")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

         #================================get cursor function=======================

    def get_cursor(self, event=""):
    # Get the cursor focus from the student_table
        cursor_focus = self.student_table.focus()

    # Retrieve content (values) of the selected row
        content = self.student_table.item(cursor_focus)
        data = content["values"]

    # Update tkinter variables with the retrieved data
        (self.var_name.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_roll_no.set(data[4]),
        self.var_id.set(data[5]),
        self.var_div.set(data[6]),
        self.var_gen.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_dep.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14]))

    # def get_cursor(self,event=""):
    #     cursor_focus = self.student_table.focus()
    #     content = self.student_table.item(cursor_focus)
    #     data = content["values"]

    #     self.var_name.set(data[0]),
    #     self.var_course.set(data[1]),
    #     self.var_year.set(data[2]),
    #     self.var_sem.set(data[3]),
    #     self.var_roll_no.set(data[4]),
    #     self.var_id.set(data[5]),
    #     self.var_div.set(data[6]),
    #     self.var_gen.set(data[7]),
    #     self.var_dob.set(data[8]),
    #     self.var_dep.set(data[9]),
    #     self.var_email.set(data[10]),
    #     self.var_phone.set(data[11]),
    #     self.var_address.set(data[12]),
    #     self.var_teacher.set(data[13]),
    #     self.var_radio1.set(data[14])
# ========================================Update Function==========================
    # def update_data1(self):
    #     if self.var_name.get()=="" or self.var_dep.get()=="select department" or self.var_course.get()=="select course" or self.var_year.get()=="select year" or self.var_sem.get()=="select semester" or self.var_id.get()=="" or self.var_div.get()=="" or self.var_roll_no.get()=="" or self.var_gen.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
    #         messagebox.showerror("Error","All Fields are required",parent=self.root)


    #     else:
    #         try:
    #             Update=messagebox.askyesno("Update","Do you want to update student details!!",parent=self.root)
    #             if Update>0:
    #                 conn=mysql.connector.connect(host="localhost",user="root",password="shariquak$789",database="face_recognizer")
    #                 my_cursor=conn.cursor()
    #                 my_cursor.execute("update student set name=%s,course=%s,year=%s,sem=%s,roll_no=%s,id=%s,")                                                                                                               
    #             conn.commit()
    #             self.fetch_data()
    #             conn.close()



    def update_data(self):
        if self.var_name.get()=="" or self.var_dep.get()=="select department" or self.var_course.get()=="select course" or self.var_year.get()=="select year" or self.var_sem.get()=="select semester" or self.var_id.get()=="" or self.var_div.get()=="" or self.var_roll_no.get()=="" or self.var_gen.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="" or self.var_phone.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Details!",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="shariquak$789",database="face_recognizer")
                    mycursor=conn.cursor()
                    mycursor.execute('update student set name=%s,course=%s,year=%s,sem=%s,roll_no=%s,division=%s,gen=%s,dob=%s,dep=%s,email=%s,phone=%s,address=%s,teacher=%s,photo=%s where student_id=%s',( 
                                                                                                                                                                                    self.var_name.get(),
                                                                                                                                                                                    self.var_course.get(),
                                                                                                                                                                                    self.var_year.get(),
                                                                                                                                                                                    self.var_sem.get(),
                                                                                                                                                                                    self.var_roll_no.get(),
                                                                                                                                                                                    self.var_div.get(),
                                                                                                                                                                                    self.var_gen.get(),
                                                                                                                                                                                    self.var_dob.get(),
                                                                                                                                                                                    self.var_dep.get(),
                                                                                                                                                                                    self.var_email.get(),
                                                                                                                                                                                    self.var_phone.get(),
                                                                                                                                                                                    self.var_address.get(),
                                                                                                                                                                                    self.var_teacher.get(),
                                                                                                                                                                                    self.var_radio1.get(),
                                                                                                                                                                                    self.var_id.get()   
                                                                                                                                                                                                ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
     #==============================Delete Function=========================================
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="shariquak$789",database="face_recognizer")
                    mycursor = conn.cursor() 
                    sql="delete from student where student_id=%s"
                    val=(self.var_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 
    # Reset Function 
    def reset_data(self):
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_dep.set("select department"),
        self.var_course.set("select course"),
        self.var_year.set("select year"),
        self.var_sem.set("select semester"),
        self.var_div.set(""),
        self.var_gen.set("female"),
        self.var_dob.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_roll_no.set(""),
        self.var_email.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
    # ===========================Search Data===================
    # def search_data(self):
    #     if self.var_roll_no.get()=="":
    #         messagebox.showerror("Error","Select Combo option and enter entry box",parent=self.root)
    #     else:
    #         try:
    #             conn = mysql.connector.connect(host="localhost",username="root",password="shariquak$789",database="face_recognizer")
    #             my_cursor = conn.cursor()
    #             sql = "SELECT student_id name course year sem division gen dob dep email phone address teacher photo FROM student where roll_no=" +str(self.var_roll_no.get()) + "'" 
    #             my_cursor.execute(sql)
    #             #my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
    #             rows=my_cursor.fetchall()        
    #             if len(rows)!=0:
    #                 self.student_table.delete(*self.student_table.get_children())
    #                 for i in rows:
    #                     self.student_table.insert("",END,values=i)
    #                 if rows==None:
    #                     messagebox.showerror("Error","Data Not Found",parent=self.root)
    #                     conn.commit()
    #                     conn.close()
    #         except Exception as es:
    #             messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



    # def generate_dataset(self):
    #     # Check if all required fields are filled
    #     if (self.var_name.get()=="" or self.var_dep.get()=="select department" or 
    #         self.var_course.get()=="select course" or self.var_year.get()=="select year" or 
    #         self.var_sem.get()=="select semester" or self.var_id.get()=="" or 
    #         self.var_div.get()=="" or self.var_roll_no.get()=="" or 
    #         self.var_gen.get()=="" or self.var_dob.get()=="" or 
    #         self.var_email.get()=="" or self.var_address.get()=="" or 
    #         self.var_teacher.get()=="" or self.var_phone.get()==""):
        
    #         messagebox.showerror("Error","All Fields are required",parent=self.root)
    #     else:
    #         try:
    #             # Connect to MySQL
    #             conn = mysql.connector.connect(host="localhost",username="root",password="shariquak$789",database="face_recognizer")
    #             my_cursor = conn.cursor()

    #             # Fetch the highest student_id from the database and increment it by 1 to get the next student_id
    #             my_cursor.execute("SELECT MAX(student_id) FROM student")
    #             id = my_cursor.fetchone()[0] or 0
    #             id += 1

    #             # Update student information in the database
    #             my_cursor.execute('''UPDATE student SET name=%s, course=%s, year=%s, sem=%s, 
    #                             roll_no=%s, division=%s, gen=%s, dob=%s, dep=%s, email=%s, 
    #                             phone=%s, address=%s, teacher=%s WHERE student_id=%s''',
    #                           (self.var_name.get(), self.var_dep.get(), self.var_course.get(), 
    #                            self.var_year.get(), self.var_sem.get(), self.var_div.get(), 
    #                            self.var_gen.get(), self.var_dob.get(), self.var_phone.get(), 
    #                            self.var_address.get(), self.var_roll_no.get(), 
    #                            self.var_email.get(), self.var_teacher.get(), id))

    #             # Capture and store face images
    #             face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    #             cap = cv2.VideoCapture(0)
    #             img_id = 0

    #             while True:
    #                 ret, frame = cap.read()
    #                 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #                 faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    #                 for (x,y,w,h) in faces:
    #                     # Crop face region
    #                     face_cropped = frame[y:y+h, x:x+w]
    #                     face_cropped_gray = cv2.cvtColor(face_cropped, cv2.COLOR_BGR2GRAY)

    #                     # Save face image to file
    #                     file_name_path = f"C:/Users/Lenovo/Desktop/new--pro/ImagesOfFaces/user.{id}.{img_id}.jpg"
    #                     cv2.imwrite(file_name_path, face_cropped_gray)

    #                     img_id += 1

    #                 # Display cropped face
    #                     cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    #                     cv2.imshow("Croped Face", face_cropped)

    #                 if cv2.waitKey(1) == 13 or img_id == 100:
    #                     break

    #             cap.release()
    #             cv2.destroyAllWindows()

    #             messagebox.showinfo("Info", "DataSet Completed!")
    #             conn.commit()
    #             self.fetch_data()
    #             self.reset_data()
    #             conn.close()

    #         except Exception as es:
    #             messagebox.showerror("Error", f"Due To : {str(es)}", parent=self.root)

            
    
    





    
    # ====================================================================================================================================================================================
    
    def generate_dataset(self):
        if self.var_name.get()=="" or self.var_dep.get()=="select department" or self.var_course.get()=="select course" or self.var_year.get()=="select year" or self.var_sem.get()=="select semester" or self.var_id.get()=="" or self.var_div.get()=="" or self.var_roll_no.get()=="" or self.var_gen.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="" or self.var_phone.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="shariquak$789",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myResutl=my_cursor.fetchall()
                id=0
                sroll=self.var_roll_no.get()
                sname=self.var_name.get()
                for x in myResutl:
                    id+=1
                my_cursor.execute('update student set name=%s,course=%s,year=%s,sem=%s,roll_no=%s,division=%s,gen=%s,dob=%s,dep=%s,email=%s,phone=%s,address=%s,teacher=%s,photo=%s where student_id=%s',( 
                    self.var_name.get(),
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_div.get(),
                    self.var_gen.get(),
                    self.var_dob.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_roll_no.get(),
                    self.var_email.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_id.get()==id+1   
                    ))
                
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                
                # ========================================================================================
                face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_frontalface_default.xml')
                #face_classifier=cv2.CascadeClassifier(haar)
                def face_cropped(img):
                    gry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gry,1.3,5)
                    #scalling factor =1.3
                    #Minimum Neighbor =5

                    for(x,y,w,h)in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0

                while True:
                    ret,frame_my=cap.read()
                    if face_cropped(frame_my) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(frame_my),(500,500))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        #file_name_path="ImagesOfFaces/user"+str(sname)+".jpg"
                        file_name_path="C:/Users/Lenovo/Desktop/new--pro/ImagesOfFaces/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(0,255,29),2)
                        cv2.imshow("Croped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==50:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Info","DataSet Completed!")
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
            







            #     face_classifieer=cv2.CascadeClassifier(cv2.data.haarcascades+ 'haarcascade_frontalface_default.xml')
            #     def face_cropped(img):
            #         gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            #         faces=face_classifieer.detectMultiScale(gray,1.3,5)
            #         #scaling factor=1.3
            #         #minimum neighbour 5
            #         for(x,y,w,y) in faces:
            #             face_cropped=img[y:y+h,x:x+w]
            #             return face_cropped

            #     cap=cv2.VideoCapture(0)
            #     img_id=0
            #     while True:
            #         ret,my_frame=cap.read()
            #         if face_cropped(my_frame) is not None:
            #             img_id+=1
            #         face=cv2.resize(face_cropped(my_frame),dsize=(450,674),fx=0,fy=0,interpolation=cv2.INTER_CUBIC)
            #         face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
            #         file_name_path="data//user"+str(id)+"."+str(img_id)+".jpg"
            #         cv2.imwrite(file_name_path)
            #         cv2.putText(face,str(img_id),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
            #         cv2.imshow('Cropped Face',face)

            #         if cv2.waitKey(1)==13 or int(img_id)==30:
            #             break
            #     cap.release()
            #     cv2.destroyAllWindows()
            #     messagebox.showinfo("Result","Generating data set completed successfully")
            # except Exception as es:
            #     messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
           
           
           
            #     face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            #     def face_cropped(img):
            #         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #         faces = face_classifier.detectMultiScale(gray, 1.3, 5)  # Scaling factor=1.3, minimum neighbors=5
            #         for (x, y, w, h) in faces:
            #             face_cropped = img[y:y+h, x:x+w]
            #             return face_cropped

            #         cap = cv2.VideoCapture(0)
            #         img_id = 0

            #         while True:
            #             ret, my_frame = cap.read()
            #             if face_cropped(my_frame) is not None:
            #                 img_id += 1
            #             face = cv2.resize(face_cropped(my_frame), (450, 350))
            #             face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            #             file_name_path = f"data/user{img_id}.jpg"
            #             cv2.imwrite(file_name_path, face)
            #             cv2.putText(face, str(img_id), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
            #             cv2.imshow("Cropped Face", face)
                        
            #             if cv2.waitKey(1) == 13 or int(img_id) == 30:
            #                 break

            #             cap.release()
            #             cv2.destroyAllWindows()
            #             print("Generating data set completed successfully")
            # except Exception as es:
            #     messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


    

                
    

    

               
                                                                                                                    
               









        





if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
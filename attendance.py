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
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
        self.attendance_data=[]



        # ===================================================================variables
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()


        #1st
        img=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\facial-recognition_0.jpg")
        img=img.resize((800,200), Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_label=Label(self.root,image=self.photoimg)
        f_label.place(x=0,y=0,width=800,height=200)
        #2nd
        img1=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\facial-recognition_0.jpg")
        img1=img1.resize((800,200), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_label=Label(self.root,image=self.photoimg1)
        f_label.place(x=700,y=0,width=800,height=200)

        #for bg
        img3=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\bg.jpg")
        img3=img3.resize((1530,710), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710)

        title_label=Label(bg_img,text="Student Attendance Management System",font=("times new roman",35,"bold"),bg="white",fg="black")
        title_label.place(x=0,y=0,width=1530,height=45)

        main_frame = Frame(bg_img,bg="white",bd=2)
        main_frame.place(x=20,y=55,width=14800,height=580)

        
        #left label frame

        Left_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_l=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\university.jpg")
        img_l=img_l.resize((720,130), Image.LANCZOS)
        self.photoimg_l=ImageTk.PhotoImage(img_l)

        f_label=Label(Left_frame,image=self.photoimg_l)
        f_label.place(x=5,y=0,width=720,height=130)

        left_inside_frame = Frame(Left_frame,bg="white",bd=2,relief=RIDGE)
        left_inside_frame.place(x=0,y=135,width=720,height=370)

        # label and entries

        #attendance id
        attendanceId_label=Label(left_inside_frame,text="Attendance ID:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #name
        name_label=Label(left_inside_frame,text=" Roll No:",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("times new roman",12,"bold"))
        name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #a date
        date_label=Label(left_inside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        date_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("times new roman",12,"bold"))
        date_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #dep
        dep_label=Label(left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        dep_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=20,font=("times new roman",12,"bold"))
        dep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #time

        time_label=Label(left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        time_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("times new roman",12,"bold"))
        time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
       
       
        #rollno

        roll_label=Label(left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("times new roman",12,"bold"))
        roll_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # attendance
        attendence_label=Label(left_inside_frame,text="Attendance:",font=("times new roman",12,"bold"),bg="white")
        attendence_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        attendance_combo=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),width=18,state="readonly")
        attendance_combo["values"]=("status","Present","Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=3,column=1,padx=10,pady=5,sticky=W)

         #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=300,width=715,height=35)

        import_button=Button(btn_frame,text="Import csv",command=self.importCSV,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        import_button.grid(row=0,column=0)

        export_button=Button(btn_frame,text="Export csv ",width=19,font=("times new roman",12,"bold"),bg="blue",fg="white",command=self.exportCSV)
        export_button.grid(row=0,column=1)

        update_button=Button(btn_frame,text="Update",width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_button.grid(row=0,column=2)

        reset_button=Button(btn_frame,command=self.reset_data,text="Reset",width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_button.grid(row=0,column=3)








        right_frame=LabelFrame(main_frame,bg="white",bd=2,relief=RIDGE,text="Attndance Details",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)

        #button frame
        table_frame=Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=5,width=700,height=445)

        # ==============================scrolbar
        scrol_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scrol_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","dep","time","date","attendance"),xscrollcommand=scrol_x.set,yscrollcommand=scrol_y.set)


        scrol_x.pack(side=BOTTOM,fill=X)
        scrol_y.pack(side=RIGHT,fill=Y)

        scrol_x.config(command=self.AttendanceReportTable.xview)
        scrol_y.config(command=self.AttendanceReportTable.yview)


        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("dep",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("dep",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease-1>",self.get_cursor)
    # ==================================================fetch data
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,value=i)
# =======================================================================================================================================
    def importCSV(self):
            global mydata
            mydata.clear()
            fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("csv file","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln) as myfile:
                csvread=csv.reader(myfile,delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)
# ====================================================================================================================================================
    # def exportCSV(self):
    #     try:
    #         if len(mydata)<1:
    #             messagebox.showerror("No Data","No Data Found",parent=self.root)
    #             return False
    #         fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="open csv",filetypes=(("csv file","*.csv"),("All File","*.*")),parent=self.root)
    #         with open(fln,mode="w",newline="") as myfile:
    #             exp_write=csv.writer(myfile,delimiter=",")
    #             for i in mydata:
    #                 exp_write.writerow(i)
    #             messagebox.showinfo("Data Export","Your data has exported to "+os.path.basename(fln)+" Successfully")
    #     except Exception as es:
    #         messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    # def get_cursor(self):
    #     cursor_row=self.AttendanceReportTable.focus()
    #     content=self.AttendanceReportTable.item(cursor_row)
    #     rows=content['values']
    #     self.var_atten_id.set(rows[0])
    #     self.var_atten_name.set(rows[1])
    #     self.var_atten_date.set(rows[2])
    #     self.var_atten_dep.set(rows[3])
    #     self.var_atten_time.set(rows[4])
    #     self.var_atten_roll.set(rows[5])
    #     self.var_atten_attendance.set(rows[6])


    def exportCSV(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data Found", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV file", "*.csv"), ("All Files", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data has been exported to " + os.path.basename(fln) + " successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

    def get_cursor(self, event=None):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        if rows:  # Check if rows is not empty
            self.var_atten_id.set(rows[0])
            self.var_atten_name.set(rows[1])
            self.var_atten_date.set(rows[2])
            self.var_atten_dep.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_roll.set(rows[5])
            self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_date.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_roll.set("")
        self.var_atten_attendance.set("")
        


        







if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
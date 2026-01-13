import os
import cv2
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import sys
import dlib
import numpy as np
import os
import train
import xml.etree.cElementTree as ET

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("face Recognition System")


        title_label=Label(self.root,text="Train Data Set",font=("times new roman",35,"bold"),bg="white",fg="navyblue")
        title_label.place(x=0,y=0,width=1530,height=45)

        img_top=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\facialrecognition.png")
        img_top=img_top.resize((1530,325), Image.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_label=Label(self.root,image=self.photoimg_top)
        f_label.place(x=0,y=55,width=1530,height=325)
        #button
        b1_1=Button(self.root,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="white",fg="navyblue")
        b1_1.place(x=0,y=380,width=1530,height=60)


        img_bottom=Image.open(r"C:\Users\Lenovo\Desktop\new--pro\icons\bg.png")
        img_bottom=img_bottom.resize((1530,325),Image.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_label=Label(self.root,image=self.photoimg_bottom)
        f_label.place(x=0,y=440,width=1530,height=325)


def train_face_recognizer(data_dir, output_file):
    # Create a list of image paths and corresponding labels
    image_paths = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
    faces = []
    labels = []

    for image_path in image_paths:
        # Read the image in grayscale
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        # Extract the label from the image filename
        label = int(os.path.split(image_path)[-1].split(".")[1])
        # Store the face and label
        faces.append(img)
        labels.append(label)

    # Create LBPH recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # Train the recognizer with the faces and labels
    recognizer.train(faces, np.array(labels))
    # Save the trained model to XML file
    recognizer.save(output_file)

# Example usage
data_directory = r"C:\Users\Lenovo\Desktop\new--pro\ImagesOfFaces"
output_xml_file = r"C:\Users\Lenovo\Desktop\new--pro\classifier.xml"
train_face_recognizer(data_directory, output_xml_file)


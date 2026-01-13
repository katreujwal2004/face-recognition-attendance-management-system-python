Face Recognition Attendance Management System

Python | OpenCV | MySQL | Tkinter

Project Summary

A real-time Face Recognition Attendance Management System designed to automate attendance marking using computer vision. The system accurately detects and recognizes faces through a live camera feed, logs attendance with timestamps, prevents duplicates, and generates structured reports — eliminating manual effort and proxy attendance.

Overview

This project implements an end-to-end desktop-based attendance solution using OpenCV-powered face recognition and a Tkinter GUI. It captures real-time video, identifies registered individuals, and records attendance in a MySQL database with full backend integration. The system also supports PDF report generation and audio alerts, making it suitable for academic or organizational use.

Problem Statement

Conventional attendance systems are time-consuming, error-prone, and vulnerable to manipulation. The objective of this project is to build a secure, automated, and efficient attendance system that leverages face recognition to ensure accuracy, transparency, and real-time execution.

Dataset

Face image dataset (local storage)

Includes:

Labeled face images of registered users

Live camera input for recognition

Attendance records stored in a database

Files & Directories

ImagesOfFaces/ → Dataset of registered face images

main.py → Core face recognition and attendance logic

train.py → Face dataset training module

gui.py → Tkinter-based user interface

database/ → MySQL schema and tables

reports/ → Generated PDF attendance reports

README.md → Project documentation

Tools & Technologies

Python – Core programming language

OpenCV – Face detection and recognition

Haar Cascades – Face detection algorithm

Tkinter – Desktop GUI development

MySQL – Backend database for attendance storage

ReportLab / FPDF – PDF report generation

System Approach
Face Detection & Recognition

Implemented Haar Cascade Classifier for face detection

Trained a face recognition model using labeled image datasets

Performed real-time recognition via live camera feed

Attendance Automation

Automatically marks attendance upon successful recognition

Prevents duplicate attendance entries for the same day

Logs attendance with accurate date and time stamps

GUI Development

Live camera feed display

User-friendly controls and navigation

Buttons for recognition, dataset creation, and reporting

Database Integration

Persistent storage of user and attendance records

Structured MySQL tables for efficient querying

Attendance data used directly for report generation

Key Features

Real-time face recognition-based attendance

Duplicate attendance prevention

Timestamp-based logging

Interactive desktop application

Live camera feed with recognition status

Audio alerts for recognition outcomes

PDF attendance report generation

Secure MySQL database integration

Output

The system provides:

Live face recognition through webcam

Automatic attendance marking

On-screen status notifications

Downloadable PDF attendance reports

How to Run the Project
Project Repository

https://github.com/katreujwal2004/face-recognition-attendance-management-system

Steps

Clone the repository

git clone https://github.com/katreujwal2004/face-recognition-attendance-management-system.git


Install required dependencies

pip install opencv-python mysql-connector-python reportlab


Configure MySQL database and tables

Run the application

python main.py


Register faces and start attendance using the GUI

Results & Conclusion

This project demonstrates the practical application of computer vision and automation to solve real-world problems. It showcases strong skills in Python development, OpenCV-based face recognition, GUI design, database integration, and system automation, making it a solid addition to a data/AI-focused portfolio.

Future Enhancements

Improve accuracy using deep learning-based face recognition

Add cloud database support

Develop a web-based interface

Enable multi-camera attendance tracking

Implement role-based access control

Author & Contact

Ujwal Katre
📧 Email: ujwalkatre2004@gmail.com

🔗 GitHub: https://github.com/katreujwal2004

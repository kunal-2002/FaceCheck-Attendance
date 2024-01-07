from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help



class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x790+0+0")
        self.root.title("FaceCheck Attendance")
        self.root.wm_iconbitmap("face.ico")

        # Header Image
        img = Image.open(r".\assets\Header.png")
        img = img.resize((1540,130),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1540,height=130)

        # Background Image
        img1 = Image.open(r".\assets\Background.jpg")
        img1 = img1.resize((1540,660),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0,y=130,width=1540,height=660)

        title_lbl = Label(bg_img,text="STUDENT ATTENDANCE MONITORING SYSTEM USING FACE RECOGNITION",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1540,height=45) 
        
        # current Time
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
            
        lbl = Label(title_lbl, font=('times new roman',14,'bold'), background='white', foreground='blue')
        lbl.place(x=0, y=0,width=110, height=50)
        time()

        # Student Details Button
        img2 = Image.open(r".\assets\Students.png")
        img2 = img2.resize((220,220),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1 = Button(bg_img,image=self.photoimg2,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_l = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_l.place(x=200,y=300,width=220,height=40)

        # Detect Face Button
        img3 = Image.open(r".\assets\Face_Detection.png")
        img3 = img3.resize((220,220),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b2 = Button(bg_img,image=self.photoimg3,cursor="hand2", command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220)

        b2_l = Button(bg_img,text="Face Detector",cursor="hand2", command=self.face_data, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_l.place(x=500,y=300,width=220,height=40)

        # Attendance Button
        img4 = Image.open(r".\assets\Attendance.png")
        img4 = img4.resize((220,220),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b3 = Button(bg_img,image=self.photoimg4,cursor="hand2",command=self.attendance_data)
        b3.place(x=800,y=100,width=220,height=220)

        b3_l = Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_l.place(x=800,y=300,width=220,height=40)

        # Help Button
        img5 = Image.open(r".\assets\help.png")
        img5 = img5.resize((220,220),Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b4 = Button(bg_img,image=self.photoimg5,cursor="hand2", command=self.help_page)
        b4.place(x=1100,y=100,width=220,height=220)

        b4_l = Button(bg_img,text="Help",cursor="hand2", command=self.help_page,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_l.place(x=1100,y=300,width=220,height=40)

        # Training the Algorithm Button
        img6 = Image.open(r".\assets\Model_Training.png")
        img6 = img6.resize((220,220),Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b5 = Button(bg_img,image=self.photoimg6,cursor="hand2", command=self.train_algo)
        b5.place(x=200,y=380,width=220,height=220)

        b5_l = Button(bg_img,text="Algorithm Training",cursor="hand2", command=self.train_algo,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_l.place(x=200,y=580,width=220,height=40)

        # Photos Button
        img7 = Image.open(r".\assets\Photos.jpg")
        img7 = img7.resize((220,220),Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b6 = Button(bg_img,image=self.photoimg7,cursor="hand2", command=self.open_img)
        b6.place(x=500,y=380,width=220,height=220)

        b6_l = Button(bg_img,text="Photos",cursor="hand2", command=self.open_img, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_l.place(x=500,y=580,width=220,height=40)

        # Developers Button
        img8 = Image.open(r".\assets\developer.png")
        img8 = img8.resize((220,220),Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b7 = Button(bg_img,image=self.photoimg8,cursor="hand2", command=self.developer_page)
        b7.place(x=800,y=380,width=220,height=220)

        b7_l = Button(bg_img,text="Developers",cursor="hand2", command=self.developer_page, font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_l.place(x=800,y=580,width=220,height=40)

        # Exit Button
        img9 = Image.open(r".\assets\exit.png")
        img9 = img9.resize((220,220),Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b8 = Button(bg_img,image=self.photoimg9,cursor="hand2", command=self.exit_button)
        b8.place(x=1100,y=380,width=220,height=220)

        b8_l = Button(bg_img,text="Exit",cursor="hand2", command=self.exit_button,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b8_l.place(x=1100,y=580,width=220,height=40)
    
    def open_img(self):
        os.startfile("data")

    # Buttons functions
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
        
    def train_algo(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
        
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
        
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
        
    def developer_page(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)
        
    def help_page(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)
        
    def exit_button(self):
        self.inp = tkinter.messagebox.askyesno("Face Recognition System","Are you sure to exit this software?",parent=self.root)
        if self.inp > 0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
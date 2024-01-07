import webbrowser
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x790+0+0")
        self.root.title("FaceCheck Attendance")
        self.root.wm_iconbitmap("face.ico")
        
        
        title_lbl = Label(self.root,text="HELP",font=("times new roman",25,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1540,height=45)
        
        Back_Button = Button(title_lbl, text="Back", command=self.root.destroy, font=("arial",11,"bold"),width=17,bg="white",fg="red")
        Back_Button.pack(side=RIGHT)

        img_top = Image.open(r".\assets\help.jpeg")
        img_top = img_top.resize((1540,740),Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1540,height=740)
        
        email_label1 = Label(f_lbl, text="For any queries, drop a mail at", font=("times new roman", 20, "bold"),fg="white", bg='black')
        email_label1.place(x=600,y=150)
        
        email_label2 = Label(f_lbl, text="kkunal2103@outlook.com", font=("times new roman", 20, "bold"),fg="blue", bg='black', cursor='hand2')
        email_label2.place(x=625,y=185)
        
        email_label2.bind('<Button-1>',
                   lambda x:webbrowser.open_new("mailto:kkunal2103@outlook.com"))
        
if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
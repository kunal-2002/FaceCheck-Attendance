import webbrowser
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x790+0+0")
        self.root.title("Face Recognition System")
        
        
        title_lbl = Label(self.root,text="DEVELOPERS",font=("times new roman",25,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1540,height=45)
        
        Back_Button = Button(title_lbl, text="Back", command=self.root.destroy, font=("arial",11,"bold"),width=17,bg="white",fg="red")
        Back_Button.pack(side=RIGHT)

        img_top = Image.open(r".\assets\Background.jpg")
        img_top = img_top.resize((1540,740),Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1540,height=740)
        
        # Contributor 1
        # Main Frame
        main_frame1 = Frame(f_lbl, bd=2, bg="white")
        main_frame1.place(x=285, y=10, width=400, height=500)
        
        img1 = Image.open(r".\assets\Kunal.png")
        img1 = img1.resize((200,200),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(main_frame1, image=self.photoimg1)
        f_lbl1.place(x=100,y=10,width=200,height=200)
        
        # Developer1 info
        name_label1 = Label(main_frame1, text="Kunal Kathpal", font=("times new roman", 20, "bold"),fg="blue", bg="white")
        name_label1.place(x=100,y=220)
        
        w_label1 = Label(main_frame1, text="Full Stack Developer", font=("times new roman", 20, "bold"),fg="blue", bg="white")
        w_label1.place(x=100,y=260)
        
        p_label1 = Label(main_frame1, text="Student, 7th Semester", font=("times new roman", 14, "bold"),fg="black", bg="white")
        p_label1.place(x=100,y=300)
        
        c_label1 = Label(main_frame1, text="CRSSIET, Jhajjar", font=("times new roman", 14, "bold"),fg="black", bg="white")
        c_label1.place(x=100,y=320)
        
        github_btn1 = Button(main_frame1, text="Github", width=18, font=("times new roman",16,"bold"), bg="black", fg="white", cursor="hand2")
        github_btn1.place(x=100, y=350)
        github_btn1.bind('<Button-1>',
                   lambda x:webbrowser.open_new("https://www.github.com/kunal-2002"))
        
        linkedin_btn1 = Button(main_frame1, text="Linkedin", width=18, font=("times new roman",16,"bold"), bg="black", fg="white", cursor="hand2")
        linkedin_btn1.place(x=100, y=400)
        linkedin_btn1.bind('<Button-1>',
                   lambda x:webbrowser.open_new("https://www.linkedin.com/in/kunal-kathpal"))
    

        # Contributor 2
        # Main Frame
        main_frame2 = Frame(f_lbl, bd=2, bg="white")
        main_frame2.place(x=855, y=10, width=400, height=500)
        
        img2 = Image.open(r".\assets\Lucky.png")
        img2 = img2.resize((200,200),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(main_frame2, image=self.photoimg2)
        f_lbl2.place(x=100,y=10,width=200,height=200)
        
        # Developer2 info
        name_label2 = Label(main_frame2, text="Lucky", font=("times new roman", 20, "bold"),fg="blue", bg="white")
        name_label2.place(x=100,y=220)
        
        w_label2 = Label(main_frame2, text="Full Stack Developer", font=("times new roman", 20, "bold"),fg="blue", bg="white")
        w_label2.place(x=100,y=260)
        
        p_label2 = Label(main_frame2, text="Student, 7th Semester", font=("times new roman", 14, "bold"),fg="black", bg="white")
        p_label2.place(x=100,y=300)
        
        c_label2 = Label(main_frame2, text="CRSSIET, Jhajjar", font=("times new roman", 14, "bold"),fg="black", bg="white")
        c_label2.place(x=100,y=320)
        
        github_btn2 = Button(main_frame2, text="Github",width=18, font=("times new roman",16,"bold"), bg="black", fg="white", cursor="hand2")
        github_btn2.place(x=100, y=350)
        github_btn2.bind('<Button-1>',
                   lambda x:webbrowser.open_new("https://www.github.com/Luckydhingra"))
        
        linkedin_btn2 = Button(main_frame2, text="Linkedin", width=18, font=("times new roman",16,"bold"), bg="black", fg="white", cursor="hand2")
        linkedin_btn2.place(x=100, y=400)
        linkedin_btn2.bind('<Button-1>',
                   lambda x:webbrowser.open_new("https://www.linkedin.com/in/lucky-dhingra"))
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
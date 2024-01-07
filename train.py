from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(self.root,text="TRAINING THE ALGORITHM",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1540,height=45)

        img_top = Image.open(r".\assets\facialrecognition.png")
        img_top = img_top.resize((1540,325),Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1540,height=325)

        # button
        b1_l = Button(self.root,text="TRAIN ALGORITHM", command=self.train_classifier, cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_l.place(x=0,y=380,width=1540,height=60)

        img_bottom = Image.open(r".\assets\facial_recognition_action.jpg")
        img_bottom = img_bottom.resize((1540,350),Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1540,height=350)

    def train_classifier(self):
        data_dir= ("data")
        path=[os.path.join(data_dir, file) for file in os.listdir(data_dir)]  #list comprehension
        
        faces=[]
        ids=[]

        for image in path:
            img = Image.open(image).convert('L') #Gray Scale conversion
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
            
        ids=np.array(ids)

        # Train the classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Success","Training of the LBPH algorithm is completed successfully.")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
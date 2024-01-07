from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np



class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x790+0+0")
        self.root.title("Face Recognition System")
        
        title_lbl = Label(self.root,text="FACE RECOGNITION",font=("times new roman",25,"bold"),bg="white",fg="Green")
        title_lbl.place(x=0,y=0,width=1540,height=45)
        
        # 1st image
        img_left = Image.open(r".\assets\face_detector1.jpg")
        img_left = img_left.resize((650,738),Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.root, image=self.photoimg_left)
        f_lbl.place(x=0,y=55,width=650,height=738)
        
        # 2nd image
        img_right = Image.open(r".\assets\face-recognition.jpg")
        img_right = img_right.resize((890,738),Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(self.root, image=self.photoimg_right)
        f_lbl.place(x=650,y=55,width=890,height=738)
        
        # Button
        b1_l = Button(f_lbl,text="Face Recognition",command=self.face_recog, cursor="hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1_l.place(x=340,y=620,width=200,height=40)
        
    # Attendance
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list=[]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
            for line in myDataList:
                entry= line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                
        
    # Face Recognition
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            
            coord = []
            
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id, predict= clf.predict(gray_image[y:y+h, x:x+w])
                confidence= int((100*(1-predict/300)))
                
                conn = mysql.connector.connect(host="localhost",user="root",password="4321",database="face_recognizer")
                my_cursor = conn.cursor()
                
                # "dep","course","year","sem","Student_id","name","div","roll","gender","dob","email","phone","address","teacher","photo"
                my_cursor.execute("Select Student_id from student where Student_id="+str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)
                
                my_cursor.execute("Select Roll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)
                
                my_cursor.execute("Select name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)
                
                my_cursor.execute("Select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)
            
                if confidence>77:
                    cv2.putText(img, f"ID: {i}",(x,y-85),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img, f"Roll No: {r}",(x,y-60),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img, f"Name: {n}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    cv2.putText(img, f"Department: {d}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                coord = [x,y,w,y]
                
            return coord
        
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(0)
        
        while True:
            ret, img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)
            
            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
            

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
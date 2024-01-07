from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1540x790+0+0")
        self.root.title("Face Recognition System")
        
        # variables
        self.var_studentID = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_attendance = StringVar()
        
        # Header Image
        img = Image.open(r".\assets\Header.png")
        img = img.resize((1540,130),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1540,height=130)

        # Background Image
        img1 = Image.open(r".\assets\Background.jpg")
        img1 = img1.resize((1540,710),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimg1)
        bg_img.place(x=0,y=130,width=1540,height=710)

        title_lbl = Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1540,height=45)
        
        # Main Frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=55, width=1490, height=600)
        
        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Information", font=("times new roman", 13, "bold"))
        Left_frame.place(x=15, y=10, width=760, height=580)

        img_left = Image.open(r".\assets\collegestudents.jpg")
        img_left = img_left.resize((750,130),Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=750,height=130)
        
        # inner left frame
        innerLeft_frame = Frame(Left_frame, bd=2, bg="white", relief=RIDGE)
        innerLeft_frame.place(x=5, y=135, width=750, height=370)
        
        # Labels and entries
        # Student ID
        Student_id_label = Label(innerLeft_frame, text="Student ID:", font=("times new roman", 13, "bold"), bg="white")
        Student_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        Student_id_entry = ttk.Entry(innerLeft_frame, width=20,textvariable=self.var_studentID ,font=("times new roman", 13, "bold"))
        Student_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        
        # Roll No.
        rollNo_label = Label(innerLeft_frame, text="Roll No:", font=("times new roman", 13, "bold"), bg="white")
        rollNo_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        rollNo_entry = ttk.Entry(innerLeft_frame, width=20,textvariable=self.var_roll, font=("times new roman", 13, "bold"))
        rollNo_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        
        # Student Name
        studentName_label = Label(innerLeft_frame, text="Student Name:", font=("times new roman", 13, "bold"), bg="white")
        studentName_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        studentName_entry = ttk.Entry(innerLeft_frame, width=20,textvariable=self.var_name, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        
        # Department
        dep_label = Label(innerLeft_frame, text="Department:", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=1, column=2, padx=10, sticky=W)

        dep_entry = ttk.Entry(innerLeft_frame, width=20, textvariable=self.var_dep, font=("times new roman", 13, "bold"))
        dep_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        
        # Date
        date_label = Label(innerLeft_frame, text="Date:", font=("times new roman", 13, "bold"), bg="white")
        date_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        date_entry = ttk.Entry(innerLeft_frame, width=20, textvariable=self.var_date, font=("times new roman", 13, "bold"))
        date_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        
        # Time
        time_label = Label(innerLeft_frame, text="Time:", font=("times new roman", 13, "bold"), bg="white")
        time_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        time_entry = ttk.Entry(innerLeft_frame, width=20,textvariable=self.var_time, font=("times new roman", 13, "bold"))
        time_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)
        
        # Attendance status
        attendance_label = Label(innerLeft_frame, text="Attendance Status:", font=("times new roman", 13, "bold"), bg="white")
        attendance_label.grid(row=3, column=0, padx=10, sticky=W)

        self.attendance_status = ttk.Combobox(innerLeft_frame, textvariable=self.var_attendance, font=("times new roman", 13, "bold"), state="readonly", width=18)
        self.attendance_status["values"] = ("Status","Present","Absent")
        self.attendance_status.current(0)
        self.attendance_status.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        
        # buttons Frame 
        btn_frame = Frame(innerLeft_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=745, height=35)

        import_btn = Button(btn_frame, text="Import CSV",command=self.importCsv, width=18, font=("times new roman",13,"bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, text="Export CSV",command=self.exportCsv, width=18, font=("times new roman",13,"bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="Update", width=18, font=("times new roman",13,"bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, width=18, font=("times new roman",13,"bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        
        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 13, "bold"))
        Right_frame.place(x=790, y=10, width=670, height=580)
        
        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=650, height=460)
        
        # Table and Scroll Bar
        scroll_x= ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y= ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable= ttk.Treeview(table_frame,column=("id","roll","name","dep","time","date","attendance"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="Student ID")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("dep",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("dep",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        
    # fetch data
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    # Import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select CSV File",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
            
    # Export CSV
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","Data Not Found to export.",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV File",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                csvwrite = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    csvwrite.writerow(i)
                messagebox.showinfo("Success","Your data is exported to "+os.path.basename(fln)+" successfully.",parent=self.root)
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                
    # get cursor
    def get_cursor(self,event=""):
        cursor_focus= self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_focus)
        data= content["values"]
        
        self.var_studentID.set(data[0]),
        self.var_roll.set(data[1]),
        self.var_name.set(data[2]),
        self.var_dep.set(data[3]),
        self.var_time.set(data[4]),
        self.var_date.set(data[5]),
        self.var_attendance.set(data[6])
        
    # reset
    def reset_data(self):
        self.var_studentID.set(""),
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_dep.set(""),
        self.var_time.set(""),
        self.var_date.set(""),
        self.var_attendance.set("Status")
        
        
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
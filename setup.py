import sys
from cx_Freeze import setup, Executable
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Admin\AppData\Local\Programs\Python\Python311\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Admin\AppData\Local\Programs\Python\Python311\tcl\tk8.6"

executables = [Executable("app.py", base=base, icon="face.ico")]


setup(
    name = "FaceCheck Attendance",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["face.ico",'tcl86t.dll','tk86t.dll', 'assets','data','database','attendance_report']}},
    version = "1.0",
    description = "Face Recognition System for Attendance Tracking",
    executables = executables
    )

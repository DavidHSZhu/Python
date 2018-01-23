from tkinter import *
from BackEnd import DatabaseConnector
from tkinter import font
class MainWindow:
    "This class defines the front end for our database management program"

    def __init__(self):
        self.initGUI()
        self.buildGUI()
        self.startBackEnd()
        self.startGUI()

    def initGUI(self):
        self.root = Tk()
        self.root.wm_title("Database Manager")
        self.topFrame = Frame(self.root)
        self.bottomFrame = Frame(self.root)
        self.varFirstName=StringVar()
        self.labFname=Label(self.root, text="FirstName:").grid(row=0)
        self.txt_Fname = Entry(self.root,textvariable=self.varFirstName)
        self.txt_Fname.grid(row=0,column=1)
        self.varLastName=StringVar()
        self.labLname=Label(self.root, text="LastName:").grid(row=0,column=2)
        self.txt_Lname = Entry(self.root,textvariable=self.varLastName)
        self.txt_Lname.grid(row=0,column=3)
        self.varIDNumber=StringVar()
        self.labLIDNumber=Label(self.root, text="IDNumber:").grid(row=0,column=4)
        self.txt_IDNumber = Entry(self.root,textvariable=self.varIDNumber)
        self.txt_IDNumber.grid(row=0,column=5)
        self.varGPA=StringVar()
        self.labGPA=Label(self.root, text="GPA:").grid(row=0,column=6)
        self.txt_GPA = Entry(self.root,textvariable=self.varGPA)
        self.txt_GPA.grid(row=0,column=7)
        self.btn_Insert = Button(self.root,text ="Insert", command = self.insertEvent)
        self.btn_Update = Button(self.root,text ="Update", command = self.updateEvent)
        self.btn_Remove = Button(self.root,text ="Remove", command = self.removeEvent)
        self.btn_Get = Button(self.root,text ="Get", command = self.getEvent)

    def buildGUI(self):

        self.btn_Insert.grid(row=2,column=0,columnspan=2,sticky=W+E+N+S)
        self.btn_Update.grid(row=2,column=2,columnspan=2,sticky=W+E+N+S)
        self.btn_Remove.grid(row=2,column=4,columnspan=2,sticky=W+E+N+S)
        self.btn_Get.grid(row=2,column=6,columnspan=2,sticky=W+E+N+S)
        self.my_font = font.Font(family="Monaco", size=8)
        self.list1=Listbox(self.root,font=self.my_font)
        self.list1.grid(row=3,column=1,columnspan=6,sticky=W+E+N+S)
    def startGUI(self):
        self.root.mainloop()

    #insert new row with all 4 fields
    def insertEvent(self):
        fname = self.txt_Fname.get()
        lname = self.txt_Lname.get()
        idNumber = self.txt_IDNumber.get()
        gpa = self.txt_GPA.get()
        self.list1.delete(0,END)
        self.backEnd.insert(fname, lname, idNumber, gpa)


    #update based on ID
    def updateEvent(self):
        fname = self.txt_Fname.get()
        lname = self.txt_Lname.get()
        idNumber = self.txt_IDNumber.get()
        gpa = self.txt_GPA.get()
        self.list1.delete(0,END)
        self.backEnd.update(fname, lname, idNumber, gpa)

    #remove based on ID
    def removeEvent(self):
        idNumber = self.txt_IDNumber.get()
        self.list1.delete(0,END)
        self.backEnd.remove(idNumber)


    #get based on ID
    def getEvent(self):
        idNumber = self.txt_IDNumber.get()
        self.list1.delete(0,END)
        self.backEnd.get(idNumber,self.varFirstName,self.varLastName,self.varGPA)



    def startBackEnd(self):
      self.backEnd = DatabaseConnector("localhost","haishui","ap92fr","student",self.list1)



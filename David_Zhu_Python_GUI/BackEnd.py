#import MySQLdb
import pymysql

class DatabaseConnector:
 "This class is used as the back end to connect to our database"

 def __init__(self,hostname,username,password,databaseName,list1):
    self.hostname = hostname
    self.username = username
    self.password = password
    self.databaseName = databaseName
    self.list=list1
    self.showList()
 def openDBConnection(self):
    self.db = pymysql.connect(self.hostname,self.username,self.password,self.databaseName)
    #print("Opening Connection")

 def closeDBConnection(self):
    self.db.close()
    #print("Clossing Connection")

 def insert(self, fname, lname, IDNumber, GPA):
    self.openDBConnection()
    cursor=self.db.cursor()
    try:
       cursor.execute("INSERT INTO  `student_info` (  `firstName` ,  `LastName` ,  `StudentID` ,  `GPA` ) VALUES (\""+fname+"\",  '"+lname+"', {}, {})".format(IDNumber,GPA))
       print("Inserting",fname,lname,IDNumber,GPA)
       self.db.commit()
    except:
       self.db.rollback()
    self.closeDBConnection()
    self.showList()
 def update(self, fname, lname, IDNumber, GPA):
    self.openDBConnection()
    cursor=self.db.cursor()
    self.idnumber=int(IDNumber)

    try:
      self.IDNumber=int(IDNumber)
      cursor.execute("UPDATE  `student_info` set `firstName`='%s' ,`LastName`='%s' ,`GPA`='%s' WHERE StudentID='%d'"% (fname, lname,GPA ,self.idnumber))
      self.db.commit()
      print("Updating record in Students table",fname, lname,IDNumber, GPA)
    except:
      self.db.rollback()
    self.closeDBConnection()
    self.showList()
 def remove(self, IDNumber):
    self.openDBConnection()
    cursor=self.db.cursor()
    try:
     self.studentid=int(IDNumber)
     cursor.execute("delete from student_info WHERE StudentID='%d'" % (self.studentid))
     self.db.commit()
     print("Removing record from Students table where IDNmuber=",IDNumber)
    except:
     self.db.rollback()
    self.closeDBConnection()
    self.showList()
 def get(self, IDNumber, varFirstName,varLastName,varGPA):
   self.openDBConnection()
   print(IDNumber)
   cursor=self.db.cursor()
   self.IDNumber=int(IDNumber)
   cursor.execute("SELECT firstname,lastname,GPA FROM Student_info` WHERE StudentID='%d'" % self.IDNumber)

   for row in cursor.fetchall():

      varFirstName.set(str(row[0]))
      varLastName.set(str(row[1]))
      varGPA.set(str(row[2]))
   self.closeDBConnection()
   self.showList()
 def showList(self):
     self.openDBConnection()
     self.cursor=self.db.cursor()
     self.cursor.execute("SELECT firstname,lastname,studentid,GPA FROM `student_info` order by studentid asc ")
     i=0

     for row in self.cursor.fetchall():
              i+=1
              self.list.insert(i,'{0:<9}'.format(str(row[0]))+'{0:<10}'.format(row[1])+'{0:<10}'.format(row[2])+'{0:<10}'.format(str(row[3])))
     self.closeDBConnection()
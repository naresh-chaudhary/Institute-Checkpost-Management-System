#!/usr/bin/python

import mysql.connector
from mysql.connector import errorcode
from datetime import datetime

##===============================================

class DatabaseUtility:
        def __init__(self, database, tableName1,tableName2,tableName3):
                self.db = database
                self.tableName1=tableName1
                self.tableName2=tableName2
                self.tableName3=tableName3
                self.date1 = datetime.now().strftime("%y-%m-%d")
                self.time = datetime.now().strftime("%H:%M:%S")

                #f = open('C:\\Users\\The_Captain\\Desktop\\TPayne Experience\\_Episodes\\_LetsLearn\\026_LLP__SQL_Databases\\password.txt', 'r')
                #p = f.read(); f.close();
                self.cnx = mysql.connector.connect(user = 'root',
                                                                        password = '',
                                                                        host = '127.0.0.1')
                self.cursor = self.cnx.cursor()

                self.ConnectToDatabase()
                self.CreateTable1()
                self.CreateTable2()
                self.CreateTable3()
                
        def ConnectToDatabase(self):
                try:
                        self.cnx.database = self.db
                except mysql.connector.Error as err:
                        if err.errno == errorcode.ER_BAD_DB_ERROR:
                                self.CreateDatabase()
                                self.cnx.database = self.db
                        else:
                                print(err.msg)

        def CreateDatabase(self):
                try:
                        self.RunCommand("CREATE DATABASE %s DEFAULT CHARACTER SET 'utf8';" %self.db)
                except mysql.connector.Error as err:
                        print("Failed creating database: {}".format(err))

        def CreateTable1(self):
                cmd = (" CREATE TABLE IF NOT EXISTS " + self.tableName1 + " ("
                        " `id_no` varchar(15) NOT NULL ,"
                        "`id_type` varchar(15) NOT NULL,"
                        " `date` date NOT NULL,"
                        " `time_in` time NOT NULL,"
                        " `fname` varchar(25) NOT NULL,"
                        "`lname` varchar(25),"
                        "`sex` varchar(10) NOT NULL,"
                        "`address` varchar(150) NOT NULL,"
                        "`mobile_no` varchar(10) DEFAULT 'NA',"
                        "`landline` varchar(15) DEFAULT 'NA',"
                        "PRIMARY KEY(`id_no`,`date`,`time_in` )"
                        ") ENGINE=InnoDB;")
                self.RunCommand(cmd)

        def CreateTable2(self):
                cmd=("CREATE TABLE IF NOT EXISTS "+self.tableName2+"("
                     "`vehicle_no` varchar(15) NOT NULL,"
                     "`vehicle_type` varchar(15) NOT NULL,"
                     "`id_no` varchar(15) ,"
                     "`date` date NOT NULL,"
                     "`time_in` time NOT NULL,"
                     "FOREIGN KEY(id_no,date,time_in) REFERENCES `person`(`id_no`,`date`,`time_in`),"
                     "PRIMARY KEY(`vehicle_no`,`id_no`)"
                     ") ENGINE=InnoDB;")
                self.RunCommand(cmd)

        def CreateTable3(self):
                cmd=("CREATE TABLE IF NOT EXISTS "+self.tableName3+"("
                     "`id_no` varchar(15) NOT NULL,"
                     "`date` date NOT NULL,"
                     "`time_in` time NOT NULL,"
                     "`whom_to_visit` varchar(50) NOT NULL,"
                     "`relationship` varchar(20),"
                     "`purpose_of_visit` varchar(30),"
                     "FOREIGN KEY(id_no,date,time_in) REFERENCES `person`(`id_no`,`date`,`time_in`)"
                     #"PRIMARY KEY(`id_no`,`date`,`time_in`)"
                     ") ENGINE=InnoDB;")
                self.RunCommand(cmd)

        def GetTable1(self):
                self.CreateTable1()
                return self.RunCommand("SELECT * FROM %s;" % self.tableName1)
        def GetTable2(self):
                self.CreateTable3()
                return self.RunCommand("SELECT * FROM %s;" % self.tableName2)
        def GetTable3(self):
                self.CreateTable3()
                return self.RunCommand("SELECT * FROM %s;" % self.tableName3)
        def GetTable1joinTable2(self):
                cmd="SELECT p.id_no,p.id_type,p.time_in,p.fname,p.lname,p.sex,p.address,p.mobile_no,p.landline,v.vehicle_no,"
                cmd+="v.vehicle_type FROM %s as p left outer join %s as v on p.id_no=v.id_no;"%(self.tableName1,self.tableName2)
                return self.RunCommand(cmd)
        def GetByFname(self,name,date):
                cmd="SELECT p.id_no,p.id_type,p.time_in,p.fname,p.lname,p.sex,p.address,p.mobile_no,p.landline,v.vehicle_no,"
                cmd+="v.vehicle_type FROM %s as p left outer join %s as v on p.id_no=v.id_no WHERE p.fname REGEXP '%s' "%(self.tableName1,self.tableName2,name)
                cmd+="AND p.date='%s';"%(date)
                return self.RunCommand(cmd)
        def GetByLname(self,name,date):
                cmd="SELECT p.id_no,p.id_type,p.time_in,p.fname,p.lname,p.sex,p.address,p.mobile_no,p.landline,v.vehicle_no,"
                cmd+="v.vehicle_type FROM %s as p left outer join %s as v on p.id_no=v.id_no WHERE p.lname REGEXP '%s' "%(self.tableName1,self.tableName2,name)
                cmd+="AND p.date='%s';"%(date)
                return self.RunCommand(cmd)
        def GetByName(self,fname,lname,date):
                cmd="SELECT p.id_no,p.id_type,p.time_in,p.fname,p.lname,p.sex,p.address,p.mobile_no,p.landline,v.vehicle_no,"
                cmd+="v.vehicle_type FROM %s as p left outer join %s as v on p.id_no=v.id_no WHERE p.fname REGEXP '%s' "%(self.tableName1,self.tableName2,fname)
                cmd+="AND p.lname REGEXP '%s' AND p.date='%s' "%(lname,date)
                return self.RunCommand(cmd)

        def GetByAddress(self,address,date):
                cmd="SELECT p.id_no,p.id_type,p.time_in,p.fname,p.lname,p.sex,p.address,p.mobile_no,p.landline,v.vehicle_no,"
                cmd+="v.vehicle_type FROM %s as p left outer join %s as v on p.id_no=v.id_no WHERE p.address REGEXP '%s' "%(self.tableName1,self.tableName2,address)
                cmd+="AND p.date='%s';"%(date)
                return self.RunCommand(cmd)
        
        def GetByIDNo(self,id_no,date):
                cmd="SELECT p.id_no,p.id_type,p.time_in,p.fname,p.lname,p.sex,p.address,p.mobile_no,p.landline,v.vehicle_no,"
                cmd+="v.vehicle_type FROM %s as p left outer join %s as v on p.id_no=v.id_no WHERE p.id_no='%s' "%(self.tableName1,self.tableName2,id_no)
                cmd+="AND p.date='%s';"%(date)
                return self.RunCommand(cmd)
                

        def GetLast30Visits(self,date):
                cmd="SELECT p.id_no,p.id_type,p.time_in,p.fname,p.lname,p.sex,p.address,p.mobile_no,p.landline,v.vehicle_no,"
                cmd+="v.vehicle_type FROM %s as p left outer join %s as v on p.id_no=v.id_no WHERE p.date='%s' ORDER BY p.time_in DESC LIMIT 30;"%(self.tableName1,self.tableName2,date)
                return self.RunCommand(cmd)
        
        def GetLast30TwoWheelers(self,date):
                cmd="SELECT p.id_no,p.id_type,p.time_in,p.fname,p.lname,p.sex,p.address,p.mobile_no,p.landline,v.vehicle_no,"
                cmd+="v.vehicle_type FROM %s as p left outer join %s as v on p.id_no=v.id_no WHERE p.date='%s' "%(self.tableName1,self.tableName2,date)
                cmd+="and v.vehicle_type='Motorcycle' ORDER BY p.time_in DESC LIMIT 30;"
                return self.RunCommand(cmd)
        
        def GetLast30FourWheelers(self,date):
                cmd="SELECT p.id_no,p.id_type,p.time_in,p.fname,p.lname,p.sex,p.address,p.mobile_no,p.landline,v.vehicle_no,"
                cmd+="v.vehicle_type FROM %s as p left outer join %s as v on p.id_no=v.id_no WHERE p.date='%s' "%(self.tableName1,self.tableName2,date)
                cmd+="and v.vehicle_type !='Motorcycle' ORDER BY p.time_in DESC LIMIT 30;"
                return self.RunCommand(cmd)
        
        def GetLast30Pedestrians(self,date):
                cmd="SELECT p.id_no,p.id_type,p.time_in,p.fname,p.lname,p.sex,p.address,p.mobile_no,p.landline FROM %s AS p WHERE date='%s' AND  id_no not in"%(self.tableName1,date)
                cmd+="( SELECT p.id_no from %s as p inner join %s as v on v.id_no=p.id_no);"%(self.tableName1,self.tableName2)
                return self.RunCommand(cmd)
                
        def GetNumberOfPersons(self,date):
                cmd="SELECT COUNT(p.time_in)  FROM %s as p WHERE p.date='%s';"%(self.tableName1,date)
                return self.RunCommand(cmd)
        
        def GetNumberOfMales(self,date):
                cmd="SELECT COUNT(p.time_in) FROM %s as p where p.sex='male' and p.date='%s';"%(self.tableName1,date)
                return self.RunCommand(cmd)
        def GetNumberOfFemales(self,date):
                cmd="SELECT COUNT(p.time_in) FROM %s as p where p.sex='female'  and p.date='%s';"%(self.tableName1,date)
                return self.RunCommand(cmd)
                
        def GetNumberOfStudents(self,date):
                cmd="SELECT COUNT(p.time_in) FROM %s as p where p.id_type='Student Id'  and p.date='%s';"%(self.tableName1,date)
                return self.RunCommand(cmd)
                
        def GetNumberOfStaff(self,date):
                cmd="SELECT COUNT(p.time_in) FROM %s as p where p.id_type='Staff Id'  and p.date='%s';"%(self.tableName1,date)
                return self.RunCommand(cmd)
                
        def GetNumberOfOutsiders(self,date):
                cmd="SELECT COUNT(p.time_in) FROM %s as p where p.id_type !='Staff Id' AND p.id_type!='Student Id'  and p.date='%s';"%(self.tableName1,date)
                return self.RunCommand(cmd)

                
        def GetColumns1(self):
                return self.RunCommand("SHOW COLUMNS FROM %s;" % self.tableName1)
        
        def GetColumns2(self):
                return self.RunCommand("SHOW COLUMNS FROM %s;" % self.tableName2)
        def GetColumns3(self):
                return self.RunCommand("SHOW COLUMNS FROM %s;" % self.tableName3)
        

        def RunCommand(self, cmd):
                print ("RUNNING COMMAND: " + cmd)
                try:
                        self.cursor.execute(cmd)
                except mysql.connector.Error as err:
                        print ('ERROR MESSAGE: ' + str(err.msg))
                        print ('WITH ' + cmd)
                try:
                        msg = self.cursor.fetchall()
                except:
                        msg = self.cursor.fetchone()
                return msg

        def AddEntryToTable1(self,id_no,id_type,fname,lname,sex,address,mobile_no,landline):
                cmd = " INSERT INTO " + self.tableName1 + " (date, time_in,id_no,id_type,fname,lname,sex,address,mobile_no,landline)"
                cmd += " VALUES ('%s', '%s', '%s','%s','%s','%s','%s','%s','%s','%s' );" % (self.date1, self.time,id_no,id_type,fname,lname,sex,address,mobile_no,landline)
                self.RunCommand(cmd)

        def AddEntryToTable2(self,id_no,vehicle_no,vehicle_type):
                cmd="INSERT INTO "+self.tableName2 +"(date,time_in,id_no,vehicle_no,vehicle_type)"
                cmd+="VALUES('%s','%s','%s','%s','%s');"%(self.date1,self.time,id_no,vehicle_no,vehicle_type)
                self.RunCommand(cmd)

        def AddEntryToTable3(self,id_no,date1,time,whom_to_visit,relationship,purpose_of_visit):
                cmd="INSERT INTO "+self.tableName3 +"(date,time_in,id_no,whom_to_visit,relationship,purpose_of_visit)"
                cmd+="VALUES ('%s','%s','%s','%s','%s','%s');"%(date1,time,id_no,whom_to_visit,relationship,purpose_of_visit)
                print type(date1)
                print type(time)
                self.RunCommand(cmd)

        def __del__(self):
                self.cnx.commit()
                self.cursor.close()
                self.cnx.close()

##===============================================
##===============================================


if __name__ == '__main__':
        db = 'icpms'
        tableName1 = 'person'
        tableName2='vehicle'
        tableName3='purpose'
        dbu = DatabaseUtility(db, tableName1,tableName2,tableName3)

        # dbu.AddEntryToTable ('testing')
        # dbu.AddEntryToTable ('testing2')
        #print (dbu.GetColumns())
        #print (dbu.GetTable())
        

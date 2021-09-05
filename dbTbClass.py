import sqlite3


class Db:

    dbName = ''  

    dbConnect = None 

    def __init__(self, dbName = None):
        self.dbName = dbName
        self.dbConnect = None

        if dbName:
            self.open(dbName) 

    def open(self, dbName):
        try:
            self.dbConnect = sqlite3.connect(self.dbName)
            print ("connected")
        except sqlite3.Error as e:
            print ("error connectiong to database")   

db = Db("testDb3")



class Tb(Db):

    tbCursor = None
    fieldsNameType = None


    def __init__(self, dbName, tbName):
        self.tbName = tbName
        super().__init__(dbName)
        self.tbCursor = self.dbConnect.cursor()


    def createTable(self, fieldsNameType):
        #self.tbDict = tbDict
 
##        print (self.tbName)
       
        sql = "CREATE TABLE IF NOT EXISTS "+ self.tbName + " (id INTEGER PRIMARY KEY AUTOINCREMENT, "+ fieldsNameType + ") "
#        sql_create_projects_table = "CREATE TABLE IF NOT EXISTS self.tbName (id INTEGER PRIMARY KEY AUTOINCREMENT, fieldsNameType)"
#        sql_create_projects_table = "CREATE TABLE IF NOT EXISTS projects1 (id INTEGER PRIMARY KEY AUTOINCREMENT, fieldsNameType)"


##        print (sql_create_projects_table)
        self.tbCursor.execute (sql) 
        print ("table created") 

        self.dbConnect.commit()

#        self.dbConnect.close()



    def tbInsert(self, tbValues):
#        sql = 'insert into projects (name, begin_date, end_date) VALUES (?, ?, ?)', tbValues
        sql = "insert into "+ self.tbName + " (name, begin_date, end_date) VALUES ('name2', 'begin_date2', 'end_date2')"


        try:
            self.tbCursor.execute(sql)
            self.dbConnect.commit()
        except sqlite3.Error as e:
            print ("error insert to database")   



    def tbList(self):
#        sql = "SELECT * FROM "+ self.tbName
        sql = "SELECT * FROM tb2"
        print  (sql)        
        for row in self.tbCursor.execute(sql):
            print(row)

#    def createTable('tbDict1')
        

#    def commit()
#        self.db

tb = Tb('db1', 'tb2')    

#tbFieldsNameType = ['name TEXT', 'begin_date TEXT', 'end_date TEXT']
tbFieldsNameType = "name TEXT, begin_date TEXT, end_date TEXT"

#tb.createTable()
tb.createTable(tbFieldsNameType)

#tb.tbInsert(['name1', 'begin date 1', 'end date 2'])
tb.tbInsert()

tb.tbList()

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

        try:
            self.tbCursor.execute (sql) 
            print ("table created") 
            self.dbConnect.commit()
        except sqlite3.Error as e:
            print ("error create table in database")   
#        self.dbConnect.close()



    def tbInsert(self, tbFieldsKey, tbFieldsValue):
#        sql = 'insert into projects (name, begin_date, end_date) VALUES (?, ?, ?)', tbValues
#        sqlInsert = "insert into "+ self.tbName + " (name, begin_date, end_date) VALUES ('name2', 'begin_date2', 'end_date2')"
        
#
#        sqlInsert = "insert into "+ self.tbName + " (name, begin_date, end_date) VALUES ("+ tbValues +")"
#        sqlInsert = "insert into "+ self.tbName + " (id " + tbFieldsKey + ") VALUES ( ?, ?, ?, ? ), " + tbFieldsValue 

        tbFieldsValueCount = len(tbFieldsValue)
        print (tbFieldsValueCount)
        questionMark = '?' 
#        for x in tbFieldsValueCount:
#        for x+1 in tbFieldsValue:
 
        for i in range(1, len(tbFieldsValue)):
            questionMark = questionMark + " ,?"               



        print (questionMark)

#        sqlInsert = "insert into "+ self.tbName + " (" + tbFieldsKey + ") VALUES (?, ?, ?)"
        sqlInsert = "insert into "+ self.tbName + " (" + tbFieldsKey + ") VALUES ( " + questionMark +")"
        print (sqlInsert)
#        print ("after  insert\n")
#        print (tbFieldsValue)
#        print ("\nafter  tbFuîeld\n")
         
#        tbFieldsVal = tbFieldsValue
#        print (tbFieldsVal)
#        name = "n123"
#        begin_date = "bd123"
#        end_date = "ed123"

        name = tbFieldsValue[0]
        begin_date = tbFieldsValue[1]
        end_date = tbFieldsValue[2]
        data_tuple = (name, begin_date, end_date)


        try:
#            self.tbCursor.execute(sqlInsert, tbFieldsValue)
            self.tbCursor.execute(sqlInsert, data_tuple)
            self.dbConnect.commit()
        except sqlite3.Error as e:
            print ("error insert to database")   



    def tbList(self):
#        sql = "SELECT * FROM "+ self.tbName
        sqlList = "SELECT * FROM tb2"
        print  (sqlList)        
        for row in self.tbCursor.execute(sqlList):
            print(row)



#    def tbInsert(self, tbFieldsKey, tbFieldsValue):


    def tbDelete(self, ids):
#        sqlDelete = 'DELETE FROM self.tbName WHERE id=?'        
#        sqlDelete = 'DELETE FROM tb2 WHERE id=?'        
#        sqlDelete = 'DELETE FROM ' + self.tbName + ' WHERE id=3'        
        sqlDelete = "DELETE FROM "+ self.tbName+" WHERE id=?"        
        try:

            print ( sqlDelete)
            print (ids)           
#            self.tbCursor.execute(sqlDelete, id)
#            self.tbCursor.execute(sqlDelete, 2)
#            self.tbCursor.execute(sqlDelete, id)
            self.tbCursor.execute(sqlDelete, (ids,))
#            self.tbCursor.execute("DELETE FROM tb2 WHERE id=?", (ids,))
#            self.tbCursor.execute("DELETE FROM tb2 WHERE id=5")

#            self.cursor.execute(sqlDelete, (id,))
            self.dbConnect.commit()

        except sqlite3.Error as e:
            print ("error delete to database")   




'''

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


'''

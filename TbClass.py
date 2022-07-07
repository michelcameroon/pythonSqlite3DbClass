import sqlite3
from sqlite3 import Error

class TbClass:


#    self.dbName = ""

    def __init__(self):
#        self.sqlite_file = "address.db"
        self.conn = None            # set the placeholder for the connection
#        self.create_connection()    # create the connection
#        self.drop_table()           # drop the table if it exists
#        self.create_table()         # creation the dummy table
#        self.create_data()          # for filling up the database with dummy data

        

    def createConnection(self, dbName):
        """ create a database connection to the SQLite database
            specified by db_file
        :db_file: self.sqlite_file
        :creates : self.conn Connection object
        """
        self.dbName = dbName 

        try:
#            self.conn = sqlite3.connect(self.sqlite_file)
            self.conn = sqlite3.connect(self.dbName)
            self.conn.row_factory = sqlite3.Row  #this for getting the column names!
        except Error as e:
            print("create_connection: {}".format(e))
        else:
            print("Database connection created!")


#    def drop_table(self, tbName):
    def drop_table(self, sql):
        """
        small function to drop the dummy table
        """
        #sql = '''DROP TABLE IF EXISTS tbName '''
        #sql = "DROP TABLE IF EXISTS 'customers222'"
        #sql = "DROP TABLE IF EXISTS 'tbName'"
        #print ("sql= " + sql)
        #sql = "DROP TABLE IF EXISTS " +  tbName
        #sql = "DROP TABLE IF EXISTS 'customers222'" 
        #print ("sql = ")
        print (sql)
        try:
            self.conn.execute(sql)
        except Error as e:
            print("drop_table: {}".format(e))
        else:
            print("Table dropped")

    def tbCreate(self, sql):
        #sql = "create table ' " + createTb + " ' ('id' integer primary key, name text)"
        #sql = "create table 'test4' ('id' integer primary key, 'name' text)"
        print(sql)
        
        try:
            self.conn.execute(sql)
        except Error as e:
            print("create_table: {}".format(e))
        else:
            print("Table created!")




#    def insert(self, insert, val):
    def insert(self, insert):
       try:
           cur = self.conn.cursor()
#           cur.execute(insert, val)
           cur.execute(insert)
#           cur.execute("insert into tb4 (name, salary) values(?, ?)", "[('henry', 15000)]"
#)

           self.conn.commit()
       except Error as e:
           print("insert: {}".format(e))
       else:
            print("Insert ok")

#    def insert(self, insert, val):


    def update(self, update):
       try:
           cur = self.conn.cursor()
#           cur.execute(insert, val)
           cur.execute(update)
#           cur.execute("insert into tb4 (name, salary) values(?, ?)", "[('henr>
#)

           self.conn.commit()
       except Error as e:
           print("insert: {}".format(e))
       else:
            print("update ok")


    def delete(self, delete):
        try:
            cur = self.conn.cursor()
#            cur.execute(insert, val)
            cur.execute(delete)
#           cur.execute("insert into tb4 (name, salary) values(?, ?)", "[('henr>
#)

            self.conn.commit()
        except Error as e:
            print("deleete: {}".format(e))
        else:
            print("delete ok")



    def insertval(self, insert, val):
       try:
           cur = self.conn.cursor()
#           cur.execute(insert, val)
           cur.execute(insert, val)
#           cur.execute("insert into tb4 (name, salary) values(?, ?)", "[('henry', 15000>
#)

           self.conn.commit()
       except Error as e:
           print("insertval: {}".format(e))
       else:
            print("Insertval ok")




    def create_data(self):
        addresses = [("Jansen", "Blaak 928", "Rotterdam"), ("Klaasen", "Maasberglaan 23", "Rotterdam"),
                     ("Sluijsen", "Maasstraat 25", "Barendrecht"), ("de Vos", "Meent 198", "Rotterdam"),
                     ("De Notenkraker", "Pennylane 15", "Amsterdam")]

        sql = """INSERT INTO `addresses` (`name`, `address`, `city`)
                            VALUES (?, ?, ?)"""

        try:
            cur = self.conn.cursor()
            cur.executemany(sql, addresses)
            self.conn.commit()

        except Error as e:
            print("create_table: {}".format(e))
        else:
            print("Insert of fake data!")



    def list(self, sql):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            return cur.fetchall()
        except Error as e:
            print("list: {}".format(e))
        
    def listId(self, sql):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            return cur.fetchall()
        except Error as e:
            print("list: {}".format(e))



    def fieldList(self, tbName):
        try:
            #cur = self.conn.cursor()fieldList = self.conn.execute("PRAGMA table_info(tbName)").fetchall()
            cur = self.conn.cursor()
#            fieldList = self.conn.execute("PRAGMA table_info(tbName)").fetchall()
#            fieldList = cur.execute("PRAGMA table_info(tbName)").fetchall()
#            fieldList = cur.execute("PRAGMA table_info('tb4')").fetchall()
#            print(tbName)
#            fieldList = cur.execute("PRAGMA table_info(tbName)").fetchall()
            cmd = "PRAGMA table_info(" + tbName + ")"
#            fieldList = cur.execute("PRAGMA table_info(tbName)").fetchall()
            fieldList = cur.execute(cmd).fetchall()
#            print(fieldList)

#            exit()
#            fieldList = conn.execute(f'PRAGMA table_info({table_name});').fetchall()
#            fieldList = self.conn.execute(f'PRAGMA table_info(tbName);').fetchall()
            #pragma = "PRAGMA table_info(tbName)"
            #fieldList = cur.execute(pragma)
            return fieldList            
        except Error as e:
            print("fieldlist: {}".format(e))
      
    def fieldListNames(self, tbName):
        try:
            #cur = self.conn.cursor()

            tbFields = self.fieldList(tbName)
            print (tbFields)

            namesInString = ''
            y=0

#            for listFieldsName in listFieldsNames:
            for listFieldsName in tbFields:
#    print (listFieldsName)
#    print (len(listFieldsName))
                if y==0:
                    namesInString = listFieldsName[1]
                else:
                    namesInString = namesInString + ' , ' + str(listFieldsName[1])
                    
                y=y+1

#print (namesInString)
            print (namesInString)




            ''' 
        listFieldsNames = []

        for tbField in tbFields:
            print(tbField)
            print ("fields = " + tbField[1])
        
#            for fields in tbFields.items:      #mistake
#            for tbField in tbFields:      #mistake
#                for fields in tbField:
#                    print ("fields : " + fields)
#                    print ("fields : " + str(fields))
                #listFieldsNames.append(fields[1])    

#                    print ("fields = " + fields[1])
#                    listFieldsNames.append(fields[1])
#                    listFieldsNames.append(fields[1])
#                    listFieldsNames.append(fields)
#                    print ("listFieldsNames : " + str(listFieldsNames))
                #for field in fields:
                #    print(field)
            '''      
#        return listFieldsNames
            return namesInString               

        except Error as e:
            print("fieldListNames: {}".format(e))


    def fieldListNamesType(self, tbName):
        try:
            #cur = self.conn.cursor()

             tbFields = self.fieldList(tbName)
             print (tbFields)


#            tbFieldsNames = self.fieldListNames(tbName)
#            print (tbFieldsNames)
             namesTypeInString = ''
             y=0

#            for listFieldsName in listFieldsNames:
             for listFieldsNameType in tbFields:
#    print (listFieldsName)
#    print (len(listFieldsName))
                 if y==0:
                     namesTypeInString = listFieldsNameType[2]
                 else:
                     namesTypeInString = namesTypeInString + ' , ' + str(listFieldsNameType[2])

                    
                 y=y+1

#print (namesInString)
             print (namesTypeInString)

             return namesTypeInString

        except Error as e:
            print("fieldListNamesType: {}".format(e))



    
    def get_rows(self, fields):
        """
        Small function for getting multiple rows
        :param fields:
        :return: rows
        """
        try:
            sql = '''SELECT `name`, `address`, `city` 
                     FROM `addresses` WHERE `city` = ?'''

            cur = self.conn.cursor()
            cur.execute(sql, fields)
            return cur.fetchall()

        except Error as e:
            print("get_row: {}".format(e))

    def get_row(self, fields):
        try:
            sql = '''SELECT `name`, `address`, `city` 
                     FROM `addresses` WHERE `city` = ?'''

            cur = self.conn.cursor()
            cur.execute(sql, fields)
            return cur.fetchone()

        except Error as e:
            print("get_row: {}".format(e))


    def tbNames(self, sql):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            return cur.fetchall()
        except Error as e:
            print("list: {}".format(e))






    def close_conn(self):
        try:
            self.conn.close()
        except Error as e:
            print("close_conn: {}".format(e))
        else:
            print("Connection closed!")


if __name__ == "__main__":
    print('TbClass')
#    s = RowsKeys()
'''
    s = TbClass()

    s.createConnection("database.db")

    # get one row and print as dictionary

    print("Return one Row")

    fields = ["Barendrecht"]
    data = s.get_row(fields)
    print(dict(data))

    print("==============")

    print("Return multiple Rows")
    # get multiple rows and print as dictionary
    fields = ["Rotterdam"]
    rows = s.get_rows(fields)
    for row in rows:
        print(dict(row))

    print()
    s.close_conn()
'''

from dbTbClass import Db, Tb


tb = Tb('db1', 'tb2')    

#tbFieldsNameType = ['name TEXT', 'begin_date TEXT', 'end_date TEXT']
tbFieldsNameType = "name TEXT, begin_date TEXT, end_date TEXT"

#tb.createTable()
tb.createTable(tbFieldsNameType)

#tb.tbInsert(['name1', 'begin date 1', 'end date 2'])
tbValues = ['n12', 'bd12', 'ed12']
#tb.tbInsert("name, begin_date, end_date", "('name = name11', 'begin_date = begin_date_11', 'end_date = end_date_11')")
tb.tbInsert("name, begin_date, end_date", tbValues)
#tb.tbInsert("name, begin_date, end_date", "[('name11', 'begin date 11', 'end date 11')]")

tb.tbList()

tb.tbDelete(80)

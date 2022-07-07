from TbClass import  TbClass

import sqlite3


tb = TbClass()

tbName = "load"

tb.createConnection("solarCalc.db")

#tbFields = tb.fieldList(tbName)
tbFields = tb.fieldList("load")
print(tbFields)
tb.close_conn()


#for tbField in tbFields.items:		#mistake


#listFields = []

#listFieldsNames = []

tb.createConnection("solarCalc.db")


#listFieldsNames = tb.fieldListNames("load")
listFieldsNames = tb.fieldList("load")

tb.close_conn()
#print("listFiledsNames : " + str(listFieldsNames))

namesInString = ''
y=0

for listFieldsName in listFieldsNames:
#    print (listFieldsName)
#    print (len(listFieldsName))
     if y==0:
        namesInString = listFieldsName[1]
     else:
        namesInString = namesInString + ' , ' + str(listFieldsName[1])
     y=y+1

#print (namesInString)
print (namesInString)

insert = "INSERT INTO 'load'  ( " + namesInString + " ) values ('', 'name1', 3, 4, 5)"

print (insert)

# from TbClass.fieldListNames()

print ("***************************************")

tb.createConnection("solarCalc.db")


fieldListNames = tb.fieldListNames('load')

print (fieldListNames)

print ("==================================")

tb.createConnection("solarCalc.db")


fieldListNamesType = tb.fieldListNamesType('load')

print (fieldListNamesType)





'''    
    i=0
    for listFieldN in listFieldsName:
        print(listFieldN)
        if y==0:
#            namesInString.append(str(listFieldN))
#            namesInString = listFieldN
            namesInString = namesInString + str(listFieldN)
            print (namesInString)
        else:
            namesInString = namesInString + ' , ' + str(listFieldN)
        i=i+1
    y=y+1    
#        namesInString = namesInString + str(listFieldN[1]) + ','
#        namesInString = namesInString + listFieldsName  + ' , '
#        namesInString = namesInString + str(listFieldN)  + ' , '

print ("namesInString = " + namesInString)

insert = "INSERT INTO 'load' (nameInString) values ('', 'name1', 3, 4, 5)"

#print (insert)
'''
'''
for listFieldsName in listFieldsNames:
    print (listfieldsName)     
for tbField in tbFields:
    print(tbField)
#    for fields in tbFields.items:	#mistake
    for fields in tbFields:
        print (fields)
        listFields.append(fields[1])	

        print ("fields = " + fields[1])
        listFieldsNames.append(fields[1])
        for field in fields:
            print(field)


for listFieldsName in listFieldsNames:
    print (listFieldsName)
'''

'''
for listField in listFields:
    print("fieldName : " + listField)

#dictFields = dict([])
dictFields = dict{}


for tbField in tbFields:
    dictFields[name].append(tbField)
'''

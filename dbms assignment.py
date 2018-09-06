#Q.1- Write a python script to create a databse of students named Students.
import sqlite3

con = sqlite3.connect('Students.db')
print(" database successfully opened")
con.close()

#Q.2- Take students name and marks(between 0-100) as input from user 10 times using loops.

try:
    con = sqlite3.connect('Students.db')
    
    cursor = con.cursor()
    
    query = 'create table students(Name varchar(10) primary key, \
    Marks int(3))'
    
    cursor.execute(query)
    
    print('Table created !')
    con.commit()
    
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('error occured: ', e)
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE!')

l = []
i=0
while(i<10):
    try:
        name = input("Enter the name: ")
        marks = int(input('Enter your Marks: '))
        if(marks<0 or marks >100):
            raise ValueError('Invalid entry of marks')
            i=i-1
        else:
            t = name,marks
            l.append(t)
            i=i+1
    except  ValueError as msg:
        print(msg)

#Q.3- Add these values in two columns named "Name" and "Marks" with the appropriate data type.
try:
    con = sqlite3.connect('Students.db')
    
    cursor = con.cursor()
    
    query = "insert into students(Name, Marks) \
    values(?,?)"
    
    records = l
    
    cursor.executemany(query, records)
    
    con.commit()
    
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE!!')

#Q.4- Print the names of all the students who scored more than 80 marks.

try:
    con = sqlite3.connect('Students.db')
    
    cursor = con.cursor()
    
    query = 'select * from students where Marks > 80'
    
    cursor.execute(query)
    
    data = cursor.fetchall()

    print("Name of Student who scored greater then 80 are :")
    for row in data:
        print('Name: {}'\
             .format(row[0]))
    
except sqlite3.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE!!')


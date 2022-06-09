
import mysql.connector  
myconn = mysql.connector.connect(host ="localhost",user="root",passwd="1234567",database="python_database")
print(myconn)
cur = myconn.cursor()
print(cur)
print("Database Connected Successfully")
x=1
while x==1:
    print("1.for insertion")
    print("2.for deletion")
    print("3.for search")
    print("4.for view table")
    ch = int(input("Enter your choice: "))


    if ch==1:
        a=input("Enter Name: ")
        b=int(input("Enter Regno: "))
        c=int(input("Enter Age: "))
        d=input("Enter Gender: ")
        e=input("Enter Community: ")
        f=int(input("Enter Mobile number: "))
        g= input("Enter Mail: ")
        h= input("Enter CGPA: ")
        sql = "insert into student_data(Name,Regno,Age,Gender,Community,Mobile,Email,CGPA) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(a,b,c,d,e,f,g,h)
        try:
            cur.execute(sql,val)
            myconn.commit()
        except Exception as e:
            print(e)
            myconn.rollback()
        print(cur.rowcount,"Record Inserted Succesfully")


    if ch==2:
        b=int(input("Enter Regno: "))
        sql = "delete from student_data where Regno =%s"
        val = (b,)
        try:
            cur.execute(sql,val)
            print(cur.rowcount,"record(s) deleted")
            myconn.commit()
            print("Deleted Sucessfully")
        except Exception as e:
            print(e)
            myconn.rollback()

        
    if ch ==3:
        b=int(input("Enter Regno: "))
        sql = "select*from student_data where Regno =%s"
        var = (b,)
        try:
            cur.execute(sql,var)
            y= cur.fetchall()
            myconn.commit()
            if(len(y)==0):
                print("No Records Found")
            for i in y:
                print(i)
        except Exception as e:
            print(e)
            myconn.rollback()

    if ch==4:
        sql = "select*from student_data"
        try:
            cur.execute(sql)
            y = cur.fetchall()
            myconn.commit()
            if(len(y)==0):
                print("No Records Found")
            for i in y:
                print(i)
        except Exception as e:
            print(e)
            myconn.rollback()


    x= int(input("Press 1 to Continue............"))
myconn.close()
        




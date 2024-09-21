import mysql.connector

try :
    mydatabase = mysql.connector.connect(host = 'localhost',
                                         user = "root",
                                         password = "",
                                         database = "mysql")
    print("Data is connected Successfully..")
except Exception as e :
    print("Exception",e)
    
cursor = mydatabase.cursor()

def register(data):
    try:
        cursor.execute("INSERT INTO `user_auth`(`Username`, `Email`, `Password`,'Retype Password') VALUES (%s,%s,%s)",data)
        mydatabase.commit()
        return True
    except Exception as e :
        print("Exception",e)
        return False
    
def get_all():
    try:
        cursor.execute("SELECT * FROM `user_auth`")
        return cursor.fetchall()
    except Exception as e :
        print("Exception as ",e)
        
def login(data):
    try:
        cursor.execute('SELECT * FROM `user_auth` WHERE `email`=%s and `password`=%s',data)
        return cursor.fetchone()
    except Exception as e :
        print("Exception as ",e)
        
def deleteuser(id):
    try:
        cursor.execute("DELETE FROM `user_auth` WHERE id=%s",id)
        mydatabase.commit()
        return True
    except Exception as e :
        print("Exception as ",e)
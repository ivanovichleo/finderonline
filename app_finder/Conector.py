import mysql.connector
class conectors:

    def __init__(self,host,user,pword) -> None:
        self.host=host
        self.username=user
        self.password=pword

    def conection(self):
        db=mysql.connector.connect(

        host=self.host,
        user=self.username
        password=self.password
        
        # host="Ivanovichleo.mysql.pythonanywhere-services.com",
        # user="Ivanovichleo"
        # password="Findercard59"
        return db
    )

    def insert_room(self,room):
        
        db=self.conection
        Mycursor=db.cursor()
        
        sql="INSERT INTO Room (code) Values " + room

        Mycursor.execute(sql)
        db.commit()


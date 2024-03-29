import mysql.connector


class LessonDa:
    def connect(self, ):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root123",
            database="mft"
        )
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, name, teacher, discription):
        self.connect()
        self.cursor.execute("INSERT INTO PERSON (name, teacher , discription) VALUES (%s,%s ,%s)",
                            [name, teacher, discription])
        self.connection.commit()
        self.disconnect()

    def edit(self, id, name, teacher,discription):
        self.connect()
        self.cursor.execute("UPDATE PERSON SET NAME=%s, TECHER=%s,DISCRIPTION=%s WHERE ID=%s",
                            [name,teacher, discription, id])
        self.connection.commit()
        self.disconnect()

    def remove(self, id):
        self.connect()
        self.cursor.execute("DELETE FROM LESSON WHERE ID=%s",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM LESSON ORDER BY TEACHER AND DISCRIPTION")
        lesson_list = self.cursor.fetchall()
        self.disconnect()
        return  lesson_list if  lesson_list else None

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("SELECT * FROM LESSON WHERE ID=%s",
                            [id])
        lesson = self.cursor.fetchall()
        self.disconnect()
        return  lesson[0] if  lesson else None

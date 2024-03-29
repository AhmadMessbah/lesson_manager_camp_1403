import mysql.connector


class LessonDa:
    def connect(self,):
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

    def save(self, name_lesson, teacher_name, description):
        self.connect()
        self.cursor.execute("INSERT INTO lesson (name_lesson, teacher_name , description) VALUES (%s,%s ,%s)",
                            [name_lesson, teacher_name, description])
        self.connection.commit()
        self.disconnect()

    def edit(self, id, name_lesson, teacher_name,discription):
        self.connect()
        self.cursor.execute("UPDATE lesson SET name_lesson=%s, teacher_name=%s,description=%s WHERE ID=%s",
                            [name_lesson,teacher_name, discription, id])
        self.connection.commit()
        self.disconnect()

    def remove(self, id):
        self.connect()
        self.cursor.execute("DELETE FROM lesson WHERE ID=%s",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM lesson ORDER BY teacher_name AND description")
        lesson_list = self.cursor.fetchall()
        self.disconnect()
        return  lesson_list if  lesson_list else None

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("SELECT * FROM lesson WHERE ID=%s",
                            [id])
        lesson = self.cursor.fetchall()
        self.disconnect()
        return  lesson[0] if  lesson else None

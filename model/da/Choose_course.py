import mysql.connector

class PersonDa:
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
                                 # save person by name family grade
    def save(self,datetime_coure, person_id,lesson_id):
        self.connect()
        self.cursor.execute("INSERT INTO choose_course (datetime_coure, person_id,lesson_id) VALUES (%s,%s,%s)",
                            [datetime_coure, person_id,lesson_id])
        self.connection.commit()
        self.disconnect()

                                      # edit person by id name family grade
    def edit(self,datetime_course, person_id,lesson_id):
        self.connect()
        self.cursor.execute("UPDATE choose_course SET datetime_coure=%s, person_id=%s ,lesson_id=%s WHERE ID=%s",
                            [datetime_course, person_id,lesson_id])
        self.connection.commit()
        self.disconnect()

                                    # find all person by family grade
    def find_all(self):
        self.connect()
        self.cursor.execute("SELECT * FROM choose_course ORDER BY ")
        person_list = self.cursor.fetchall()
        self.disconnect()
        return person_list if person_list else None

                                      # find  person by id
    def find_by_id(self,id):
        self.connect()
        self.cursor.execute("SELECT * FROM choose_course WHERE ID=%s",
                            [id])
        person = self.cursor.fetchall()
        self.disconnect()
        return person[0] if person else None

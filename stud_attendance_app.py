import mysql.connector
class database():
    def __init__(self): # Initialize Database Configurations
        self._host = "127.0.0.1"
        self._port = 3306
        self._user = "root"
        self._password = "12345"
        self._database = "university"
        self.conn = None
        self.cursor = None
    def connect_db(self): # Establish connection to the database
        self.conn = mysql.connector.Connect(
            host = self._host,
            port = self._port,
            database = self._database,
            user = self._user,
            password = self._password,
        )
        self.cursor = self.conn.cursor() # Create cursor object
        print ("Connection Established!")

class attendancems(): # Functions to interact with database
    def Add_student (self,surname,last_name):
        query = ("INSERT INTO students (surname,last_name) VALUES (%s,%s)")
        values = (surname, last_name)
        db = database()
        db.connect_db()
        db.cursor.execute(query,values)
        db.conn.close()
        
    def add_lecturer(self,surname,last_name): # Adds a New Lecturer eg. George
        query = ("INSERT INTO lecturers (surname,last_name) VALUES (%s,%s)")
        values = (surname, last_name)
        db = database()
        db.connect_db()
        db.cursor.execute(query,values)
        db.conn.close()
    def create_class(self,lecturer_id,lecture_date,unit_id): # Creates a new class/lecture eg.Saturday 3pm
        query = ("INSERT INTO classes (lecturer_id,class_date,unit_id) VALUES (%s,%s,%s,%s)")
        values = (lecturer_id,lecture_date,unit_id)
        db = database()
        db.connect_db()
        db.cursor.execute(query,values)
        db.conn.close()
    def create_unit(self,unit_name,lecturer_id): # Registers a unit eg. ICT105
        query = ("INSERT INTO units (unit_name,lecturer_id) VALUES (%s,%s)")
        values = (unit_name,lecturer_id)
        db = database()
        db.connect_db()
        db.cursor.execute(query,values)
        db.conn.close()
    def submit_attendance(self,class_id,student_id,attendance): # Fills in the attendance of a student for a selected class
        query = ("INSERT INTO attendance (class_id,student_id,attendance) VALUES (%s,%s)")
        values = (class_id,student_id,attendance)
        db = database()
        db.connect_db()
        db.cursor.execute(query,values)
        db.conn.close()
    def attendance_report_by_student(self,student_id): # Fetches a student's attendance report
        query = ("""SELECT s.surname,a.class_id, u.unit_name,a.attendance FROM attendance AS a 
                 JOIN students AS s ON a.student_id = s.student_id JOIN unit AS u ON a.class_id = u.class_id
                  WHERE student_id = (%s)""")
        values = (student_id)
        db = database()
        db.connect_db()
        db.cursor.execute(query)
        results = db.cursor.fetchall()
        db.conn.close()
        return results
    def attendance_report_by_class(self,class_id): # Fetches a class's attendance report
        query = ("""SELECT s.surname,a.class_id, u.unit_name,a.attendance FROM attendance AS a 
                 JOIN students AS s ON a.student_id = s.student_id JOIN unit AS u ON a.class_id = u.class_id
                  WHERE class_id = (%s)""")
        values = (class_id)
        db = database()
        db.connect_db()
        db.cursor.execute(query)
        results = db.cursor.fetchall()
        db.conn.close()
        return results

db = database()  
db.connect_db()
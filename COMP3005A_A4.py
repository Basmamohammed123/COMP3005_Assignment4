import psycopg2

dbname = 'new_database'
user = 'postgres'
password = 'Basma2002'
host = 'localhost' 
port = '5432'

def create_database():
    auto_commit = psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
    connection = psycopg2.connect(user=user, password=password, host=host, port=port)
    connection.set_isolation_level(auto_commit)
    cursor = connection.cursor() # Create cursor object 
    cursor.execute("CREATE database " + dbname) # Create database
    connection.commit() # Saves changes
    connection.close() # Closes the connection
    
def create_student_table():
    # Connect to the PostgreSQL
    connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cursor = connection.cursor() # Create cursor object 
    
    table_to_create = """
            CREATE TABLE IF NOT EXISTS students (
                student_id SERIAL PRIMARY KEY,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                enrollment_date DATE 
            )
        """
    cursor.execute(table_to_create) # Create students table
    connection.commit() # Saves changes
    connection.close() # Closes the connection

def getAllStudents():
    connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    
    cursor = connection.cursor() # Create cursor object 
    cursor.execute("SELECT * FROM students") # Retrieves everything in students table
    students = cursor.fetchall() # fetches all the rows in the query
    for student in students:
        print(student) # Prints students info
    connection.close() # Closes the connection
    
def addStudent(first_name, last_name, email, enrollment_date):
    connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cursor = connection.cursor() # Create cursor object 
    cursor.execute("""
            INSERT INTO students (first_name, last_name, email, enrollment_date)
            VALUES (%s, %s, %s, %s)
        """, (first_name, last_name, email, enrollment_date))
    connection.commit()
    connection.close()

def updateStudentEmail(student_id, new_email):
    connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cursor = connection.cursor() # Create cursor object 
    cursor.execute("""
            UPDATE students
            SET email = %s
            WHERE student_id = %s
        """, (new_email, student_id))
    connection.commit()
    connection.close()

def deleteStudent(student_id):
    connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cursor = connection.cursor() # Create cursor object 
    cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    connection.commit()
    connection.close()

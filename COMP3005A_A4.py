import psycopg2

def create_student_table():
    # Connect to the PostgreSQL
    connection = psycopg2.connect('dbname=class user=postgres password=Basma2002 host=localhost port=5432')
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
    connection = psycopg2.connect('dbname=class user=postgres password=Basma2002 host=localhost port=5432')
    
    cursor = connection.cursor() # Create cursor object 
    cursor.execute("SELECT * FROM students") # Retrieves everything in students table
    students = cursor.fetchall() # fetches all the rows in the query
    for student in students:
        print(student) # Prints students info
    connection.close() # Closes the connection
    
def addStudent(first_name, last_name, email, enrollment_date):
    connection = psycopg2.connect('dbname=class user=postgres password=Basma2002 host=localhost port=5432')
    cursor = connection.cursor() # Create cursor object 
    cursor.execute("""
            INSERT INTO students (first_name, last_name, email, enrollment_date)
            VALUES (%s, %s, %s, %s)
        """, (first_name, last_name, email, enrollment_date))
    connection.commit()
    connection.close()

def updateStudentEmail(student_id, new_email):
    connection = psycopg2.connect('dbname=class user=postgres password=Basma2002 host=localhost port=5432')
    cursor = connection.cursor() # Create cursor object 
    cursor.execute("""
            UPDATE students
            SET email = %s
            WHERE student_id = %s
        """, (new_email, student_id))
    connection.commit()
    connection.close()

def deleteStudent(student_id):
    connection = psycopg2.connect('dbname=class user=postgres password=Basma2002 host=localhost port=5432')
    cursor = connection.cursor() # Create cursor object 
    cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_student_table() # Creates students table

    # Insert a new students
    addStudent('John', 'Doe', 'john.doe@example.com', '2023-09-01')
    addStudent('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01')
    addStudent('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
    getAllStudents()

    #Update the email of the first student
    updateStudentEmail(1, 'john@example.com')
    getAllStudents()    
    
    #Deletes the record of the student with the specified_id
    deleteStudent(1)
    getAllStudents()
    

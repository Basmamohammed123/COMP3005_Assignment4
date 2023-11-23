# COMP3005_Assignment4

To be able to connect to your PostgreSQL, you must first change the following variables
to match with the information of your PostgreSQL: user, password, host, port

def create_database(): Creates new database

create_student_table(): This function creates a students table in the database.

getAllStudents(): This function retrieves all of the information found in the students table 

addStudent(first_name, last_name, email, enrollment_date): This function adds a student in the students table. It takes four paramters: first_name, last_name, email, and enrollment_date.

updateStudentEmail(student_id, new_email): This function changes the email to "new_email" of the student with the student id "student_id".

deleteStudent(student_id): This function deletes the student from the students table with a student id "student_id".

To compile the code, run the following:

create_database() # Creates new database

create_student_table() # Creates students table

#Inserts new students

addStudent('John', 'Doe', 'john.doe@example.com', '2023-09-01')

addStudent('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01')

addStudent('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')

#Update the email of the first student

updateStudentEmail(1, 'john@example.com')
  
#Deletes the record of the student with the specified_id

deleteStudent(1)

#Returns all information found in the table

getAllStudents()

Video Demo: 

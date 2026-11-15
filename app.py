from getpass import getpass
from datetime import date

import psycopg

def menu():
    """Prompt for menu choices and run the selected database operation."""
    while True:
        print("\n1. List students")
        print("2. Add student")
        print("3. Update student email")
        print("4. Delete student")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                getAllStudents()

            elif choice == "2":
                first_name = input("First name: ").strip()
                last_name = input("Last name: ").strip()
                email = input("Email: ").strip()
                date_text = input("Enrollment date (YYYY-MM-DD, or blank): ").strip()

                # Convert a blank date to None, which psycopg sends as SQL NULL.
                enrollment_date = date.fromisoformat(date_text) if date_text else None
                addStudent(first_name, last_name, email, enrollment_date)
                print("Student added.")

            elif choice == "3":
                student_id = int(input("Student ID: "))
                new_email = input("New email: ").strip()
                updateStudentEmail(student_id, new_email)

            elif choice == "4":
                student_id = int(input("Student ID: "))
                deleteStudent(student_id)

            elif choice == "5":
                break

            else:
                print("Enter a number from 1 to 5.")

        # Database errors so the user can try again.
        except ValueError:
            print("Enter a whole number for the student ID or a valid YYYY-MM-DD date.")
        except psycopg.errors.UniqueViolation:
            print("That email is already in use.")
        except psycopg.Error as error:
            print(f"Database error: {error}")

def getAllStudents():
    """Fetch and display all students in student ID order."""
    with psycopg.connect(**db_config) as conn:
        rows = conn.execute(
            "SELECT * FROM students ORDER BY student_id"
        ).fetchall()

    for student_id, first_name, last_name, email, enrollment_date in rows:
        print(f"{student_id} | {first_name} {last_name} | {email} | {enrollment_date}")

def addStudent(first_name, last_name, email, enrollment_date):
    """Insert a student and let PostgreSQL generate the student ID."""
    with psycopg.connect(**db_config) as conn:
        conn.execute( 
            "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
            (first_name, last_name, email, enrollment_date)
        )

def updateStudentEmail(student_id, new_email):
    """Change the email of the student with the given ID."""
    with psycopg.connect(**db_config) as conn:
        conn.execute(
            "UPDATE students SET email = %s WHERE student_id = %s",
            (new_email, student_id)
        )

def deleteStudent(student_id):
    """Remove the student with the given ID."""
    with psycopg.connect(**db_config) as conn:
        conn.execute(
            "DELETE FROM students WHERE student_id = %s",
            (student_id,)
        )

if __name__ == "__main__":
    # Prompt for password
    db_config = {
        "host": "localhost",
        "port": 5432,
        "dbname": "student_db",
        "user": "postgres",
        "password": getpass("PostgreSQL password: "),
    }
    menu()
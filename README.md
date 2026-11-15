# Student Database Application

A Python command-line application that uses PostgreSQL to list, add,
update, and delete student records.

## Requirements

- Python 3
- PostgreSQL
- pgAdmin for database setup and verification

## Database setup

1. Start PostgreSQL and connect to your local server in pgAdmin.
2. Create a database named `student_db`.
3. Open the Query Tool for `student_db` and run `database/setup.sql`.
   The script creates the `students` table and inserts John Doe,
   Jane Smith, and Jim Beam.
4. Verify the starting data by running:

   ```sql
   SELECT * FROM students ORDER BY student_id;
   ```

## Run the application on Windows

Open PowerShell in the project folder and run:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Python runs the application directly. There is no compile step.

Enter your PostgreSQL password when prompted. The app defaults to
`localhost`, port `5432`, and the `postgres` user. If your server uses
different settings, update `db_config` in `app.py`.

## Menu options

| Option | Function | What it does |
| --- | --- | --- |
| 1 | `getAllStudents()` | Displays all students in ID order. |
| 2 | `addStudent()` | Adds a student. Enter the enrollment date as `YYYY-MM-DD` or leave it blank. |
| 3 | `updateStudentEmail()` | Changes a student's email using their student ID. |
| 4 | `deleteStudent()` | Deletes a student using their student ID. |
| 5 | Exit | Closes the application. |

## Demonstration video

[Watch the database setup and demonstration](https://drive.google.com/file/d/19eiPndvnLzdO6bmmILFgC9qkoNXKGXVh/view?usp=sharing)
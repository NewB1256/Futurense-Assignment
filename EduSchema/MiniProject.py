import mysql.connector

def connect_db(user, password, host, database, port='3306'):
    try:
        conn = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )
        print("Successfully connected to the MySQL database.")
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_tables(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(255),
                            description TEXT,
                            instructor_id INT
                          )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS instructors (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(255),
                            profile TEXT
                          )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(255)
                          )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS enrolments (
                            student_id INT,
                            course_id INT,
                            progress FLOAT,
                            PRIMARY KEY (student_id, course_id)
                          )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS assessments (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            course_id INT,
                            name VARCHAR(255),
                            max_score INT
                          )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS grades (
                            student_id INT,
                            assessment_id INT,
                            score INT,
                            PRIMARY KEY (student_id, assessment_id)
                          )''')
        conn.commit()
        print("Tables are created successfully.")
    except mysql.connector.Error as e:
        print(f"Error creating tables: {e}")

def add_course(conn, name, description, instructor_id):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO courses (name, description, instructor_id) VALUES (%s, %s, %s)", (name, description, instructor_id))
        conn.commit()
        print("Course added successfully.")
    except mysql.connector.Error as e:
        print(f"Error adding course: {e}")

def update_course(conn, course_id, name=None, description=None, instructor_id=None):
    try:
        cursor = conn.cursor()
        if name:
            cursor.execute("UPDATE courses SET name = %s WHERE id = %s", (name, course_id))
        if description:
            cursor.execute("UPDATE courses SET description = %s WHERE id = %s", (description, course_id))
        if instructor_id:
            cursor.execute("UPDATE courses SET instructor_id = %s WHERE id = %s", (instructor_id, course_id))
        conn.commit()
        print("Course updated successfully.")
    except mysql.connector.Error as e:
        print(f"Error updating course: {e}")

def remove_course(conn, course_id):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM courses WHERE id = %s", (course_id,))
        conn.commit()
        print("Course removed successfully.")
    except mysql.connector.Error as e:
        print(f"Error removing course: {e}")

def search_courses(conn, keyword):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM courses WHERE name LIKE %s", ('%' + keyword + '%',))
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as e:
        print(f"Error searching courses: {e}")
        return []

def sort_courses(conn, by="name"):
    try:
        cursor = conn.cursor()
        query = f"SELECT * FROM courses ORDER BY {by}"
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as e:
        print(f"Error sorting courses: {e}")
        return []

def add_instructor(conn, name, profile):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO instructors (name, profile) VALUES (%s, %s)", (name, profile))
        conn.commit()
        print("Instructor added successfully.")
    except mysql.connector.Error as e:
        print(f"Error adding instructor: {e}")

def update_instructor(conn, instructor_id, name=None, profile=None):
    try:
        cursor = conn.cursor()
        if name:
            cursor.execute("UPDATE instructors SET name = %s WHERE id = %s", (name, instructor_id))
        if profile:
            cursor.execute("UPDATE instructors SET profile = %s WHERE id = %s", (profile, instructor_id))
        conn.commit()
        print("Instructor updated successfully.")
    except mysql.connector.Error as e:
        print(f"Error updating instructor: {e}")

def remove_instructor(conn, instructor_id):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM instructors WHERE id = %s", (instructor_id,))
        conn.commit()
        print("Instructor removed successfully.")
    except mysql.connector.Error as e:
        print(f"Error removing instructor: {e}")

def assign_instructor_to_course(conn, course_id, instructor_id):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE courses SET instructor_id = %s WHERE id = %s", (instructor_id, course_id))
        conn.commit()
        print("Instructor assigned to course successfully.")
    except mysql.connector.Error as e:
        print(f"Error assigning instructor to course: {e}")
def enroll_student(conn, student_id, course_id):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO enrolments (student_id, course_id, progress) VALUES (%s, %s, 0.0)", (student_id, course_id))
        conn.commit()
        print("Student enrolled successfully.")
    except mysql.connector.Error as e:
        print(f"Error enrolling student: {e}")

def track_progress(conn, student_id, course_id, progress):
    try:
        cursor = conn.cursor()
        cursor.execute("UPDATE enrolments SET progress = %s WHERE student_id = %s AND course_id = %s", (progress, student_id, course_id))
        conn.commit()
        print("Progress tracked successfully.")
    except mysql.connector.Error as e:
        print(f"Error tracking progress: {e}")
def create_assessment(conn, course_id, name, max_score):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO assessments (course_id, name, max_score) VALUES (%s, %s, %s)", (course_id, name, max_score))
        conn.commit()
        print("Assessment created successfully.")
    except mysql.connector.Error as e:
        print(f"Error creating assessment: {e}")

def input_grade(conn, student_id, assessment_id, score):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO grades (student_id, assessment_id, score) VALUES (%s, %s, %s)", (student_id, assessment_id, score))
        conn.commit()
        print("Grade input successfully.")
    except mysql.connector.Error as e:
        print(f"Error inputting grade: {e}")

def view_grades(conn, student_id):
    try:
        cursor = conn.cursor()
        cursor.execute('''SELECT a.name, g.score, a.max_score
                          FROM grades g
                          JOIN assessments a ON g.assessment_id = a.id
                          WHERE g.student_id = %s''', (student_id,))
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as e:
        print(f"Error viewing grades: {e}")
        return []


def main():
    user = 'root'
    password = 'root@1256'
    host = 'localhost'
    database = 'EduSchema'

    conn = connect_db(user, password, host, database)

    if conn:
        create_tables(conn)  # Ensure the tables are created

        while True:
            print("\nEduSchema Main Menu")
            print("1. Manage Courses")
            print("2. Manage Instructors")
            print("3. Manage Enrollments")
            print("4. Manage Assessments")
            print("5. View Grades")
            print("6. Exit")

            choice = input("Enter choice: ")

            if choice == '1':
                print("\n1. Add Course")
                print("2. Update Course")
                print("3. Remove Course")
                print("4. Search Courses")
                print("5. Sort Courses")
                course_choice = input("Enter choice: ")

                if course_choice == '1':
                    name = input("Course Name: ")
                    description = input("Course Description: ")
                    instructor_id = input("Instructor ID: ")
                    add_course(conn, name, description, instructor_id)

                elif course_choice == '2':
                    course_id = input("Course ID: ")
                    name = input("New Course Name (leave blank to skip): ")
                    description = input("New Course Description (leave blank to skip): ")
                    instructor_id = input("New Instructor ID (leave blank to skip): ")
                    update_course(conn, course_id, name, description, instructor_id)

                elif course_choice == '3':
                    course_id = input("Course ID: ")
                    remove_course(conn, course_id)

                elif course_choice == '4':
                    keyword = input("Enter keyword to search: ")
                    results = search_courses(conn, keyword)
                    for row in results:
                        print(row)

                elif course_choice == '5':
                    by = input("Sort by (name, description, instructor_id): ")
                    results = sort_courses(conn, by)
                    for row in results:
                        print(row)

            elif choice == '2':
                print("\n1. Add Instructor")
                print("2. Update Instructor")
                print("3. Remove Instructor")
                print("4. Assign Instructor to Course")
                instructor_choice = input("Enter choice: ")

                if instructor_choice == '1':
                    name = input("Instructor Name: ")
                    profile = input("Instructor Profile: ")
                    add_instructor(conn, name, profile)

                elif instructor_choice == '2':
                    instructor_id = input("Instructor ID: ")
                    name = input("New Instructor Name (leave blank to skip): ")
                    profile = input("New Instructor Profile (leave blank to skip): ")
                    update_instructor(conn, instructor_id, name, profile)

                elif instructor_choice == '3':
                    instructor_id = input("Instructor ID: ")
                    remove_instructor(conn, instructor_id)

                elif instructor_choice == '4':
                    course_id = input("Course ID: ")
                    instructor_id = input("Instructor ID: ")
                    assign_instructor_to_course(conn, course_id, instructor_id)

            elif choice == '3':
                print("\n1. Enroll Student")
                print("2. Track Student Progress")
                enrollment_choice = input("Enter choice: ")

                if enrollment_choice == '1':
                    student_id = input("Student ID: ")
                    course_id = input("Course ID: ")
                    enroll_student(conn, student_id, course_id)

                elif enrollment_choice == '2':
                    student_id = input("Student ID: ")
                    course_id = input("Course ID: ")
                    progress = input("Progress: ")
                    track_progress(conn, student_id, course_id, progress)

            elif choice == '4':
                print("\n1. Create Assessment")
                print("2. Input Grade")
                assessment_choice = input("Enter choice: ")

                if assessment_choice == '1':
                    course_id = input("Course ID: ")
                    name = input("Assessment Name: ")
                    max_score = input("Max Score: ")
                    create_assessment(conn, course_id, name, max_score)

                elif assessment_choice == '2':
                    student_id = input("Student ID: ")
                    assessment_id = input("Assessment ID: ")
                    score = input("Score: ")
                    input_grade(conn, student_id, assessment_id, score)

            elif choice == '5':
                student_id = input("Student ID: ")
                results = view_grades(conn, student_id)
                for row in results:
                    print(f"Assessment: {row[0]}, Score: {row[1]}/{row[2]}")

            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

        conn.close()
        print("Database connection closed.")


main()
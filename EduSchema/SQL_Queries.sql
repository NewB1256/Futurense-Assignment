-- Create the database
CREATE DATABASE EduSchema;

-- Use the database
USE EduSchema;

-- Create the instructors table
CREATE TABLE instructors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    profile TEXT
);

-- Create the courses table
CREATE TABLE courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    instructor_id INT,
    FOREIGN KEY (instructor_id) REFERENCES instructors(id)
);

-- Create the students table
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Create the enrolments table
CREATE TABLE enrolments (
    student_id INT,
    course_id INT,
    progress FLOAT DEFAULT 0.0,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Create the assessments table
CREATE TABLE assessments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT,
    name VARCHAR(255) NOT NULL,
    max_score INT NOT NULL,
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Create the grades table
CREATE TABLE grades (
    student_id INT,
    assessment_id INT,
    score INT,
    PRIMARY KEY (student_id, assessment_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (assessment_id) REFERENCES assessments(id)
);

-- Insert values into instructors table
INSERT INTO instructors (name, profile) VALUES
('Saravanan', 'Experienced instructor in Mathematics'),
('Priya', 'Expert in Computer Science and Programming'),
('Rajesh', 'Specializes in Physics and Electronics');

-- Insert values into courses table
INSERT INTO courses (name, description, instructor_id) VALUES
('Mathematics 101', 'Introduction to basic mathematical concepts', 1),
('Computer Science Fundamentals', 'Fundamentals of computer science and programming', 2),
('Physics for Engineers', 'Foundational physics concepts for engineering students', 3);

-- Insert values into students table
INSERT INTO students (name) VALUES
('Arjun'),
('Priya'),
('Divya'),
('Ganesh'),
('Shalini');

-- Insert values into enrolments table
INSERT INTO enrolments (student_id, course_id) VALUES
(1, 1),
(2, 2),
(3, 1),
(4, 3),
(5, 3);

-- Insert values into assessments table
INSERT INTO assessments (course_id, name, max_score) VALUES
(1, 'Midterm Exam', 100),
(1, 'Final Exam', 100),
(2, 'Programming Assignment', 100),
(3, 'Quiz 1', 50),
(3, 'Quiz 2', 50);

-- Insert values into grades table
INSERT INTO grades (student_id, assessment_id, score) VALUES
(1, 1, 85),
(1, 2, 90),
(2, 3, 95),
(3, 1, 80),
(4, 4, 45),
(5, 5, 40);



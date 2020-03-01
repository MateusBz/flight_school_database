CREATE TABLE IF NOT EXISTS students (id integer PRIMARY KEY autoincrement, first_name varchar, last_name varchar, pesel integer, phone integer, address varchar);
CREATE TABLE IF NOT EXISTS online_courses (course_id integer, url varchar, FOREIGN KEY (course_id) REFERENCES courses (course_id));
CREATE TABLE IF NOT EXISTS onsite_courses (course_id integer, address varchar, days integer, time datetime, FOREIGN KEY (course_id) REFERENCES courses (course_id));
CREATE TABLE IF NOT EXISTS course_instructors (course_id integer, stuff_id integer, enrollment_date datetime, FOREIGN KEY (course_id) REFERENCES courses (course_id), FOREIGN KEY (stuff_id) REFERENCES staff (id));
CREATE TABLE IF NOT EXISTS staff (id integer PRIMARY KEY autoincrement, first_name varchar, last_name varchar, enrollment_date datetime, pesel integer, phone integer, address varchar);
CREATE TABLE IF NOT EXISTS administrators (stuff_id integer, department_id integer, enrollment_date datetime, FOREIGN KEY (stuff_id) REFERENCES staff (id), FOREIGN KEY (department_id) REFERENCES departments (id));
CREATE TABLE IF NOT EXISTS departments (id integer PRIMARY KEY autoincrement, NAME varchar, budget float, address varchar);
CREATE TABLE IF NOT EXISTS courses (course_id integer PRIMARY KEY autoincrement, title varchar, credits integer, department_id integer, start_date datetime, end_date datetime, price float, FOREIGN KEY (department_id) REFERENCES departments (id));
CREATE TABLE IF NOT EXISTS students_grades (enrollment_id integer PRIMARY KEY autoincrement, student_id integer, course_id integer, grade integer, FOREIGN KEY (student_id) REFERENCES students (id), FOREIGN KEY (course_id) REFERENCES courses (course_id));

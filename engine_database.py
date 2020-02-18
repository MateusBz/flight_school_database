from sqlalchemy import create_engine


def execute_query(engine, query):
    return engine.execute(query)


def create_database(url, queries):
    engine = create_engine(url)
    for query in queries:
        execute_query(engine, query)


if __name__ == '__main__':

    url = 'sqlite:///school.sqlite'
    queries = [
        """create table if not exists Student(
            id integer primary key autoincrement,
            first_name varchar,
            last_name varchar,
            PESEL integer,
            phone integer,
            address varchar);""",
        """create table if not exists OnlineCourse(
            course_id integer,
            url varchar,
            foreign key (course_id) references Course (course_id));""",
        """create table if not exists OnsiteCourse(
            course_id integer,
            address varchar,
            days integer,
            time datetime,
            foreign key (course_id) references Course (course_id));""",
        """create table if not exists CourseInstructor(
            course_id integer,
            stuff_id integer,
            enrollment_date datetime,
            foreign key (course_id) references Course (course_id),
            foreign key (stuff_id) references Staff (id));""",
        """create table if not exists Staff(
            id integer primary key autoincrement,
            first_name varchar,
            last_name varchar,
            enrollment_date datetime,
            PESEL integer,
            phone integer,
            address varchar);""",
        """create table if not exists Administrator(
            stuff_id integer,
            department_id integer,
            enrollment_date datetime,
            foreign key (stuff_id) references Staff (id),
            foreign key (department_id) references Department(id));""",
        """create table if not exists Department(
            id integer primary key autoincrement,
            name varchar,
            budget float,
            address varchar);""",
        """create table if not exists Course(
            course_id integer primary key autoincrement,
            title varchar,
            credits integer,
            department_id integer,
            start_date datetime,
            end_date datetime,
            price float,
            foreign key (department_id) references Department (id));""",
        """create table if not exists StudentsGrade(
            enrollment_id integer primary key autoincrement,
            student_id integer,
            course_id integer,
            grade integer,
            foreign key (student_id) references Student(id),
            foreign key (course_id) references Course(course_id));"""
    ]


    database = create_database(url, queries)

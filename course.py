from db import DB
from student import Student

class Course:
    def __init__(self, name, course_id, max_students):
        self.name = name
        self.id = course_id
        self.max_students = max_students
        self.students = []

    def save(self):
        db = DB()

        courseInDB = db.get(tableName="courses", field="id", data=self.id)

        if (courseInDB):
            print(f"Course with id {self.id} already exists!")
            return

        db.insert(tableName="courses", data={'id': self.id, 'name': self.name, 'max_students': self.max_students, 'students': self.students})

        print(f"Course {self.name} created with success!")

    @staticmethod
    def list_all():
        db = DB()

        all_courses = db.get_all(tableName="courses")

        for course in all_courses:
            name = course["name"]
            course_id = course["id"]
            max_students = course["max_students"]
            students_count = len(course["students"])

            print(f"Name: {name}, ID: {course_id}, Max students: {max_students}, Students count: {students_count}")
    
    # WIP (work in progress)
    @staticmethod
    def list_course_students(course_id):
        db = DB()

        course = db.get(tableName="courses",field="id",data=course_id)

        if not course:
            print(f"Course id {course_id} doesn't exists!")
            return
        
        all_students = Student.get_all()

        students_in_course = list(filter(lambda student: course['students'].contains(student.registration), all_students))

        print(students_in_course)

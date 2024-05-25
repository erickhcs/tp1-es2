from db import DB
class Course:
    def __init__(self, name, course_id, max_students):
        self.name = name
        self.id = course_id
        self.max_students = max_students
        self.students = []

    def save(self):
        db = DB('courses')

        db.insert({'id': self.id, 'name': self.name, 'max_students': self.max_students, 'students': self.students})

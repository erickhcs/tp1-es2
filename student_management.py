import cmd
from course import Course
from db import DB

class StudentManagement(cmd.Cmd):
    prompt = '>> '
    intro = 'Welcome to StudentManagement. Type "help" for available commands.'

    def do_quit(self, line):
        'Exit system'
        return True
    
    def do_add_course(self, line):
        'Add a new course separated by semicolon: add_student <name>;<course_id>;<max_students>'
        splitted_entry = line.split(";")

        newCourse = Course(name=splitted_entry[0],course_id=splitted_entry[1],max_students=splitted_entry[2])
        
        newCourse.save()

    def do_list_courses(self, line):
        'List all registered courses'
        db = DB()

        all_courses = db.get_all(tableName="courses")

        for course in all_courses:
            name = course["name"]
            course_id = course["id"]
            max_students = course["max_students"]
            students = course["students"]

            print(f"Name: {name}, ID: {course_id}, Max students: {max_students}, Students: {students}")

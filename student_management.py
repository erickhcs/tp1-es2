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
        try:
          splitted_entry = line.split(";")

          if len(splitted_entry) != 3:
              print("add_course parameters are incorrect. You should pass values separated by semicolon: add_student <name>;<course_id>;<max_students>")
              return
                    
          name=splitted_entry[0]
          course_id=splitted_entry[1]
          max_students=splitted_entry[2]

          if len(name) == 0:
             print("name parameter should not be empty!")
             return
          
          if len(course_id) == 0:
             print("course_id parameter should not be empty!")
             return


          if not max_students.isdigit():
            print("max_students parameter should be a number!")
            return


          newCourse = Course(name,course_id,max_students=int(max_students))
          
          newCourse.save()
        
        except ValueError as e:
          print(f"Error: {e}")

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

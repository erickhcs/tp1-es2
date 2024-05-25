import cmd
from course import Course

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
        

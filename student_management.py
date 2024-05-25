import cmd
from course import Course
from student import Student
class StudentManagement(cmd.Cmd):
    prompt = '>> '
    intro = 'Welcome to StudentManagement. Type "help" for available commands.'

    def do_quit(self, line):
        'Exit system'
        return True
    
    def do_add_course(self, line):
        'Add a new course separated by semicolon: add_course <name>;<course_id>;<max_students>'
        try:
            splitted_entry = line.split(";")

            if len(splitted_entry) != 3:
                print("add_course parameters are incorrect. You should pass values separated by semicolon: add_course <name>;<course_id>;<max_students>")
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
            
            newCourse.create()
        
        except ValueError as e:
            print(f"Error: {e}")

    def do_list_courses(self, line):
        'List all registered courses'
        Course.list_all()
    
    def do_list_students_from_course(self, line):
        'List students from a course: list_students_from_course <course_id>'
        Course.list_course_students(line)

    def do_add_student(self, line):
        'Add a new student separated by semicolon: add_student <name>;<cpf>;<registration>'
        try:
            splitted_entry = line.split(";")

            if len(splitted_entry) != 3:
                print("add_student parameters are incorrect. You should pass values separated by semicolon: add_student <name>;<cpf>;<registration>")
                return
                      
            name=splitted_entry[0]
            cpf=splitted_entry[1]
            registration=splitted_entry[2]

            if len(name) == 0:
                print("name parameter should not be empty!")
                return
            
            if len(cpf) != 14:
                print("cpf parameter should be in the format xxx.xxx.xxx-xx!")
                return


            if not registration.isdigit():
                print("registration parameter should be a number!")
                return


            newStudent = Student(name,cpf,registration=int(registration))
            
            newStudent.create()
        
        except ValueError as e:
            print(f"Error: {e}")

    def do_list_students(self, line):
        'List all registered students'
        Student.list_all()

    def do_register_student_in_course(self, line):
        'Register student in course: register_student_in_course <student_registration>;<course_id>'
        try:
            splitted_entry = line.split(";")

            if len(splitted_entry) != 2:
                print("register_student_in_course parameters are incorrect. You should pass values separated by semicolon: register_student_in_course <student_registration>;<course_id>")
                return
            
            student_registration = splitted_entry[0]
            course_id = splitted_entry[1]

            if len(course_id) == 0:
                print("course_id parameter should not be empty!")
                return

            if not student_registration.isdigit():
                print("student_registration parameter should be a number!")
                return
            
            Course.add_student(student_registration=int(student_registration),course_id=course_id)

        except ValueError as e:
            print(f"Error: {e}")

import cmd

class StudentManagement(cmd.Cmd):
    prompt = '>> '
    intro = 'Welcome to StudentManagement. Type "help" for available commands.'

    def do_hello(self, line):
        print("Hello, World!")

    def do_quit(self, line):
        return True

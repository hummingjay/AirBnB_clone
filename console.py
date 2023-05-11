#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """ My AirBnB clone command interpreter """
    prompt = "(hbnb) "

    # THe commands
    def do_EOF(self, line):
        """Accepts interuption by user to exit program """
        print()
        return True

    def do_quit(self, line):
        """Quit command to Exit the program """
        return True

if __name__ == '__main__':
        HBNBCommand().cmdloop()

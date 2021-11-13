#!/usr/bin/python3
""" program that contains the entry point of the command interpreter"""

import cmd
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage




classes = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City, 
"Place": Place, "Review": Review, "State": State, "User": User}

class HBNBCommand(cmd.Cmd):
    """HBNBCommand Class definition"""
    prompt = "(hbnb)"

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_EOF(self, line):
        """End of file"""
        return True

    def do_empty(self, line):
        """"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        arguments = line.split()

        if len(arguments) == 0:
            print("** class name missing **")
        else:
            if arguments[0] in classes:
                instance = classes[arguments[0]]()
                print(instance.id)
                instance.save()

            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

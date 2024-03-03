#!/usr/bin/python3
"""
Write a program called console.py
that contains the entry point of the command interpreter:
"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """
    Console handling class
    """
    prompt = '(hbnb) '

    def getClass(self, arg):
        classList = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
        }
        if arg in classList:
            return classList[arg]
        else:
            return None

    def emptyline(self):
        pass

    def do_quit(self, arg):
        exit()

    def do_EOF(self, arg):
        exit()

    def do_help(self, arg):
        help_messages = {
            "quit": "Quit command to exit the program",
            "EOF": "exit the program",
            "help": "displays help message",
            "create": "creates a new instance of a class\
 (create <classname>)",
            "show": "displays instance of a class (show <class name>\
 <instance id>)",
            "destroy": "removes an instance of a class (destroy <classname>\
 <instance id>)",
            "all": "shows instances of all classes or a specific class (all\
 [classname])",
            "update": "changes attribute of instance (update <classname>\
 <instance id> <attribute> <value>)",
            "": "\nDocumented commands (type help <topic>)\n\
========================================\n\
EOF help quit\n\n"
        }
        print(help_messages[arg])

    def do_create(self, arg):
        if arg == "":
            print("** class name missing **")
        else:
            cla = self.getClass(arg)

            if cla is None:
                print("** class doesn't exist **")
            else:
                new = cla()
                new.save()
                print(new.id)

    def do_show(self, arg):
        if arg == "":
            print("** class name missing **")
        else:
            args = arg.split()
            cla = self.getClass(args[0])
            if cla is None:
                print("** class doesn't exist **")
            elif len(args) != 2:
                print("** instance id missing **")
            else:
                instanceList = models.storage.all()
                key = "{}.{}".format(args[0], args[1])
                if key in instanceList:
                    print(str(instanceList[key]))
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        if arg == "":
            print("** class name missing **")
        else:
            args = arg.split()
            cla = self.getClass(args[0])
            if cla is None:
                print("** class doesn't exist **")
            elif len(args) != 2:
                print("** instance id missing **")
            else:
                instanceList = models.storage.all()
                key = "{}.{}".format(args[0], args[1])
                if key in instanceList:
                    del instanceList[key]
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        instanceList = models.storage.all()
        if arg == "":
            for i in instanceList.values():
                print(str(i))
        else:
            cla = self.getClass(arg)
            if cla is None:
                print("** class doesn't exist **")
            else:
                for i in instanceList.values():
                    if i.__class__ == cla:
                        print(str(i))

    def do_update(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            cla = self.getClass(args[0])
            if cla is None:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                instanceList = models.storage.all()
                key = "{}.{}".format(args[0], args[1])
                if key not in instanceList:
                    print("** no instance found **")
                elif len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    setattr(instanceList[key], args[2], args[3])


if __name__ == '__main__':
    HBNBCommand().cmdloop()

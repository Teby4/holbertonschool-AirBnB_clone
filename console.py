#!/usr/bin/python3
"""
Write a program called console.py that contains the entry point of the command interpreter:
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    
    """
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, arg):
        exit()
    
    def do_EOF(self, arg):
        exit()
        
    def do_help(self, arg):
        help_messages = {
            "quit" : "Quit command to exit the program",
            "EOF" : "exit the program",
            "help" : "displays help message",
            "" : "\nDocumented commands (type help <topic>)\n\
========================================\n\
EOF help quit\n\n"
        }
        print(help_messages[arg])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
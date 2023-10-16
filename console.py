#!/usr/bin/python3
"""
Module: console

This module contains the entry point of the command interpreter
"""


import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    This class contains the entry point of the command intepreter
    """
    prompt = '(hbnb) '
    class_map = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
    }

    def do_quit(self, arg):
        """
        This method exits the program
        """
        return True

    def do_EOF(self, arg):
        """
        This method exits the program
        """
        return True

    def emptyline(self):
        """
        This method makes sure nothing is executed
        """
        pass

    def do_create(self, arg):
        """
        This method creates a new instance of BaseModel, saves it(to JSON file)
        and prints the id
        """
        if not arg:
            print("** class name missing **")
            return
        class_name = arg
        if class_name not in self.class_map:
            print("** class doesn't exist **")
            return
        try:
            instance = self.class_map[class_name]()
            instance.save()
            print(instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        This method prints the representation of an instance based
        on the class name
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            with open("file.json", "r") as file:
                data = json.load(file)
                key = class_name + "." + instance_id
                if key in data:
                    instance_data = data[key]
                    instance = eval(instance_data['__class__'])(
                            **instance_data)
                    print(instance)
                else:
                    print("** no instance found **")
        except IndexError:
            if len(args) < 2:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        This method deltes an instance based on the class name and id
        (save the change into the JSON file)
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            with open("file.json", "r") as file:
                data = json.load(file)
                key = class_name + "." + instance_id
                if key in data:
                    del data[key]
                    with open("file.json", "w") as file:
                        json.dump(data, file)
                else:
                    print("** no instance found **")
        except IndexError:
            if len(args) < 2:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """
        This method prints all string representauon of all instances based
        or not on the class name.
        """
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        try:
            cls = globals()[class_name]
        except KeyError:
            print("** class doesn't exist **")
            return

        instances = []
        with open("file.json", "r") as file:
            data = json.load(file)
            for key, value in data.items():
                if key.split(".")[0] == class_name:
                    instances.append(eval(value['__class__'])(**value))
        print(instances)

    def do_update(self, arg):
        """
        This method updates an instance based on the class name and id
        by adding or updating attribute(save the cahnge into the JSON file)
        """
        args = arg.split()
        if len(args) < $:
            print("** Not enough arguments **")
            return

        class_name = args[0]
        if class_name not in self.class_map:
            print("** class doesn't exist **")
            return
        if class_name == "":
            print("** class name missing **")
            return

        obj_id = args[1]
        if obj_id == "":
            print("** instance id missing **")
            return

        attr_name = args[2]
        if attr_name == "":
            print("** attribute name missing **")
            return
        attr_value = ""
        if len(args) >= 4:
            attr_value = args[3]
            setattr(instance, attr_name, attr_value)
            instance.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

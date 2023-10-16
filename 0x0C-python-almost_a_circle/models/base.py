#!/usr/bin/python3
'''Defines a class Base'''
import json
import csv
import turtle


class Base:
    '''Get the base'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Assign the public instance attribute id with this argument value

        Otherwise - increment __nb_objects and assign the new value to the
        public instance attribute id
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Return the JSON string represenntation of a dictionary'''
        if list_dictionaries is None or list_dictionaries == 0:
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        '''Save a JSON string to a file'''
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + '.json'

        json_string = cls.to_json_string([obj.to_dictionary()
                                         for obj in list_objs])

        with open(filename, 'w') as jsonfile:
            jsonfile.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        '''Returns the list of the JSON string representation'''
        if json_string is None or json_string == 0:
            return []
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        '''Return an instance with all attributes already set'''
        if dictionary and dictionary != {}:
            cls.__name__ = "Rectangle"
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        '''Return a list of instances from a JSON string'''
        filename = cls.__name__ + '.json'
        try:
            with open(filename, "r") as jsonfile:
                dict_list = Base.from_json_string(jsonfile.read())
                return [cls.create(**dic) for dic in dict_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Write the CSV serialization of a list of objects to a file'''
        filename = cls.__name__ + '.csv'
        if list_objs is None or list_objs == []:
            list_objs = []
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        else:
            fieldnames = ["id", "size", "x", "y"]

        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        '''Return a list of class instances from a CSV file'''
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([s, int(i)] for s, i in dic.items())
                                    for dic in list_dicts]
                return [cls.create(**dic) for dic in list_dicts]
        except IOError:
            return []

    def draw(list_rectangles, list_squares):
        '''Draw Rectangles and Squares using the turtle module'''
        turt = turtle.Turtle()
        turt.screen.bgcolor("#0000FF")
        turt.pensize(4)
        turt.shape("turtle")

        turt.color("#000000")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#ff0000")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

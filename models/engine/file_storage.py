#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review}

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """ Return the dictionary """
        fs_objects = {}
        if cls:
            if type(cls) is str and cls in classes:
                for key, val in self.__objects.items():
                    if cls == key.split('.')[0]:
                        fs_objects[key] = val
            elif cls.__name__ in classes:
                for key, val in self.__objects.items():
                    if cls.__name__ == key.split('.')[0]:
                        fs_objects[key] = val
        else:
            return self.__objects
        return fs_objects

    def new(self, obj):
        '''
            Set in __objects the obj with key <obj class name>.id
            Aguments:
                obj : An instance object.
        '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        '''
            Serializes __objects attribute to JSON file.
        '''
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass
        

        def delete(self, obj=None):
            """deletes object from __objects if it's inside"""
            if obj is not None:
                key = obj.__class__.__name__ + "." + str(obj.id)
                if key in self.__objects:
                    del self.__objects[key]
            self.save()
    

    def close(self):
        """
        close with reload
        """
        self.reload()

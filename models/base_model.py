#!/usr/bin/python3
"""
base_model module
"""
from datetime import datetime
import uuid
import models
time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    class BaseModel
    """
    id = primary_key = True
    created_at = DateTime, default = datetime.utcnow
    updated_at = DateTime, default = datetime.utcnow

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if"created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if"updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        return new_dict

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
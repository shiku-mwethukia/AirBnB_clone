#!/usr/bin/python3
<<<<<<< HEAD
"""
base_model module
"""
from datetime import datetime
import uuid
time = "%Y-%m-%dT%H:%M:%S.%f"
class BaseModel:
    """
    class BaseModel
    """
    id = primary_key=True
    created_at = DateTime, default=datetime.utcnow
    updated_at = DateTime, default=datetime.utcnow
    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)
=======
"""Module for Base class
Contains the Base class for the AirBnB clone console.
"""

import uuid
from datetime import datetime
class BaseModel:

    """Class for base model of object hierarchy."""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
            
    def __str__(self):
        """Returns a human-readable string representation
        of an instance."""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute
        with the current datetime."""

        self.updated_at = datetime.now()
    def to_dict(self):
        """Returns a dictionary representation of an instance."""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
>>>>>>> 31e26df4c17d26f4692c01000ff1441978eb470d

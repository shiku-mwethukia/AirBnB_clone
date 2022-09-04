#!/usr/bin/python3
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
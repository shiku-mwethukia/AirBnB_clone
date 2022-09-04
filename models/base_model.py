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
    id = primary_key = True
    created_at = DateTime, default = datetime.utcnow
    updated_at = DateTime, default = datetime.utcnow

    def __str__(self):
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

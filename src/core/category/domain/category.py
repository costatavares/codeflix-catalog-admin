from dataclasses import dataclass,field

import uuid
from uuid import UUID 

@dataclass
class Category:

    name:str
    description: str = ""
    is_active: bool = True
    id:UUID = field(default_factory=uuid.uuid4)

    # def __init__(
    #     self,
    #     name,
    #     id="",
    #     description: str = "",
    #     is_active: bool = True,
    # ):      
    #     self.id = id or uuid.uuid4()
    #     self.name = name
    #     self.description = description
    #     self.is_active = is_active

    #     # if len(self.name) > 255:
    #     #     raise ValueError("name must have less than 256 characteres")

    #     self.validate()

    def __post_init__(self):
        self.validate()
        
    def validate(self):
        if len(self.name) > 255:
            raise ValueError("name cannot be longer than 255")
        
        if not self.name: # len(self.name) == 0
            raise ValueError("name cannot be empty")
        
        
    def __str__(self):
        return f"{self.name} - {self.description} -({self.is_active})"

    def __repr__(self):
        return f"<Category {self.name} ({self.id})>"

    def update_category(self, name, description):
        self.name = name
        self.description = description

        self.validate()

    def active(self):
        self.is_active = True
        
        self.validate()

    def deactivate(self):
        self.is_active = False

        self.validate()    
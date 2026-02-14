import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
        """Base class for a Student"""
        name: str
        surname: str
        active: bool = True
        id: str = field(init = False)
        login: str = field(init = False)
        def __post_init__(self):
            """Cette méthode remplace la logique de __init__"""
            self.id = generate_id()
            self.login = f"{self.name[0]}{self.surname}"

def new_stud_in_town(*args, **kwargs):
    return Student(**kwargs)
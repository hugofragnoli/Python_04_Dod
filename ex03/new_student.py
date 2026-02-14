import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Function to generate an id randomly"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Base class for a Student"""
    name: str
    surname: str
    active: bool = True
    id: str = field(init=False)
    login: str = field(init=False)

    def __post_init__(self):
        """Cette méthode remplace la logique de __init__"""
        self.id = generate_id()
        self.login = f"{self.name[0]}{self.surname}"


def new_stud_in_town(*args, **kwargs):
    """Fonction pour créer une nouvelle instance de Student.

    Args: (fonctionne en key - value)
        *args: Arguments positionnels pour le constructeur de Student.
        **kwargs: Arguments par mots-clés pour le constructeur de Student.

    Returns:
        Student: Une nouvelle instance de la classe Student."""
    return Student(**kwargs)

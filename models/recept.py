from dataclasses import dataclass, field
from typing import List
from .ingredient import Ingrediënt
from .stap import Stap

@dataclass
class Recept:
    naam: str
    omschrijving: str
    ingrediënten: List[Ingrediënt] = field(default_factory=list)
    stappen: List[Stap] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.naam.strip():
            raise ValueError("Recept-naam mag niet leeg zijn.")
        if not self.omschrijving.strip():
            raise ValueError("Omschrijving mag niet leeg zijn.")
        if not self.ingrediënten:
            raise ValueError("Minstens één ingrediënt vereist.")
        if not self.stappen:
            raise ValueError("Minstens één stap vereist.")

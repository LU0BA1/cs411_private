from typing import Any, Optional

class Animal:
    def _init_(self, animal_id: int, species: str, age: Optional[int] = None, health_status: Optional[str] = None):
        self.animal_id = animal_id
        self.species = species
        self.age = age
        self.health_status = health_status


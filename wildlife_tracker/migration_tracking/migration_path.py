from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:
    def _init(self, path_id: int, species: str, start_location: 'Habitat', destination: 'Habitat', duration: Optional[int] = None): 
        self.path_id = path_id
        self.species = species
        self.start_location = start_location
        self.destination = destination
        self.duration = duration

from typing import Optional, List
from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.animal_management.animal import Animal

class HabitatManager:
    def _init_(self):
        self.habitats: dict[int, Habitat] = {}

    def create_habitat(self, habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat:
        pass
    
    def get_habitat_by_id(self, habitat_id: int) -> Optional[Habitat]:
        pass
    
    def remove_habitat(self, habitat_id: int) -> None:
        pass
        
    def update_habitat_details(self, habitat_id: int, **kwargs) -> None:
        pass

    def get_habitats(self) -> List[Habitat]:
        pass

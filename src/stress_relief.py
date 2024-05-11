from config import root_dir
from src.connect_to_database import DatabaseManager  # Import DatabaseManager


class Stress:
    def __init__(self, id, image, description) -> None:
        self.id = id
        self.image = image
        self.description = description
    pass

    id: int
    image: str
    description: str

class StressFunction:
    stresses: list[Stress]
    current_stress_index = None

    def __init__(self) -> None:
        self.database = DatabaseManager()
        self.stresses = self.get_all()
        self.set_current_stress(0)
        pass


    def get_all(self) -> list[Stress]:
        result = self.database.execute_query("SELECT * FROM stress_relief;")
        if result != None:
            data = []
            for item in result:
                data.append(Stress(item[0], root_dir + item[1], item[2]))
            return data
        return []
    def set_current_stress(self, index) -> Stress:
        if index < len(self.stresses):
            self.current_stress_index = index
            return self.stresses[index]

    def next_stress(self) -> Stress or None:
        if self.current_stress_index != len(self.stresses)-1:
            return self.set_current_stress(self.current_stress_index+1)

    def previous_stress(self) -> Stress or None:
        if self.current_stress_index != 0:
            return self.set_current_stress(self.current_stress_index-1)


    def current_stress(self):
        if self.current_stress_index is None:
            return None
        return self.stresses[self.current_stress_index]
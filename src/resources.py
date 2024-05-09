from src.connect_to_database import DatabaseManager


class Resources:
    def __init__(self, id, description, image_path=None, link=None) -> None:
        self.id = id
        self.description = description
        self.image_path = image_path
        self.link = link



class ResourcesFunction:
    resources_ls: list[Resources]
    current_resource_index = None

    def __init__(self) -> None:
        self.database = DatabaseManager()
        self.resources_ls = self.get_all()
        self.set_current_resources(0)
        pass

    def get_all(self) -> list[Resources]:
        global data
        result = self.database.execute_query("SELECT * FROM external_resources;")
        if result:
            data = []
        for item in result:
            if len(item) >= 3:
                data.append(Resources(item[0], item[1], item[2]))
            else:
                print("Warning: Incomplete data in database for resource:", item)
            return data
        return []

    def set_current_resources(self, index) -> Resources:
        if index < len(self.resources_ls):
            self.current_resource_index = index
            return self.resources_ls[index]

    def next_stress(self) -> Resources or None:
        if self.current_resource_index != len(self.resources_ls) - 1:
            return self.set_current_resources(self.current_resource_index + 1)

    def previous_stress(self) -> Resources:
        if self.current_resource_index != 0:
            return self.set_current_resources(self.current_resource_index - 1)

    def current_stress(self):
        if self.current_resource_index is None:
            return None
        return self.resources_ls[self.current_resource_index]
from src.connect_to_database import DatabaseManager


class ResourcesDB:  # TODO continue with this after they import database
    id: int
    title: str
    description: str
    link: str

    def __init__(self, id, title, description, link) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.link = link


class Resources:
    resources_ls: list[ResourcesDB]
    current_resource_index = None

    def __init__(self) -> None:
        self.database = DatabaseManager()
        self.resources_ls = self.get_all()
        self.set_current_resources(0)

    def get_all(self) -> list[ResourcesDB]:
        result = self.database.execute_query("SELECT * FROM external_resources;")
        data = [ResourcesDB(item[0], item[1], item[2], item[3]) for item in result if result is not None]
        return data

    def set_current_resources(self, index) -> ResourcesDB:
        if index < len(self.resources_ls):
            self.current_resource_index = index
            return self.resources_ls[index]

    def next_stress(self) -> ResourcesDB or None:
        if self.current_resource_index != len(self.resources_ls) - 1:
            return self.set_current_resources(self.current_resource_index + 1)

    def previous_stress(self) -> ResourcesDB:
        if self.current_resource_index != 0:
            return self.set_current_resources(self.current_resource_index - 1)

    def current_stress(self):
        if self.current_resource_index is None:
            return None
        return self.resources_ls[self.current_resource_index]

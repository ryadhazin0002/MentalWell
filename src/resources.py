from src.connect_to_database import DatabaseManager

class Resources:
    def __init__(self, id, image_path, description,video_link) -> None:
        self.id = id
        self.image_path = image_path
        self.description = description
        self.video_link = video_link
        pass

    id: int
    image_path: str
    description: str
    video_link: str



class ResourcesFunction:
    resources_ls: list[Resources]
    current_resource_index = None

    def __init__(self) -> None:
        self.database = DatabaseManager()
        self.resources_ls = self.get_all()
        self.set_current_resources(0)
        pass

    def get_all(self) -> list[Resources]:
        result = self.database.execute_query("SELECT * FROM external_resources;")
        if result != None:
            data = []
            for item in result:
                data.append(Resources(item[0], item[1], item[2], item[3]))
            return data
        return []

    def set_current_resources(self, index) -> Resources:
        if index < len(self.resources_ls):
            self.current_resource_index = index
            return self.resources_ls[index]

    def next_resource(self)-> Resources or None:
        if self.current_resource_index != len(self.resources_ls)-1:
            return self.set_current_resources(self.current_resource_index+1)

    def previous_resource(self) -> Resources or None:
        if self.current_resource_index != 0:
            return self.set_current_resources(self.current_resource_index - 1)

    def current_resource(self):
        if self.current_resource_index is None:
            return None
        return self.resources_ls[self.current_resource_index]


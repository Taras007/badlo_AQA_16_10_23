class ObjectModel:
    def __init__(self, id, name, data):
        self.id = id
        self.name = name
        self.data = data

    @staticmethod
    def from_json(json_data):
        return ObjectModel(
            id=json_data.get("id"),
            name=json_data["name"],
            data=json_data.get("data")
        )
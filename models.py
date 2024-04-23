class Contributor:
    def __init__(self, name):
        self.name = name
        self.resources = {}

class Resource:
    def __init__(self, resource_id, rating):
        self.resource_id = resource_id
        self.rating = rating
        self.downloads = []
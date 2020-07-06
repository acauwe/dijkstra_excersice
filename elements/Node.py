class Node:

    def __init__(self, id):
        self.id = id
        self.paths = []
        self.done = False
        self.distance = None
        self.shortest_path_to_start = None

    def __str__(self):
        return str(id)

    def __repr__(self):
        return str(id)
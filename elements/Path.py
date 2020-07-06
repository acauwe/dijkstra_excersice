class Path:

    def __init__(self, weight, from_node, to_node):
        self.weight = weight
        self.from_node = from_node
        self.to_node = to_node

    def __str__(self):
        return "From " + self.from_node + " to " + self.to_node

    def __repr__(self):
        return "From " + self.from_node.id + " to " + self.to_node.id

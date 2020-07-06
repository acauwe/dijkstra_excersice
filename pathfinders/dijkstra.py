class Dijkstra:
    next_nodes = []
    found = False

    def find(self, start, end):
        start.distance = 0
        self.next_nodes = [start]

        while len(self.next_nodes) > 0:
            self.dijkstra_node(self.next_nodes[0], end)

        route = []
        if end.shortest_path_to_start:
            route.append(end.shortest_path_to_start)
            while route[-1].from_node is not start:
                route.append(route[-1].from_node.shortest_path_to_start)

            route.reverse()
        return route

    def dijkstra_node(self, node, end):
        for path in node.paths:
            if path.to_node.distance is None:
                path.to_node.distance = path.from_node.distance + path.weight
                path.to_node.shortest_path_to_start = path
            elif path.from_node.distance + path.weight < path.to_node.distance:
                path.to_node.distance = path.from_node.distance + path.weight
                path.to_node.shortest_path_to_start = path

            if path.to_node is end:
                self.found = True

            if self.found:
                for next_node in self.next_nodes:
                    if next_node.distance >= path.to_node.distance:
                        self.next_nodes.remove(next_node)

            if not path.to_node.done and \
                    path.to_node not in self.next_nodes and \
                    path.to_node is not end:
                self.next_nodes.append(path.to_node)

        node.done = True
        self.next_nodes.remove(node)
        self.next_nodes.sort(key=lambda node: node.distance)

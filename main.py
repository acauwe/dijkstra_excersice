from elements.Node import Node
from elements.Path import Path
from pathfinders.dijkstra import Dijkstra


def create_map():
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")
    nodeF = Node("F")
    nodeG = Node("G")
    nodeH = Node("H")

    nodeA.paths.append(Path(1, nodeA, nodeB))
    nodeA.paths.append(Path(10, nodeA, nodeF))

    nodeB.paths.append(Path(2, nodeB, nodeC))
    nodeB.paths.append(Path(2, nodeB, nodeD))
    nodeB.paths.append(Path(3, nodeB, nodeE))

    nodeC.paths.append(Path(1, nodeC, nodeG))

    nodeE.paths.append(Path(4, nodeE, nodeF))
    nodeE.paths.append(Path(8, nodeE, nodeH))

    nodeF.paths.append(Path(1, nodeF, nodeG))

    nodeG.paths.append(Path(2, nodeG, nodeH))

    return [nodeA, nodeB, nodeC,
            nodeD, nodeE, nodeF,
            nodeG, nodeH
            ]


def start():
    map = create_map()
    route = Dijkstra().find(map[0], map[-1])
    print(route)


if __name__ == '__main__':
    start()

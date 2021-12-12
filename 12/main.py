class Edge:
    def __init__(self, fromNode: str, toNode: str):
        self.fromNode = fromNode
        self.toNode = toNode


class Node:
    def __init__(self, name: str):
        self.name = name


class Graph:
    def __init__(self):
        self.nodes: set[Node] = set()
        self.edges: set[Edge] = set()

    def addNode(self, name: str):
        self.nodes.add(Node(name))

    def addEdge(self, source: str, destination: str):
        nodeList = [node.name for node in self.nodes]
        if source == "start":
            self.edges.add(Edge(source, destination))
        elif destination == "end":
            self.edges.add(Edge(source, destination))
        elif source in nodeList and destination in nodeList:
            self.edges.add(Edge(source, destination))
            self.edges.add(Edge(destination, source))

    def countPaths(self, smallCaveVisits: int, source: int = "start", destination: int = "end") -> list:
        def canVisitSmallCave(path: 'list[str]', nextNode: str, smallCaveVisits: int) -> bool:
            if smallCaveVisits == 1:
                return path.count(nextNode) < 1
            path = path.copy()
            path.append(nextNode)
            smallCaves = {k for k in path if k.islower() and k !=
                          source and k != destination}
            visitedMultipleTimes = ""
            for smallCave in smallCaves:
                count = path.count(smallCave)
                if count == smallCaveVisits:
                    visitedMultipleTimes = smallCave
                    break
                elif count > smallCaveVisits:
                    return False
            if visitedMultipleTimes:
                smallCaves.remove(visitedMultipleTimes)
                for smallCave in smallCaves:
                    if path.count(smallCave) > 1:
                        return False
            return True

        pathsCount = 0
        paths: list[list[str]] = [[source]]

        while paths:
            for path in list(paths):
                paths.remove(path)
                nextNodes = [
                    k.toNode for k in self.edges if k.fromNode == path[-1]]
                for nextNode in nextNodes:
                    if (nextNode.isupper() or canVisitSmallCave(path, nextNode, smallCaveVisits)) and nextNode != source:
                        newPath = path.copy()
                        newPath.append(nextNode)
                        if nextNode == destination:
                            pathsCount += 1
                            print(
                                f"pathsCount: {pathsCount}; currently processing paths: {len(paths)}", end="\r")
                        else:
                            paths.append(newPath)

        return pathsCount


def parseFile(lines: 'list[str]') -> Graph:
    graph = Graph()
    for line in lines:
        fromDest, toDest = line.split("-")[0], line.split("-")[1]
        graph.addNode(fromDest)
        graph.addNode(toDest)
        graph.addEdge(fromDest, toDest)
    return graph


with open("12/input.txt", "r") as file:
    graph = parseFile(lines=file.read().splitlines())
print(
    f"Paths (small caves visited once): {graph.countPaths(1, 'start', 'end')}                         ")
print(
    f"Paths (small caves visited twice): {graph.countPaths(2, 'start', 'end')}                         ")

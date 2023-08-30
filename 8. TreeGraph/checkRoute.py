# Given a directed graph and two nodes (S and E), design an algorithm to find out whether there is a route from S to E.


class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def checkRoute(self, startNode, endNode):
        visited = [startNode]
        queue = [startNode]
        while queue:
            current = queue.pop(0)
            for otherVertex in self.gdict[current]:
                if otherVertex not in visited:
                    if otherVertex == endNode:
                        return True
                    else:
                        visited.append(otherVertex)
                        queue.append(otherVertex)
        return False





customDict = { "a" : ["c","d", "b"],
            "b" : ["j"],
            "c" : ["g"],
            "d" : [],
            "e" : ["f", "a"],
            "f" : ["i"],
            "g" : ["d", "h"],
            "h" : [],
            "i" : [],
            "j" : []
               }
 
g = Graph(customDict)
print(g.checkRoute("a", "j")) #True
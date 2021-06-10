# Graph() creates a new, empty graph.
class Graph:
    
    def __init__(self):
        
        self.verticesDict = {}
        self.numVertices = 0
    
    # adds an instance of Vertex to the graph.
    def addVertex(self, key):
        
        self.numVertices += 1
        
        newVertex = Vertex(key)
        
        self.verticesDict[key] = newVertex
        
        return newVertex
    
    # finds the vertex in the graph named vertKey.
    def getVertex(self, vertex):
        
        if vertex in self.verticesDict:
            
            return self.verticesDict[vertex]
        else:
            return None
    
    # Adds a new, weighted, directed edge to the graph that connects two vertices.
    def addEdge(self, fromVertex, toVertex, weight=0):
        
        if fromVertex not in self.verticesDict:
            newVertex = addVertex(fromVertex)
        
        if toVertex not in self.verticesDict:
            newVertex = addVertex(toVertex)
            
        self.verticesDict[fromVertex].addNeighbour(self.verticesDict[toVertex], weight)
    
    # returns the list of all vertices in the graph.
    def getVertices(self):
        
        return self.verticesDict.keys()
    
    def __iter__(self):
        
        return iter(self.verticesDict.values())
    
    def __contains__(self, vertex):
        
        return vertex in self.verticesDict
    

# Each Vertex uses a dictionary to keep track of the vertices to which it is connected, and the weight of each edge.
# The neighbouring vertices are the keys and their respective edge weights are the values.
class Vertex:

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    # addNeighbor method is used add a connection from this vertex to another.
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    # getConnections method returns all of the vertices in the adjacency list
    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id
    
    # getWeight method returns the weight of the edge from this vertex to the vertex passed in as a parameter.
    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id ) + ' connected to '+ str([x.id for x in self.connectedTo])
"""Author - Anantvir Singh, concept reference:= CLRS, Page 603"""

# --------------------------- Depth First Search ---------------------------------

class Vertex:
    def __init__(self,x):
        self.info = x
        self.color = None
        self.parent = None
        self.d = None
        self.f = None
    
    def element(self):
        return self.info
    
    def __hash__(self):
        return hash(id(self))       # Has function created so that a vertex can be used as a key in a dict or set as dict keys need to be hashable objects !

class Edge:
    def __init__(self,u,v,x):
        self._origin = u
        self._destination = v
        self.info = x
    
    def endpoints(self):                    # return (u,v) tuple for end points of this edge
        return (self._origin,self._destination)
    
    def opposite(self,v):                   # return vertex opposite to the given vertex v
        return self._origin if v is self._destination else self._origin
    
    def element(self):                      # Return value associated with this edge
        return self.info
    
    def __hash__(self):                     # Make edge hashable so that it can be used as key of a map/set
        return hash((self._origin,self._destination))

class Graph:
    
    def __init__(self,directed = False):
        self._outgoing = {}                 # map to hold vertices as keys and their incidence collection dict as value
                                            # i.e _outgoing = {u: {v : e},v: {u : e,w : f}   --> vertex u is attacjed to vertex v via edge e, similarly vertex 'w' is attached to vertex 'v' via edge 'f'
        self._incoming = {} if directed == True else self._outgoing     # create another map called '_incoming' only if 'directed' is True else, just refer to _outgoing for undirected graphs

    def is_directed(self):
        return self._outgoing is not self._incoming         # if both _outgoing and _incoming maps are different, then it is a directed graph. 

    def vertex_count(self):
        return len(self._outgoing)
    
    def vertices(self):
        return self._outgoing.keys()                        # returns vertices of graph as a python list []

    def edge_count(self):
        edges = set()
        for eachDict in self._outgoing.values():
            edges.add(eachDict.values())
        return len(edges)
    
    def get_edge(self,u,v):
        return self._outgoing[u].get(v)                     # get(v) used because it returns None if v is not present in self._outgoing[u]. If we use self._outgoing[u][v], then it will give KeyError if v is not in self._outgoing[u]

    def degree(self,v,outgoing = True):
        dic = self._outgoing if outgoing else self._incoming
        return len(dic[v])
    
    def incident_edges(self,v,outgoing = True):
        dic = self._outgoing if outgoing else self._incoming
        for edge in dic[v].values():
            yield edge
    
    def insert_vertex(self,x = None):
        #v = Vertex(x).info                                       # Create new Vertex instance
        v = Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}                          # If directed graph, make an incoming edge
        return v
    
    def insert_edge(self,u,v,value = None):
        #e = Edge(u,v,value).info
        e = Edge(u,v,value)                                 # Create new Edge instance
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
        print(v)
    
    def get_vertex_dict(self):
        return self._outgoing

# ------------------------------------- Depth First Search ----------------------------------------

time = 0
def DFS(G):                                 
    vertex_map = G.get_vertex_dict()
    for vertex in G.vertices():
        vertex.color = 'WHITE'
        vertex.parent = None
    global time
    for u in vertex_map:
        if u.color == 'WHITE':
            DFS_Visit(G,u)

def DFS_Visit(G,u):
    vertex_map = G.get_vertex_dict()
    global time
    time = time + 1
    u.d = time
    u.color = 'GRAY'
    for v in vertex_map[u].keys():
        if v.color == 'WHITE':
            v.parent = u
            DFS_Visit(G,v)
    u.color = 'BLACK'
    time = time + 1
    u.f = time


g = Graph(directed = True)
u = g.insert_vertex('u')
v = g.insert_vertex('v')
x = g.insert_vertex('x')
y = g.insert_vertex('y')
w = g.insert_vertex('w')
z = g.insert_vertex('z')

g.insert_edge(u,v,'1')
g.insert_edge(u,x,'2')
g.insert_edge(x,v,'3')
g.insert_edge(y,x,'4')
g.insert_edge(v,y,'5')
g.insert_edge(w,y,'6')
g.insert_edge(w,z,'7')
g.insert_edge(z,z,'8')

DFS(g)



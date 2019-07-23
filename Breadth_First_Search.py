"""Author - Anantvir Singh, concept reference:= CLRS Page 595"""

import math
# constant length implementation
class Queue_List:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self.Q = [None] * Queue_List.DEFAULT_CAPACITY   
        self.n = 0                                      # keep track of current number of elements in the queue. This variable will eb helpful in creating dynamic array implementation
        self.front = None                               # pointer for front of list
        self.rear = None                                #pointer for rear of list

    def enqueue(self,item):
        if self.front==0 and self.rear == len(self.Q) - 1:
            print('Overflow')
        
        #------------find new rear-----------
        if self.rear == len(self.Q) - 1:
            self.rear = 0
        elif self.front == None:
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1
        #--------------------------------------
        self.Q[self.rear] = item
        self.n += 1     
        return self.Q

    def dequeue(self):
        if self.front == None:
            print('Underflow !')
        item = self.Q[self.front]
        self.Q[self.front] = None
        self.n -= 1
        #------------Find new front--------
        if self.front == self.rear:
            self.front = None
            self.rear = None
        elif self.front == len(self.Q) - 1:
            self.front = 0
        else:
            self.front += 1
        return item
    
    def is_Empty(self):
        return self.n == 0


# --------------------------- Adjaceny Map Representation of a Graph ----------------------------------------

class Vertex:
    def __init__(self,x):
        self._element = x
        self.color = None
        self.parent = None
        self.d = 0
    
    def element(self):
        return self._element
    
    def __hash__(self):
        return hash(id(self))       # Has function created so that a vertex can be used as a key in a dict or set as dict keys need to be hashable objects !

class Edge:
    def __init__(self,u,v,x):
        self._origin = u
        self._destination = v
        self._element = x
    
    def endpoints(self):                    # return (u,v) tuple for end points of this edge
        return (self._origin,self._destination)
    
    def opposite(self,v):                   # return vertex opposite to the given vertex v
        return self._origin if v is self._destination else self._origin
    
    def element(self):                      # Return value associated with this edge
        return self._element
    
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
        v = Vertex(x)                                      # Create new Vertex instance
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}                          # If directed graph, make an incoming edge
        return v
    
    def insert_edge(self,u,v,value = None):
        e = Edge(u,v,value)                                 # Create new Edge instance
        self._outgoing[u][v] = e
        self._outgoing[v][u] = e
        print(v)
    
    def get_vertex_dict(self):
        return self._outgoing


def Breadth_First_Search(G,s):
    l = list(G.vertices())              # Get all vertices as list []
    l.remove(s)                         # Remove source vertex, because source is already discovered, we dont need to set its color as WHITE and distance as infinity
    for vertex in l:                    # For each vertex, set color - white, distance = inf and parent = None
        vertex.color = 'WHITE'
        vertex.d = math.inf
        vertex.parent = None
    s.color = 'GRAY'                    # Because source has already been discovered, make it GRAY and distance = 0
    s.d = 0
    s.parent = None
    Q = Queue_List()
    Q.enqueue(s)                        # Add source to queue
    vertex_dict = G.get_vertex_dict()   # Get the hashmap representation of graph(Adjacency map representation)
    while not Q.is_Empty(): 
        u = Q.dequeue()
        for v in vertex_dict[u].keys(): # For each vertex in adjacency map of 'u'
            if v.color == 'WHITE':      # Basically it means for each neighbouring vertex of the currently dequeued vertex, discovered it and make it gray. Add 1 to its distance, make 'u' as its parent and enqueue this node. This is done because BFS is a level wise search. All nodes in a level are at equal distance from previous level.
                v.color = 'GRAY'
                v.d = u.d + 1
                v.parent = u
                Q.enqueue(v)
        u.color = 'BLACK'               # After all neighbours of a node have been discovered and made gray, make the node 'BLACK', meaning it has been completely processed



g = Graph()
r = g.insert_vertex('r')                # This graph is same as on CLRS page 596
v = g.insert_vertex('v')
s = g.insert_vertex('s')
w = g.insert_vertex('w')
t = g.insert_vertex('t')
x = g.insert_vertex('x')
u = g.insert_vertex('u')
y = g.insert_vertex('y')

g.insert_edge(r,v,'1')
g.insert_edge(r,s,'2')
g.insert_edge(s,w,'3')
g.insert_edge(w,t,'4')
g.insert_edge(w,x,'5')
g.insert_edge(t,x,'6')
g.insert_edge(t,u,'7')
g.insert_edge(u,y,'8')
g.insert_edge(x,y,'9')
Breadth_First_Search(g,s)


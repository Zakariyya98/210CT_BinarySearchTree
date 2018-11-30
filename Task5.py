#Task 3 Unweighted, Undirected Graph
class Vertex():
    def __init__ (self, nodes):
        #Nodes
        self.vertex = nodes
        #Connections/Adjecenies
        self.edge = []
    
class Graph():
    def __init__ (self):   
        self.list = {}
    
    def add_edge(self, node, edge):
        self.list.get(node).edge.append(edge)
        self.list.get(edge).edge.append(node) 
        
    def add_vertex(self, node):
        self.list[node] = Vertex(node)
    
    def print(self):
        print(self.list)
        
        
#Breadth-First Search Implementation 
        
    def BFS_Code (self, v):
        lst = []
        visited = []
        lst.append(v)
        while len(lst) > 0:
            lst2 = lst.pop(0)
            if lst2 not in visited:
                visited.append(lst2)
                for lst3 in self.list.get(lst2).edge:
                    lst.append(lst3)
        printtxt = open("Task5Node.txt", "a+")
        printtxt.write("This is the Path traversed for the Breadth-First Search" "\n")
        printtxt.write(str(visited))
        printtxt.close()
        return visited
    
#Depth-First Search Implementation
  
    def DFS_Code(self, v):
        lst = []
        visited = []
        lst.append(v)
        while len(lst) > 0:
            lst2 = lst.pop()
            if lst2 not in visited:
                visited.append(lst2)
                for lst3 in self.list.get(lst2).edge:
                    lst.append(lst3)
        printtxt = open("Task5Node.txt", "a+")
        printtxt.write("\n" "This is the Path traversed for the Depth-First Search" "\n")
        printtxt.write(str(visited))
        printtxt.close()
        return visited

G = Graph()
G.add_vertex(0)
G.add_vertex(1)
G.add_vertex(2)
G.add_vertex(3)
G.add_vertex(4)
G.add_vertex(5)
G.add_edge(0,1)
G.add_edge(0,3)
G.add_edge(0,2)
G.add_edge(1,3)
G.add_edge(2,1)
G.add_edge(2,4)
G.add_edge(1,4)
G.add_edge(3,1)
G.add_edge(4,3)
G.add_edge(3,5)
print(G.BFS_Code(0))
print(G.DFS_Code(0))
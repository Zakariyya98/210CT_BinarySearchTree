#Task 3 Unweighted, Undirected Graph

#The Vertex class will create the vertex to be instantiated with a list with
#the list as the object.
class Vertex():
    def __init__ (self, nodes):
        #Nodes
        self.vertex = nodes
        #Connections/Adjecenies
        self.edge = []
#This class will allow the structure for the graph to be created    
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
#Title: DFS Pseudocode
#Author: Hintea, D.
#Date November 2018
#Availability: http://cumoodle.coventry.ac.uk located in 210CT Week 7
#I Converted the Pseudocode to Python, added some of my own code too 

#This function will show check if there is a path between two nodes and will print
#the path traversal to a txt file.
    def isPath(self, v,w):
        lst = []
        visited = []
        lst.append(v)
        while len(lst) > 0:
            lst2 = lst.pop()
            if lst2 == w:
                visited.append(lst2)
                
                printtxt = open("isPath.txt", "w+")
                printtxt.write("This is the Path traversed" "\n")
                printtxt.write(str(visited))
                printtxt.close()
                
                break
            if lst2 not in visited:
                visited.append(lst2)
                for lst3 in self.list.get(lst2).edge:
                    lst.append(lst3)
        return visited
    
#Title: DFS Pseudocode
#Author: Hintea, D.
#Date November 2018
#Availability: http://cumoodle.coventry.ac.uk located in 210CT Week 7
#I Converted the Pseudocode to Python, added some of my own code too  

#This function will traverse the graph visting each vertex, it will use the current vertex
#edge to check the next vertex which is unvisited, as it traverses through each vertex
#it will mark them as visited and will keep repeating until all are marked.   
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
    
#Task 4 isConnected Implementation
#This Function will check to see if the Graph is Connected to every node and if each node is connected
#it will print yes or if its not connected will print no.

    def isConnected(self):
        if len(self.DFS_Code (0)) == len(self.list):
            print("Yes")
        else:
            print("No")         
#-----------------------------------------------------#
#These make up the nodes and connections in the graph, The Vertex being the Nodes and
#the edges being the connetions/adjecency. The last function call will check to see if
#the graph is connected.          

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
print(G.isPath(3,0))
G.isConnected()
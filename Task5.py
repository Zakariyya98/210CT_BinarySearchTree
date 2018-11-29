### Right BFS Implementation
def BFS_Code (self, v,w):
        lst = []
        visited = []
        lst.append(v)
        while len(lst) > 0:
            lst2 = lst.pop(0)
            if lst2 == w:
                visited.append(lst2)
                break
            if lst2 not in visited:
                visited.append(lst2)
                for lst3 in self.list.get(lst2).edge:
                    lst.append(lst3)
        return visited
#-----------------------------------------------------------------------
#Right DFS Implementation
def isPath(self, v,w):
        lst = []
        visited = []
        lst.append(v)
        while len(lst) > 0:
            lst2 = lst.pop()
            if lst2 == w:
                visited.append(lst2)
                break
            if lst2 not in visited:
                visited.append(lst2)
                for lst3 in self.list.get(lst2).edge:
                    lst.append(lst3)
        return visited
    
    
#---------------------------------------------------------------------------

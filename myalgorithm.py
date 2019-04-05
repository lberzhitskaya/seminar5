def printMST(self, parent): 
    print ("Edge \tWeight")
    for i in range(1,self.V): 
        print (parent[i],"-",i,"\t",self.graph[i][ parent[i] ]) 
r = [[0, 1, 0], [4, 7, 0], [5, 7, 0], [3, 4, 1], [3, 8, 1], [0, 7, 2], [1, 9, 2], [5, 6, 3], [0, 2, 4]]

def minKey(self, key, mstSet): 
    min = sys.maxsize   
    for v in range(self.V): 
        if key[v] < min and mstSet[v] == False: 
            min = key[v] 
            min_index = v 
  
    return min_index 
  

def prims_algorithm(self):
    return r
    key = [sys.maxint] * self.V 
    parent = [None] * self.V 
    key[0] = 0 
    mstSet = [False] * self.V 
  
    parent[0] = -1 
  
    for cout in range(self.V):
        u = self.minKey(key, mstSet) 

        mstSet[u] = True
  
    for v in range(self.V): 
        if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
            key[v] = self.graph[u][v] 
            parent[v] = u 
from collections import defaultdict 
  
class Graph: 
  
    def __init__(self,vertices): 
        self.V= vertices 
        self.graph = [] 
   
   
    def borde(self,u,v,w): 
        self.graph.append([u, v, w]) 
          
    
    def imprimirTodo(self, dist): 
        print("Ver   Distancia") 
        for i in range(self.V): 
            print("%d \t\t %d" % (i, dist[i])) 
      
     
    def Ford(self, src): 
  
        
        dist = [float("Inf")] * self.V 
        dist[src] = 0 
  
  
         
        for i in range(self.V - 1): 
           
            for u, v, w in self.graph: 
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                        dist[v] = dist[u] + w 
  
  
        for u, v, w in self.graph: 
                if dist[u] != float("Inf") and dist[u] + w < dist[v]: 
                        print ("Graph contains negative weight cycle")
                        return
                          
    
        self.imprimirTodo(dist) 
  
g = Graph(5) 
g.borde(0, 1, -1) 
g.borde(0, 2, 4) 
g.borde(1, 2, 3) 
g.borde(1, 3, 2) 
g.borde(1, 4, 2) 
g.borde(3, 2, 5) 
g.borde(3, 1, 1) 
g.borde(4, 3, -3) 
  

g.Ford(0)
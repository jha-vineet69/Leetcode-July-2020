class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:        
        edges = collections.defaultdict(list)   
        indeg = [0] * numCourses                
        re = []

        for second, first in prerequisites:     
            edges[first].append(second)         
            indeg[second] += 1                  
        
        queue = []                              
        for i in range(numCourses):
            if indeg[i] == 0:
                queue.append(i)

        while queue:
            u = queue.pop(0)
            re.append(u)
            for v in edges[u]:
                indeg[v] -= 1                   
                if indeg[v] == 0:              
                    queue.append(v)
        if len(re) != numCourses:
            re = []
        return re
    
        
            
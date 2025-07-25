
from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            if n > 1:
                return False 
            return True
        # write your code here
        def recurse(node, parent, nodes,seen):
            if node in seen:
                # print("Returning False:",node, parent, seen)
                return False
            seen.add(node)
            ans = True
            for connect in nodes[node]:
                if connect == parent:
                    continue
                ans = ans and recurse(connect, node, nodes, seen)
                if not ans:
                    return False
            return True
        
        nodes = {}
        for i in range(n):
            nodes[i] = []
        for edge in edges:
            nodes[edge[0]].append(edge[1])
            nodes[edge[1]].append(edge[0])
        seen = set()
        # print(nodes)
        ans = True
        for i in range(n):
            if len(nodes[i]) == 0:
                return False
            if i in seen:
                continue
            ans = ans and recurse(i,-1,nodes,seen)
            if not ans:
                return False
        
        return True

        


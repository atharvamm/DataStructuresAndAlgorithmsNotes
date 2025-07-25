
from typing import (
    List,
)

class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        def recurse(node, prev, nodes, seen):
            if node in seen:
                return None
            seen.add(node)
            for child in nodes[node]:
                if child != prev:
                    recurse(child, node, nodes, seen)
        
            return None

        nodes = {}        
        for i in range(n):
            nodes[i] = []
        
        for edge in edges:
            nodes[edge[0]].append(edge[1])
            nodes[edge[1]].append(edge[0])
        
        cc = 0
        seen = set()
        for i in range(n):
            if i not in seen:
                cc += 1
                recurse(i,-1,nodes,seen)
        return cc
            


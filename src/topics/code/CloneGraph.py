
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph_v1(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        head = node
        from collections import deque
        node_list = {}
        visited = set()
        list_nodes = deque([node])

        while list_nodes:
            cur_node = list_nodes.popleft()
            if cur_node.val not in visited:
                if cur_node.val not in node_list:
                    node_list[cur_node.val] = Node(cur_node.val, [])                
                new_node = node_list[cur_node.val]

                for cur_neighbor in cur_node.neighbors:
                    if cur_neighbor.val not in node_list:
                        node_list[cur_neighbor.val] = Node(cur_neighbor.val,[])                
                    new_neighbor = node_list[cur_neighbor.val]
                    new_node.neighbors.append(new_neighbor) 
                    list_nodes.append(cur_neighbor)
                visited.add(new_node.val)
        
        return node_list[head.val]
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        from collections import deque

        if node is None:
            return None        
        node_list = {}
        visited = set()
        list_nodes = deque([node])
        node_list[node.val] = Node(node.val,[])

        while list_nodes:
            cur_node = list_nodes.popleft()
            if cur_node.val not in visited:                
                new_node = node_list[cur_node.val]

                for cur_neighbor in cur_node.neighbors:
                    if cur_neighbor.val not in node_list:
                        node_list[cur_neighbor.val] = Node(cur_neighbor.val,[])                
                    new_neighbor = node_list[cur_neighbor.val]
                    new_node.neighbors.append(new_neighbor)
                    list_nodes.append(cur_neighbor)
                
                visited.add(new_node.val)
        
        return node_list[node.val]







        
## Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def generatelinkedlistfromlist(lst):
    nextEle,curEle = None, None
    for i in range(len(lst) - 1,-1,-1):
        curEle = ListNode(lst[i],nextEle)
        nextEle = curEle
    return nextEle

def view_linked_list(ans):
    while ans:
        print(ans.val,end = "->")
        ans = ans.next
    print()

## Binary Tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



# def generatebinarytreefromlist(lst):
#     if len(lst) == 0:
#         return None
#     root = None
#     parent,left,right = 0,1,2
#     nodes = {}
#     while True:
#         if parent not in nodes:
#             nodes[parent] = TreeNode(lst[parent])

#         # print(parent_node.val)
#         parent_node = nodes.get(parent)
#         if root is None:
#             root = parent_node

#         if right >= len(lst):
#             break

#         if left not in nodes:
#             if left >= len(lst):
#                 nodes[left] = None
#             elif lst[left] is None:
#                 nodes[left] = None
#             else:
#                 nodes[left] = TreeNode(lst[left])

#         if right not in nodes:
#             if right >= len(lst):
#                 nodes[right] = None
#             elif lst[right] is None:
#                 lst[right] = None
#             else:
#                 nodes[right] = TreeNode(lst[right])
    


#         parent_node.left = nodes.get(left)
#         parent_node.right = nodes.get(right)
        


#         parent += 1
#         left += 2
#         right += 2


#     return root
    

def generatebinarytreefromlist(nodes):
    if not nodes:
        return None
    
    # Initialize the root of the tree
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    
    # Iterate through the list and construct the tree
    while i < len(nodes):
        current = queue.pop(0)
        
        # Create left child if available
        if i < len(nodes) and nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        
        # Create right child if available
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    
    return root


def view_tree(root):
    # print(root,type(root))
    if root is None:
        return None
    
    ans = []
    
    if root.left is not None:
        ans.append(root.left.val)
    else:
        ans.append(None)
    ans.append(root.val)
    if root.right is not None:
        ans.append(root.right.val)
    else:
        ans.append(None)
    
    print("Val,Left,Right:",ans[0],"<--",ans[1],"-->",ans[2])
    view_tree(root.left)
    view_tree(root.right)

## Display 2D Matrix
def view_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end = " ")
        print()


## Graphs
class GraphNode:
    def __init__(self, x):
        self.val = x
        self.neighbors = []

## Undirected Graph
def createundirectedgraph(edges):
    if not edges:
        return []

    node_dict = {}

    for edge in edges:
        node1_val, node2_val = edge

        if node1_val not in node_dict:
            node_dict[node1_val] = GraphNode(node1_val)
        if node2_val not in node_dict:
            node_dict[node2_val] = GraphNode(node2_val)

        node1 = node_dict[node1_val]
        node2 = node_dict[node2_val]

        node1.neighbors.append(node2)
        node2.neighbors.append(node1)

    return list(node_dict.values())




if __name__ == "__main__":
    # Binary Tree
    a = [3,5,1,6,2,0,8,None,None,7,4]
    btree = generatebinarytreefromlist(a)
    view_tree(btree)


    # Linked List



    # Graph



## Print Dynamic Programming Table

'''
# Show DP TABLE
def printTable(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j],end = " ")
        print()
'''
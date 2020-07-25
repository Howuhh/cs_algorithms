# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        cloned = {}
        
        def _clone(node):
            if node not in cloned:
                cloned[node] = Node(node.val)
                
                for neigh in node.neighbors:
                    _clone(neigh)
                    cloned[node].neighbors.append(cloned[neigh])
        
        _clone(node)
        return cloned[node]

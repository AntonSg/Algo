
class Node():
    def __init__(self,val:int):
        self.val = val
        self.left = None
        self.right = None


tree = Node(0)
tree.left = Node(1)
tree.right = Node(2)
tree.left.left = Node(3)
tree.left.right = Node(4)
tree.left.left.left = Node(5)
tree.left.left.right = Node(6)
tree.right.left = Node(7)
tree.right.right = Node(8)

tree = """
      0
    /   \
   1     2
  / \   / \
 3   4  7  8
/ \   
5  6  
"""
global l
l = []
def dfs(node,l):
    l.append(node.val)
    if node.left is not None:
        dfs(node.left,l)
        dfs(node.right,l)

dfs(tree,l)
print(l)



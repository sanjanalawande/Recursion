class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        

def preorder_print(root):
    #Root->Left->Right
    if not root:
        return 
    print(root.data)
    preorder_print(root.left)
    preorder_print(root.right)


def inorder_print(root):
    #Left->Root->Right
    if not root:
        return 
    inorder_print(root.left)
    print(root.data)
    inorder_print(root.right)
    
    
def postorder_print(root):
    #Left->Right->Root
    if not root:
        return 
    postorder_print(root.left)
    postorder_print(root.right)
    print(root.data)
    
    
    
if __name__ == "__main__":
    #Set up Tree 
    root = Node("F")
    root.left = Node("D")
    root.left.left = Node("B")
    root.left.left.left = Node("A")
    root.left.left.right = Node("C")
    root.left.right = Node("E")
    root.right = Node("I")
    root.right.left = Node("G")
    root.right.left.right = Node("H")
    root.right.right = Node("J")
    
print("PreOrder: ", preorder_print(root))
print("PostOrder: ", postorder_print(root))
print("InOrder: ", inorder_print(root))
        
        
        
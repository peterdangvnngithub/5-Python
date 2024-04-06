class Node:
    def __init__(self, key):
        self.left   = None
        self.right  = None
        self.key    = key

class Binary_Tree:
    def __init__(self):
        self.root   = None

    def insert(self, key):
        if not self.root:
            self.root   = Node(key)
        else:
            self.insert_recursive(self.root, key)

    def insert_recursive(self, current_Node, key):
        if key < current_Node.key:
            if current_Node.left is None:
                current_Node.left   = Node(key)
            else:
                self.insert_recursive(current_Node.left, key)
        else:
            if current_Node.right is None:
                current_Node.right  = Node(key)
            else:
                self.insert_recursive(current_Node.right, key)
    
    def in_order(self, current_Node):
        # Recursion
        if current_Node is not None:
            self.in_order(current_Node.left)
            # print(current_Node.key, end=" ")
            self.in_order(current_Node.right)
        # 
    
    def pre_order(self, current_Node):
        # Recursion
        if current_Node is not None:
            # print(current_Node.key, end=" ")
            self.pre_order(current_Node.left)
            self.pre_order(current_Node.right)
        return True
    
    def post_order(self, current_Node):
        if current_Node is not None:
            self.post_order(current_Node.left)
            self.post_order(current_Node.right)
            #print(current_Node.key, end=" ")
        return True

    def print_binary_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            # print(" " * (level * 4) + prefix + str(node.key))
            self.print_binary_tree(node.left, level + 1, "L---- ")
            self.print_binary_tree(node.right, level + 1, "R---- ")

# Tạo cây nhị phân
binary_Tree = Binary_Tree()
data = [5, 3, 7, 2, 4, 6, 8]

binary_Tree.insert(5)
binary_Tree.insert(3)
binary_Tree.insert(4)
binary_Tree.insert(2)
binary_Tree.insert(7)
binary_Tree.insert(6)
binary_Tree.insert(8)

binary_Tree.print_binary_tree(binary_Tree.root)
print("Traversal Inorder:")
binary_Tree.in_order(binary_Tree.root)
print("\nTraversal Preorder:")
binary_Tree.pre_order(binary_Tree.root)
print("\nTraversal Postorder:")
binary_Tree.post_order(binary_Tree.root)
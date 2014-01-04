class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def lookup(self, data, parent=None):

        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            # computes the two depths
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            # returns the appropriate depth
            return max(left_depth, right_depth) + 1

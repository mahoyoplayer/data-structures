from typing import Optional
class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self, root:Optional[Node] = None):
        self.root = root

    # Check if value is present in BST
    def search(self, val: int) -> bool:
        curr = self.root
        while curr:
            if curr.val == val:
                return True
            elif curr.val < val:
                curr = curr.left
            else:
                curr = curr.right
        return False

    # Add value to BST
    def add(self, val: int) -> bool:
        if not self.root:
            self.root = Node(val)
            return True
        curr = self.root
        while True:
            if val < curr.val:
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(val)
                    return True
            elif val > curr.val:
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node.val
                    return True
            else:
                # Value is already inside BST
                return False

    # Remove value from BST 
    def remove(self, val: int) -> bool:
        curr = self.root
        while curr:
            return
            if curr.val == val:
                pass
        return


    # Return height at which value is at
    def height(self, val) -> int:
        curr, h = self.root, 0
        while curr:
            if val == curr.val:
                return h
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
            h += 1
        return -1

if __name__ == "__main__":
    print("Hello World")

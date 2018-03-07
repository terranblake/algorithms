import sys
import os
sys.path.insert(0, os.path.join('C:\\Users\\terra\\Documents\\coursera\\algorithms-pt1\\data_structures\\'))

from bst_node import BST_Node
from binarysearchtree import BinarySearchTree

class TreeTraversal(object):
    def __init__(self, elements=None):
        if not elements or not len(elements) > 1:
            raise ValueError('Please provide data to traverse.')

        self.tree = BinarySearchTree(BST_Node(elements.pop(0)))
        print(self.tree.head)
        
        for element in elements:
            self.tree.insert(element)

    # Left - Root - Right
    def inorder(self, node=None):
        if node:
            self.inorder(node.get_next('left'))
            print(node.data)
            self.inorder(node.get_next('right'))

    # Root - Left - Right
    def preorder(self, node=None):
        if node:
            print(node.data)
            self.inorder(node.get_next('left'))
            self.inorder(node.get_next('right'))

    # Left - Right - Root
    def postorder(self, node=None):
        if node:
            self.inorder(node.get_next('left'))
            self.inorder(node.get_next('right'))
            print(node.data)
    
    def breadthfirst(self):
        raise NotImplementedError

def main():
    my_tree = TreeTraversal([25, 12, 10, 14, 50])

    my_tree.inorder(my_tree.tree.head)
    my_tree.preorder(my_tree.tree.head)
    my_tree.postorder(my_tree.tree.head)

if __name__ == '__main__':
    main()
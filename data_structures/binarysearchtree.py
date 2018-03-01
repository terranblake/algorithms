from bst_node import BST_Node

class BinarySearchTree(object):
    def __init__(self, head=None):
        if head and type(head) is BST_Node:
            self.head = head
        else:
            self.invalid_type_error(type(head))

    def insert(self, data=None):
        raise NotImplementedError

    def invalid_type_error(self, dtype):
        raise TypeError('\
            <class \'BinarySearchTree\'> requires elements of type <class \'BST_Node\'>. \
            You provided element of type {}'.format(dtype)
            )
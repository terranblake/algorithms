from bst_node import BST_Node


class BinarySearchTree(object):
    def __init__(self, head=None):
        self.path = []

        if head and type(head) is BST_Node:
            self.head = head
        else:
            self.invalid_type_error(type(head))

    # Navigate based upon the left and right
    #   paths of the current <class 'BST_Node'>,
    #   then insert the node at the resultant position
    def insert(self, data=None, node=None):
        new_node = BST_Node(data)

        if node is None:
            # Reset path
            self.path = [self.head.get_data()]
            self.insert(data, self.head)
        else:
            node_data = node.get_data()

            # Navigate down left branch
            if data < node_data:
                node_left = node.get_next('left')

                # If next branch exists, navigate
                if node_left:
                    # Add current location to path
                    print(node_data, ' > ', data, '\nNavigate Left')
                    self.path.append(node_left.get_data())

                    self.insert(data, node_left)
                # Else, place new node
                else:
                    print(node_data, ' > ', data, '\nInserting Node on Left\n')
                    node.set_next('left', new_node)
                    return True

            # Navigate down right branch
            elif data > node_data:
                node_right = node.get_next('right')

                # If next branch exists, navigate
                if node_right:
                    # Add current location to path
                    print(node_data, ' < ', data, '\nNavigate Right')
                    self.path.append(node_right.get_data())

                    self.insert(data, node_right)
                # Else, place new node
                else:
                    print(node_data, ' < ', data, '\nInserting Node on Right\n')
                    node.set_next('right', new_node)
                    return True
            else:
                return False

    # Navigate based upon whether the left and
    #   right <class 'BST_Node'> data values
    #   are less than, or greater, than 'value'.
    #   return None if 'value is not found, else
    #   return the <class 'BST_Node'> that matches 'value'
    def search(self, value=None, node=None):

        if node is None:
            self.path = []

            if value is None:
                raise ValueError('Please provide a value of type < class \'int\'> to search with.')
            else:
                print('Passing head to search function.\n', self.head.get_data())
                # Recursive call to begin searching with the head of this tree
                self.search(value=value, node=self.head)
        else:
            node_data = node.get_data()
            self.path.append(node_data)

            # Standard search functionality
            if value < node_data:
                if node.get_next('left'):
                    self.search(value, node.get_next('left'))
                else:
                    self.path = ['No Path Found']
            elif value > node_data:
                if node.get_next('right'):
                    self.search(value, node.get_next('right'))
                else:
                    self.path = ['No Path Found']
            elif value == node_data:
                return True
            else:
                self.path = ['No Path Found']

    # Navigate with self.search(value), if found, remove
    #   and reshuffle tree to comply with BST rules
    def delete(self, value=None):
        raise NotImplementedError

    # An invalid type was provided for a <class 'BST_Node'> input
    def invalid_type_error(self, dtype):
        raise TypeError('\
            <class \'BinarySearchTree\'> requires elements of type <class \'BST_Node\'>. \
            You provided element of type {}'.format(dtype)
                        )


def main():
    test_set = ['3', '10', '1', '6', '14', '4', '7', '13']

    myBST = BinarySearchTree(BST_Node(8))

    for item in test_set:
        print(myBST.insert(int(item)))
        print(myBST.path, '\t', item, '\n')

    treeHead = myBST.head

    headData = treeHead.get_next('left')
    print(headData.get_data())

    myBST.search(50)
    print(myBST.path)


if __name__ == '__main__':
    main()

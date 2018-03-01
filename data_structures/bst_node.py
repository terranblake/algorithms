# Simple Binary Search Tree Node
class BST_Node(object):
    def __init__(self, data=None):
        if not data:
            raise ValueError('Please provide a value to the Node constructor.')
        elif type(data) is not int:
            raise ValueError('Required type for <class \'Node\'> data, is of type <class \'int\'>. \
                                    \nYou provided data of type {}.'.format(type(data)))
        else:
            self.data = data
            self.left = None
            self.right = None

    # Returns the left or right Node, if it has been set
    def get_next(self, side=None):
        if(side == 'left' and self.left):
            return self.left
        elif(side == 'right' and self.right):
            return self.right
        else:
            return None
        # Implement for strict type checking
            # if(side == ('left' or 'right') and not self.left):
            #     raise ValueError('The \'{}\' node has not been set. Please set it with <Node>.set_next() first.'.format(side))
            # else:
            #     self.invalid_side_error(side)

    # Sets the left or right Node, if provided with a valid Node object
    def set_next(self, side=None, data=None):
        if(type(data) == BST_Node):
            if(side == 'left'):
                self.left = data
            elif(side == 'right'):
                self.right = data
            else:
                self.invalid_side_error(side)
        else:
            raise ValueError('Required type is of <class \'Node\'>. \
                                    \nYou provided data of type {}.'.format(type(data)))

    # Error for invalid provided side
    def invalid_side_error(self, side=None):
        raise ValueError('The requested side is invalid. \'{}\' \
                \nPlease try \'left\' or \'right\'.'.format(side))
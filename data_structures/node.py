class Node(object):
    def __init__(self, data=None):
        if not data:
            raise ValueError('Please provide a value to the Node constructor.')
        elif type(data) is not int:
            raise ValueError('Required type for <class \'Node\'> data, is of type <class \'int\'>. \
                                    \nYou provided data of type {}.'.format(type(data)))
        else:
            self.data = data

    def get_data(self):
        return self.data

    def get_next(self):
        if(self.next_node):
            return self.next_node
        else:
            raise ValueError('Next Node has not been set.')

    def set_next(self, new_next=None):
        if(type(new_next) == Node):
            self.next_node = new_next
        else:
            raise ValueError('Required type is of <class \'Node\'>. \
                                    \nYou provided data of type {}.'.format(type(new_next)))
from node import Node

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data=None):
        self.new_node = Node(data)
        self.new_node.set_next(self.head)
        self.head = self.new_node

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.get_next()

        return count

    def search(self, data):
        current = self.head
        found = False
        count = 0

        while current and found is False:
            count += 1
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()

        if current is None:
            raise ValueError('Data is not in list!')
        else:
            print('\nValue `' + str(data) +
                  '` found at Node #{}'.format(str(count)))

        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False

        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()

        if current is None:
            raise ValueError('\nData is not in list!')

        if previous is None:
            current = current.get_next()
        else:
            previous.set_next(current.get_next())

        return current

    def print(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            print('Node #' + str(count) + '\t' + str(current.get_data()))
            current = current.get_next()

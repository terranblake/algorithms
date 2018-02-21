from linkedlist import LinkedList
from node import Node


class Queue(object):
    def __init__(self):
        self.list = LinkedList()
        self.last = Node()

    def is_empty(self):
        return self.list.head is None

    def dequeue(self):
        if self.list.head:
            result = self.list.head
            self.list.head = self.list.head.get_next()
            return result.get_data()
        else:
            print('Queue is empty!')

    def enqueue(self, new_data):
        new_last = Node(new_data)

        if self.list.head is None:
            self.list.head = new_last
            self.last = new_last
        
        self.last.set_next(new_last)
        self.last = new_last
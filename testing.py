from linkedlist import LinkedList
from node import Node
from stack import Stack

from random import random


class test_linkedlist(object):

    def __init__(self, items):
        self.data = LinkedList()

        for item in items:
            self.data.insert(item)

    def insert(self, data):
        self.data.insert(data)

    def print(self):
        self.data.print()

    def search(self, data):
        self.data.search(data)

    def search_empty(self):
        self.data = LinkedList()
        self.data.search(15)


if __name__ == '__main__':
    test = test_linkedlist(['1', '3', '5', '7', '9'])
    # test.print()
    # test.insert(15)

    # test.print()
    # test.search(15)

    test.search_empty()
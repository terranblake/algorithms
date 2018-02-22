from linkedlist import LinkedList
from node import Node


class Stack(object):
    def __init__(self):
        self.list = LinkedList()
        self.list.head = None
        self.iter = None

    def is_empty(self):
        return self.current.get_next()

    def find(self, data):
        return self.list.search(data)

    def __next__(self):
        if self.has_next():
            current = self.iter
            self.iter = self.iter.get_next()
            return current.get_data()
        else:
            raise ValueError('The end of the Stack has been reached!')

    def has_next(self):
        return self.iter

    def pop(self):
        if self.list.head:
            result = self.list.head
            self.list.head = self.list.head.get_next()
            return result.get_data()
        else:
            raise ValueError('No elements in the Stack!')

    def push(self, new_data):
        self.current = self.list.head
        self.list.head = Node(new_data)
        self.list.head.set_next(self.current)
        self.iter = self.list.head


def main():
    myStack = Stack()

    for word in 'To be or not to be, that is the question?'.split(' '):
        myStack.push(word)

    print(myStack.find('question?'))


if __name__ == '__main__':
    main()

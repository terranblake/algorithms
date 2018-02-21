from linkedlist import LinkedList
from node import Node


class Queue(object):
    def __init__(self):
        self.list = LinkedList()
        self.last = Node()
        self.iter = None

    def is_empty(self):
        return self.list.head is None

    def __next__(self):
        if self.has_next():
            current = self.iter
            self.iter = self.iter.get_next()
            return current.get_data()
        else:
            raise ValueError('The end of the Stack has been reached!')

    def has_next(self):
        return self.iter

    def dequeue(self):
        if self.list.head:
            result = self.list.head
            self.list.head = self.list.head.get_next()
            return result.get_data()
        else:
            raise ValueError('\nNo elements in the Queue!')

    def enqueue(self, new_data):
        new_last = Node(new_data)

        if self.list.head is None:
            self.list.head = new_last
            self.last = new_last

        self.last.set_next(new_last)
        self.last = new_last

        self.iter = self.list.head


def main():
    myQueue = Queue()

    for word in 'To be or not to be, that is the question'.split(' '):
        myQueue.enqueue(word)

    print(myQueue.__next__())


if __name__ == '__main__':
    main()
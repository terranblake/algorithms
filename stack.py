from linkedlist import LinkedList
from node import Node


class Stack(object):
    def __init__(self):
        self.list = LinkedList()

    def is_empty(self):
        return self.list.head is None

    def pop(self):
        if self.list.head:
            result = self.list.head
            self.list.head = self.list.head.get_next()
            return result.get_data()
        else:
            print('Stack is empty!')

    def push(self, new_data):
        current = self.list.head
        self.list.head = Node(new_data)
        self.list.head.set_next(current)
        print(self.list.head.get_data())

if __name__ == '__main__':
    myStack = Stack()

    myStack.push('m')
    myStack.push('i')
    myStack.push('n')
    myStack.push('d')

    myStack.pop()

    print(myStack.pop())
    print(myStack.pop())
    print(myStack.pop())
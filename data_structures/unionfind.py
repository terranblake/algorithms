from random import randint


class UnionFind(object):
    def __init__(self, size=None):
        if size < 2:
            raise Exception(
                '-- Please enter a value equal, or greater, than 2.--')

        component = []

    def union(self, first=None, second=None):
        raise NotImplementedError

    def connected(self, first=None, second=None):
        raise NotImplementedError

    def find(self, element=None):
        raise NotImplementedError

    def count(self):
        raise NotImplementedError

def main():
    size = 20
    my_uf = UnionFind()


if __name__ == '__main__':
    main()

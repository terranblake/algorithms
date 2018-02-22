import errno


class Percolation(object):
    def __init__(self, size=None):
        raise NotImplementedError

    def open(self, row=None, column=None):
        raise NotImplementedError

    def isOpen(self, row=None, column=None):
        raise NotImplementedError

    def isFull(self, row=None, column=None):
        raise NotImplementedError

    def numberOfOpenSites(self):
        raise NotImplementedError

    def percolates(self):
        raise NotImplementedError


def main():
    my_percolation = Percolation(5)


if __name__ == '__main__':
    main()

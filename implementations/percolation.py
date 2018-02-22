from random import randint

class Percolation(object):
    def __init__(self, size=None):
        if size < 1:
            raise Exception('-- Please enter a value equal, or greater, than 1.--')

        self.grid = []

        for x in range(size):
                self.grid.append(['x'] * size)

    def open(self, row=None, column=None):
        if row > len(self.grid) or column > len(self.grid):
            raise Exception('-- Please enter values equal, or less, than {}.--'.format(len(self.grid)))
        elif row < 1 or column < 1:
            raise Exception('-- Please enter values equal, or greater, than 1.')

        if self.isOpen(row, column):
            self.grid[row - 1][column - 1] = 'o'

    def isOpen(self, row=None, column=None):
        return self.grid[row - 1][column - 1] == 'x'

    def isFull(self, row=None, column=None):
        raise NotImplementedError

    def numberOfOpenSites(self):
        open_sites = 0

        for columns in self.grid:
            for item in columns:
                if item == 'o':open_sites += 1
        
        return 'There are {} open sites in the grid.'.format(open_sites)

    def displayGrid(self):
        for x in range(len(self.grid)):
            print(self.grid[x])

    def percolates(self):
        raise NotImplementedError


def main():
    my_percolation = Percolation(10)

    for x in range(50):
        row = randint(1, 10)
        col = randint(1, 10)

        my_percolation.open(row, col)

    my_percolation.displayGrid()
    print('\n', my_percolation.numberOfOpenSites())

if __name__ == '__main__':
    main()

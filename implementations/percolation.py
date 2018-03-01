from random import randint

class Percolation(object):
    def __init__(self, size=None):
        if size < 1:
            raise Exception('-- Please enter a value equal, or greater, than 1.--')

        self.grid = []

        for x in range(size):
                self.grid.append(['`'] * size)

    def open(self, row=None, column=None):
        if row > len(self.grid) or column > len(self.grid):
            raise Exception('-- Please enter values equal, or less, than {}.--'.format(len(self.grid)))
        elif row < 1 or column < 1:
            raise Exception('-- Please enter values equal, or greater, than 1.')

        if self.isOpen(row, column):
            self.grid[row - 1][column - 1] = '☐'

    def isOpen(self, row=None, column=None):
        return self.grid[row - 1][column - 1] == '`'

    # Site that connects to the top row of the grid
    def isFull(self, row=None, column=None):
        raise NotImplementedError

    def numberOfOpenSites(self):
        open_sites = 0

        for columns in self.grid:
            for item in columns:
                if item == '☐': open_sites += 1
        
        return open_sites

    def displayGrid(self):
        for x in range(len(self.grid)):
            print(self.grid[x])

    def percolates(self):
        raise NotImplementedError


def main():
    size = 20
    my_percolation = Percolation(size)

    for x in range(300):
        row = randint(1, size)
        col = randint(1, size)

        my_percolation.open(row, col)

    my_percolation.displayGrid()
    print('\n', my_percolation.numberOfOpenSites())

if __name__ == '__main__':
    main()
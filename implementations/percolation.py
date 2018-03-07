from random import randint

class Percolation(object):
    def __init__(self, size=None):
        if size < 1:
            raise Exception('-- Please enter a value equal, or greater, than 1.--')

        self.grid = []

        for x in range(size):
            self.grid.append([UF_Node(data=x, rank=x)] * size)

    def open(self, row=None, column=None):
        if row > len(self.grid) or column > len(self.grid):
            raise Exception('-- Please enter values equal, or less, than {}.--'.format(len(self.grid)))
        elif row < 1 or column < 1:
            raise Exception('-- Please enter values equal, or greater, than 1.')

        if not self.isOpen(row, column):
            self.open(row=row, column=column)

    def isOpen(self, row=None, column=None):
        return self.grid[row - 1][column - 1].open == True

    # Site that connects to the top row of the grid
    # This is essentially the same as the connected() in UnionFind,
    #   modified to account for a Node connected to the top row
    def isFull(self, row=None, column=None):
        if self.isOpen(row=row, column=column):
            for node in self.grid[0]:
                if self.grid[row - 1][column - 1].rank == node.rank:
                    return True
            
        return False

    def numberOfOpenSites(self):
        open_sites = 0

        for columns in self.grid:
            for item in columns:
                if item.open: open_sites += 1
        
        return open_sites

    def displayGrid(self):
        raise NotImplementedError

    def percolates(self):
        for row in self.grid:
            print([col.open for col in row])
                


def main():
    size = 20
    my_percolation = Percolation(size)

    my_percolation.percolates()

    my_percolation.open(5, 4)

    for x in range(300):
        row = randint(1, size)
        col = randint(1, size)

        my_percolation.open(row, col)

    my_percolation.displayGrid()
    print('\n', my_percolation.numberOfOpenSites())

    my_percolation.percolates()

if __name__ == '__main__':
    main()
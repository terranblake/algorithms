from random import randint

class UF_Node(object):
    def __init__(self, data, rank):
        # None implies that the Node is the parent
        self.data = data
        self.rank = rank

class UnionFind(object):
    def __init__(self, num=None):
        if num > 0:
            self.components = []
            self.numComponents = num

            for x in range(0, num):
                self.components.append(UF_Node(data=x, rank=x))
                
        else:
            raise ValueError('Please provide data.')

    def validate(self, value):
        if not value <= len(self.components) or not value >= 0:
            return False

        return True

    def union(self, this=None, on=None):
        print(this, 'union on', on)

        if this < 0 or on < 0:
            raise ValueError('Invalid inputs provided.')

        if self.connected(this, on):
            print(this, ' and ', on, ' are already in the same set.')
            return
        
        self.components[this].rank = self.find(on)

        # Since we can infer that there will be 1 less set after a Union
        self.numComponents -= 1

    def connected(self, first=None, second=None):
        return self.find(first) == self.find(second)

    def find(self, this=None):
        if not self.validate(this):
            return False

        return self.components[this].rank

    def count(self, value):
        if not self.validate(value):
            return

        return sum([1 for comp in self.components if comp.rank == value])

    def count_all(self):
        return [self.count(x.data) for x in self.components]

def main():
    my_UF = UnionFind(10)

    print([node.rank for node in my_UF.components])
    print([node.data for node in my_UF.components])
    print('\n')

    my_UF.union(2, 1)
    my_UF.union(4, 3)
    my_UF.union(8, 4)
    my_UF.union(9, 3)
    my_UF.union(0, 4)
    my_UF.union(1, 8)
    my_UF.union(5, 6)
    my_UF.union(6, 7)

    print('\n')
    print([node.rank for node in my_UF.components])
    print([node.data for node in my_UF.components])
    print('\n')
    print(my_UF.numComponents)

if __name__ == '__main__':
    main()

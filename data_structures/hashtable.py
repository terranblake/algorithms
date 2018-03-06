class HashTable(object):
    def __init__(self, size=None):
        self.table = {}

        if size and size > 1:
            self.size = size

    # Call basic_hash(self, result), insert { hash: value }, return hashed equivalent of value
    def insert(self, value):
        if value:
            hashed = self.basic_hash(value)
            self.table[hashed] = value
            
            return {value: hashed}

        return ValueError('Please provide something to input.')

    # Call search(self, value), delete and return hashed equivalent
    def delete(self, value):
        self.table[self.basic_hash(value)] = None

    # If value exists, return hashed equivalent, else ValueError
    def search(self, value):
        hashed = self.basic_hash(value)

        for idx, elm in self.table.items():
            if idx == hashed and elm == value:
                return idx
            
        return ValueError('Provided input not found in table.')

    # Hash value, return result of hashing
    def basic_hash(self, value):
        return sum([ord(x) for x in value]) % self.size

    def print(self):
        return self.table

def main():

    myTable = HashTable(10)

    # Test insert function
    myTable.insert('John Doe')
    myTable.insert('Jane Doe')
    myTable.insert('Jackson Johnson')
    myTable.insert('Matthew Matthews')
    print(myTable.insert('')) # Should return error

    # Test delete function
    myTable.delete('Jane Doe')

    # Test search function
    print('Jackson Johnson can be found at index:\t{}'.format(myTable.search('Jackson Johnson')))
    print(myTable.search('Jane Doe')) # Should return error, since this does not exist

    print(myTable.print())

if __name__ == '__main__':
    main()
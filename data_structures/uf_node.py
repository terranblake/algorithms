class UF_Node(object):
    def __init__(self, data, rank):
        # None implies that the Node is the parent
        self.data = data
        self.rank = rank
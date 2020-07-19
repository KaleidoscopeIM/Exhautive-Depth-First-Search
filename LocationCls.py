class LocationCLs:
    def __init__(self, anode):
        self.root = anode[0]
        self.locationX = int(anode[1])
        self.locationY = int(anode[2])

    def get_node_root(self):
        return self.root



import re


def get_type(key):
    alphanumeric_list = re.split('([0-9]+)', key)
    for a in alphanumeric_list:
        if a != '':
            if a.isdigit():
                return 'DIGIT'
            else:
                return'STRING'


class NodeCls:
    def __init__(self, anode):
        self.root = anode[0]
        if len(anode) != 1:
            self.connections = int(anode[1])
        else:
            self.connections = 0
        self.neighbours = []
        self.visited = False
        i = 0
        while i < len(anode):
            if i == 0 or i == 1:
                i = i + 1
                continue
            self.neighbours.append(anode[i])
            # self.visited.append(False)
            i = i + 1
        self.alphanumeric_sort()

    def get_node_root(self):
        return self.root

    # def get_next_not_visited(self):
    #     i = 0
    #     next_node = ''
    #     while i < self.connections:
    #         if self.visited[i] is False:
    #             next_node = self.neighbours[i]
    #             self.visited[i] = True
    #             break
    #         i = i+1
    #     return next_node

    def alphanumeric_sort(self):
        numeric_list = []
        alphabetic_list = []
        for an in self.neighbours:
            if get_type(an) == "DIGIT":
                numeric_list.append(an)
            else:
                alphabetic_list.append(an)
        alphabetic_list.sort()
        numeric_list.sort()
        self.neighbours = alphabetic_list + numeric_list


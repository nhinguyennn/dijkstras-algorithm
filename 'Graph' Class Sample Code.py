# NOTE: This sample code was given by my professor, Sung Hee Nam to test the implementation. 
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)
        
    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

# This method is for MST only
    def initializeDistances(self):
        for i in self.nodes:
            for j in self.nodes:
                self.distances[(i, j)] = sys.maxsize
                
        for i in self.nodes:
            self.distances[(i, "")] = 0

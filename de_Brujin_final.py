from graphviz import Digraph
import sys
sys.setrecursionlimit(10**6)

def clean_data(path, lines):  #Processes data from the dataset and returns the DNA sequence
    f = open(path) #path = path to dataset file, lines = no. of lines to extract from dataset
    f1 = f.readlines() 
    dna = ""
    for i in range(lines):
        f1[i] = f1[i].split()
        if f1[i][3][0] in ["A", "G", "T", "C"] and f1[i][3][1] in ["A", "G", "T", "C"]: #cleaning data
            dna += f1[i][3]
    return dna


def kMerMaker(string, kMerLength): #generates k-mers from DNA sequence
    if (kMerLength) > len(string):
        return "This is not possible"

    kMers = []
    for i in range(len(string) - kMerLength + 1):
        kMers.append(string[i:i + kMerLength])

    return kMers


class de_brujin: #DeBruijn Graph class

    def __init__(self, k_mers): #takes k-mers to create a graph
        self.vertices, self.graph, self.indegrees, self.outdegrees = self._makeGraph(k_mers) # k-1mers
        self.path = []

    def _makeGraph(self, k_mers): #function to create the graph
        vertices = []
        graph = {}
        indegrees = {}
        outdegrees = {}

        for k_mer in k_mers:
            left_mer = k_mer[0:len(k_mer) - 1] #dividing into k-1 - mers. 
            right_mer = k_mer[1:len(k_mer)]

            if left_mer not in vertices:
                vertices.append(left_mer)
            if right_mer not in vertices:
                vertices.append(right_mer)

            i = 0
            while True:
                if (( left_mer, right_mer, i)) not in graph.get(left_mer, []):
                    graph[left_mer] = graph.get(left_mer, []) + [( left_mer, right_mer, i)]
                    break
                i += 1

            graph[right_mer] = graph.get(right_mer, [])


            outdegrees[left_mer] = outdegrees.get(left_mer, 0) + 1
            indegrees[right_mer] = indegrees.get(right_mer, 0) + 1

            outdegrees[right_mer] = outdegrees.get(right_mer, 0)
            indegrees[left_mer] = indegrees.get(left_mer, 0)


        return (vertices, graph, indegrees, outdegrees)

    def addEdge(self, vertex1, vertex2): #add edges in the graph
        i = 0
        while True:
            if (( vertex1, vertex2, i)) not in self.graph.get(vertex1, []):
                self.graph[vertex1] = self.graph.get(vertex1, []) + [( vertex1, vertex1, i)]
                break
            i += 1

        self.outdegrees[vertex1] = self.outdegrees[vertex1] + 1
        self.indegrees[vertex2] = self.indegrees[vertex2] + 1

    def rmvEdge(self, vertex, nextVertex):  #remove vertex from the graph
        for i in range(len(self.graph[vertex])):
            if self.graph[vertex][i] == nextVertex:
                self.graph[vertex].pop(i)
                break
        self.outdegrees[vertex] = self.outdegrees[vertex] - 1
        self.indegrees[nextVertex] = self.indegrees[nextVertex] - 1

    def findEulerPath(self):    #Eulerian Walk
            startNode = ""
            endNode = ""

            for vertex in self.vertices:
                if self.indegrees.get(vertex, 0) + 1 == self.outdegrees.get(vertex, 0):
                    startNode = vertex

                if self.indegrees.get(vertex, 0) == self.outdegrees.get(vertex, 0) + 1:
                    endNode = vertex

            self.addEdge(endNode, startNode)
            graph.showGraph()


            self.runDFS(startNode)

            self.path = self.path[1:]
            self.path = self.path[::-1]

            finalString = ""
            for node in self.path:
                if finalString == "":
                    finalString = node
                else:
                    finalString += node[-1]

            return finalString

    def runDFS(self, current, visited = []):
            while self.outdegrees.get(current, 0) != 0:
                for edge in self.graph[current]:
                    if edge not in visited:
                        visited.append(edge)
                        self.outdegrees[current] = self.outdegrees[current] - 1
                        self.runDFS(edge[1], visited)
            self.path.append(current)

    def showGraph(self): #prints graph in console
        print(self.vertices)
        print(self.graph)
        print(self.indegrees)
        print(self.outdegrees)

    def visualize(self): #creates a graph in digital format 
        dot = Digraph(comment = "De Bruijn Graph")

        for vertex in self.vertices:
            dot.node(vertex)

        for vertex in self.vertices:
            for edge in self.graph.get(vertex, []):
                dot.edge(vertex, edge[1])

        dot.format = 'PDF' #format for output of the graph, use SVG, PDF, or postsscript for high qaulity
        dot.render('visualization.gv', view=True)

###################################### Testing ################################################
        
dna_sequence = clean_data("data.txt", 1000)
kMers = kMerMaker(dna_sequence, 5)
graph = de_brujin(
graph.visualize()
x = graph.findEulerPath()
print(x == dna_sequence)
print(x)

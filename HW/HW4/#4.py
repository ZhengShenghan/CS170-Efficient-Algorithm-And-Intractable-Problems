from collections import defaultdict
# This class represents a directed graph using adjacency list
# representation
class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary

    # A recursive function to print DFS starting from v
    def DFSUtil(self, v, visited):

        # Mark the current node as visited and print it
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    # Add w to the list of v
    def addEdge(self, v, w):
        self.graph[v].append(w)

    # Returns a mother vertex if exists. Otherwise returns -1
    def findMother(self):

        # visited[] is used for DFS. Initially all are
        # initialized as not visited
        visited = [False] * (self.V)

        # To store last finished vertex (or mother vertex)
        v = 0

        # Do a DFS traversal and find the last finished
        # vertex
        for i in range(self.V):
            if visited[i] == False:
                self.DFSUtil(i, visited)
                v = i

        # If there exist mother vertex (or vertices) in given
        # graph, then v must be one (or one of them)

        # Now check if v is actually a mother vertex (or graph
        # has a mother vertex). We basically check if every vertex
        # is reachable from v or not.

        # Reset all values in visited[] as false and do
        # DFS beginning from v to check if all vertices are
        # reachable from it or not.
        visited = [False] * (self.V)
        self.DFSUtil(v, visited)
        if any(i == False for i in visited):
            return -1
        else:
            return v

class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, data):
        """
        进栈函数
        """
        self.stack.append(data)

    def pop(self):
        """
        出栈函数，
        """
        if self.empty() == 1:
            return self.stack.pop()

    def gettop(self):
        """
        取栈顶
        """
        return self.stack[-1]
    def empty(self):
        if self.stack == []:
            return 0
        return 1

def DFS(grap : dict, start : tuple, end : tuple):#check whether they are connceted
    visited = set()
    stack = Stack()
    stack.push(start)
    visited.add(start)
    while stack.empty() == 1:
        for x in grap[stack.gettop()]:
            if x not in visited:
                visited.add(x)
                if end in visited:
                    return 1
                stack.push(x)
            stack.pop()
    return 0
    #return visited
def dfs_1(visited, graph, start,end):
    if start not in visited:
        #print (node)
        visited.add(start)
        # traversal[start[0]][start[1]] = 1
        for neighbour in graph[(start[0],start[1])]:
            dfs_1(visited, graph, neighbour,end)
def strongly_connected_components_path(vertices, edges):
    identified = set()
    stack = []
    index = {}
    boundaries = []

    def dfs(v):
        index[v] = len(stack)
        stack.append(v)
        boundaries.append(index[v])

        for w in edges[v]:
            if w not in index:
                # For Python >= 3.3, replace with "yield from dfs(w)"
                for scc in dfs(w):
                    yield scc
            elif w not in identified:
                while index[w] < boundaries[-1]:
                    boundaries.pop()

        if boundaries[-1] == index[v]:
            boundaries.pop()
            scc = set(stack[index[v]:])
            del stack[index[v]:]
            identified.update(scc)
            yield scc

    for v in vertices:
        if v not in index:
            # For Python >= 3.3, replace with "yield from dfs(v)"
            for scc in dfs(v):
                yield scc



if __name__ == '__main__':
    num = int(input())
    index = 0
    index_row = 0
    index_col = 0
    while index < num:
        index_row = 0
        ig_num , port_num = map(int, input().split())
        input_matrix = [[0 for i in range(port_num)]for j in range(ig_num)]
        #adj_matrix = [[[0 for i_1 in range(2)] for j in range(num*num)]for i in range (num*num)]#size num*num with each pair as
        graph = dict()
        vertices = []
        for i in range(ig_num):
            for j in range(ig_num):
                vertices.append((i,j))
        #entry
        i = 0
        j = 0
        while index_row < ig_num:
            input_matrix[index_row] = list(map(int, input().split()))
            index_row+=1
        for i in range(ig_num):
            for j in range(ig_num):
                graph[(i,j)] = []
        for i in range(ig_num):# we only do half matrix because it's symmetric
            for j in range(i+1):# i is column, j is row
                for k in range(port_num):
                    if i == j:
                        graph[(j,i)].append((input_matrix[j][k]-1,input_matrix[i][k]-1))
                    else:
                        graph[(j, i)].append((input_matrix[j][k] - 1, input_matrix[i][k] - 1))
                        graph[(i,j)].append((input_matrix[i][k]-1,input_matrix[j][k]-1))
        #now we get the graph
        # for i in range(ig_num):
        #     for j in range(ig_num):
        #         adj_matrix[i][j] = list()
        #         adj_matrix[j][i] = adj_matrix[i][j]



        # form a SCC graph
        scc_list = list(strongly_connected_components_path(vertices, graph))
        for i in range(len(scc_list)):
            scc_list[i] = list(scc_list[i])
        scc_vertices = [i for i in range(len(scc_list))]
        scc_edges = dict()
        # store a mother vertex
        g = Graph(len(scc_list))
        for i in range(len(scc_list)):
            for j in range(len(scc_list)):
                if i!=j:
                    visited = set()
                    dfs_1(visited, graph, scc_list[i][0], scc_list[j][0])# there is path from i to j but to find mother vertex,
                        #we need to reverse it
                        # scc_edges[j] = []
                        # scc_edges[j].append(i)
                    if scc_list[j][0] in list(visited):
                        g.addEdge(j,i)
        result = g.findMother()
        if result == -1:
            print('NO')
        else:
            mother_SCC = scc_list[result]
            for i in range(ig_num):
                if (i,i) in mother_SCC:
                    print('YES')
                    break
        index+=1
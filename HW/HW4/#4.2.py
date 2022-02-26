from collections import defaultdict
import sys
sys.setrecursionlimit(2147483647)
# This class represents a directed graph using adjacency list
# representation
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


def dfs(visited, graph, node,traversal):
    if traversal[node[0]][node[1]] == 1:
        return
    if node not in visited:
        #print (node)
        visited.add(node)
        traversal[node[0]][node[1]] = 1
        for neighbour in graph[(node[0],node[1])]:
            dfs(visited, graph, neighbour,traversal)


if __name__ == '__main__':
    num = int(input())
    index = 0
    index_row = 0
    index_col = 0
    while index < num:
        det = 0
        count = 0
        index_row = 0
        ig_num , port_num = map(int, input().split())
        input_matrix = [[0 for i in range(port_num)]for j in range(ig_num)]
        traversal_matrix = [[0 for i in range(ig_num)]for j in range(ig_num)]
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
                        graph[(input_matrix[j][k]-1,input_matrix[i][k]-1)].append((j,i))
                    else:
                        graph[(input_matrix[j][k] - 1, input_matrix[i][k] - 1)].append((j,i))
                        graph[(input_matrix[i][k]-1,input_matrix[j][k]-1)].append((i,j))
        for i in range(ig_num):
            visited = set()
            # stack = Stack()
            dfs(visited, graph, (i,i),traversal_matrix)
            #DFS_1(graph,(i,i),traversal_matrix,stack,visited)
        for i in range(ig_num):
            if det == 1:
                break
            for j in range(ig_num):
                if traversal_matrix[i][j] == 0:
                    det = 1
                    break
        if det == 1:
        #if count == ig_num*ig_num:
            print('NO')
        else:
            print('YES')
        index+=1
import sys, threading
sys.setrecursionlimit(800000)
threading.stack_size(67108864)
def main():
    def convertSCC(fileName):
        with open(fileName, 'r') as file:
            lines = file.readlines()
        data = []
        for line in lines:
            i,j = map(int, line.split())
            data.append([i,j])
        return data

    def listNode(graph, start):
        listNode = [start]
        listPointer = {}
        for edge in graph:
            if edge[0] not in listNode:
                listNode.append(edge[0])
                
            if edge[1] not in listNode:
                listNode.append(edge[1])

            if edge[0] in listPointer:
                listPointer[edge[0]].append(edge[1]) 
            else:
                listPointer[edge[0]]= [edge[1]]

        return listNode, listPointer

    def topologicalSort(graph, start):
        nodes, outgoing = listNode(graph, start)
        explored = set()
        order = []

        def dfs (graph, start):
            explored.add(start)
            if start in outgoing:
                for frontier in outgoing[start]:
                    if frontier not in explored:
                        dfs(graph, frontier)
            if start not in order:
                order.append(start)
        
        for vertex in nodes:
            if vertex not in explored:
                dfs(graph, vertex)           
        return order

    def kosaraju(fileName,start):
        graph= convertSCC(fileName)
        graphRev = []
        for edge in graph:
            graphRev.append([edge[1], edge[0]])
        nodes, outgoing = listNode(graph, start)
        rev = topologicalSort(graphRev,start)

        explored = []
        numSCC = 0
        result = [0]
        def dfsSCC (graph, start):
            explored.append(start)
            
            if start in outgoing:
                for vertex in outgoing[start]:
                    if vertex not in explored:
                        dfsSCC(graph, vertex)

        for i in range(len(rev) - 1, -1, -1):
            vertex = rev[i]
            oldSize = len(explored)
            if vertex not in explored:
                numSCC += 1 
                dfsSCC(graph, vertex)
                newSize = len(explored) -oldSize
                result.append(newSize)
        result.sort()
        return result      


    print(kosaraju('problem_set/course2/scc.txt', 1))

thread = threading.Thread(target=main)
thread.start()


#434821, 968, 459, 313, 211
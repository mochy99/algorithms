graphA = [
    ["s","a"],
    ["s","b"],
    ["a","c"],
    ["b","c"],
]
graphB = [
    ["A", "B"],
    ["A", "C"],
    ["B", "D"],
    ["C", "D"],
    ["C", "E"],
    ["D", "E"],
    ["E", "F"],
    ["E", "G"],
    ["F", "G"],
    ["G", "H"],
]
graphC = [
    ["A", "B"],
    ["B", "D"],
    ["B", "C"],
    
    ["C", "A"],
    ["C", "L"],
    ["C", "N"],
    ["D", "E"],
    ["D", "F"],
    ["E", "G"],
    ["F", "E"],
    ["G", "F"],
    ["K", "G"],
    ["K","M"],
    ["L","F"],
    ["L", "K"],
    ["L", "M"],
    ["M", "N"],
    ["N", "L"]
]
graphD = [
    [1,7],
    [7,4],
    [7,9],
    [4,1],
    [6,8],
    [9,6],
    [6,3],
    [3,9],
    [5,8],
    [2,5],
    [8,2]
]

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

def kosaraju(graph,start):
    graphRev = []
    for edge in graph:
        graphRev.append([edge[1], edge[0]])
    nodes, outgoing = listNode(graph, start)
    rev = topologicalSort(graphRev,start)
    print(rev)
    explored = []
    numSCC = 0
    def dfsSCC (graph, start):
        explored.append(start)
        
        if start in outgoing:
            for vertex in outgoing[start]:
                if vertex not in explored:
                    dfsSCC(graph, vertex)

    for i in range(len(rev) - 1, -1, -1):
        vertex = rev[i]
        if vertex not in explored:
            numSCC += 1
            dfsSCC(graph, vertex)
            print(explored)
    return numSCC      

print(kosaraju(graphD, 1))
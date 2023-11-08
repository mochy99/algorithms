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
    order = {}
    curLabel = len(nodes)

    def dfs (graph, start):
        nonlocal curLabel
        explored.add(start)
        if start in outgoing:
            for frontier in outgoing[start]:
                if frontier not in explored:
                    dfs(graph, frontier)
        if start not in order:
            order[start] = curLabel
            curLabel = curLabel - 1
    
    for vertex in nodes:
        if vertex not in explored:
            dfs(graph, vertex)           
    return order

    


print(topologicalSort(graphB, "B"))
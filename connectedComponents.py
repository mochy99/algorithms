graphA = [
    ["s","a"],
    ["s","b"],
    ["a","c"],
    ["b","c"],
    ["c","e"],
    ["c","d"],
    ["d","e"]
]
graphB = [
    ["A", "B"],
    ["B", "D"],
    ["C", "E"],
    ["C", "F"],
    ["X", "Y"],  
    ["Y", "Z"],
    ["M", "N"],  
    ["P", "Q"],
]
def connectedComponenets(graph):
    listNode = set()
    setNode = {}
    for edge in graph:
        node1, node2 = edge
        listNode.add(node1)
        listNode.add(node2)
        if node1 in setNode:
            setNode[node1].append(node2)
        else:
            setNode[node1] = [node2]
        if node2 in setNode:
            setNode[node2].append(node1)
        else:
            setNode[node2] = [node1]
    visited = set()
    count = 0

    def bfs(node):
        waiting = [node]
        while waiting:
            cur_node =waiting.pop(0)
            if cur_node not in visited:
                vertices = setNode[cur_node] if cur_node in setNode else vertices
                for frontier in vertices:
                    waiting.append(frontier)
                visited.add(cur_node)


    for node in listNode:
        if node not in visited:
            bfs(node)
            count += 1

    return count
    

print(connectedComponenets(graphB))       
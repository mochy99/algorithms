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
    ["C", "A"],
    ["B", "D"],
    ["C", "E"],
    ["D", "E"],
    ["D", "G"],
    ["E", "F"],
    ["F", "G"],
    ["G", "H"],
    ["H", "I"]
]

def bfs(graph, start):
    queue = [start]
    explored = set()
    layer ={start : 0}
    count = 0
    while queue:
        currentVertex = queue.pop(0)
        currentLayer = layer.get(currentVertex)
        
        count = currentLayer
        if currentVertex not in explored:
            explored.add(currentVertex)
            
            for edge in graph:
                if currentVertex in edge:
                    next = edge[0] if edge[1] == currentVertex else edge[1]
                    if next not in explored:
                        queue.append(next)
                        if next in layer:
                            layer[next] = min(currentLayer + 1, layer[next])
                        else:
                            layer[next] = currentLayer + 1    
    return count

print(bfs(graphA, "s"))

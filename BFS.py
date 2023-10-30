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
    currentVertex = queue.pop(0)
    layer ={start : 0}
    count = 0
    while queue:
        if queue[0] not in explored:
            currentLayer = layer.get(queue[0])

            for i in range(len(graph)):
                if queue[0] in graph[i]:
                    next = graph[i][0] if graph[i][1] == queue[0] else graph[i][1]
                    if next not in explored:
                        queue.append(next)
                        if next in layer:
                            layer[next] = min(currentLayer + 1, layer[next])
                        else:
                            layer[next] = currentLayer + 1
                            count = currentLayer + 1 
            explored.append(queue[0])
            queue.pop(0)   
        else:
            queue.pop(0)
    return count

print(bfs(graphB, "A"))

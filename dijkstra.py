graphA = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 1), ('D', 4)],
    'C': [('D', 3)],
    'D': [('E', 5)],
}
#input: graph includes the path from start vertex to end vertex
#output: 
def dijkstra(graph, start, end):
    visited = [start]
    track = {start: 0}
    while end != visited[-1]:
        minLen = 0
        next_node = None
        for vertex in visited:
            listEdges = graph[vertex]
            for neighbor, weight in listEdges:
                if neighbor not in visited:
                    curLen = track[vertex] + weight
                    if (curLen < minLen  and neighbor not in visited) or minLen == 0:
                        minLen = curLen
                        next_node = neighbor        

        visited.append(next_node)
        track[next_node] = minLen

    return track[end]


print(dijkstra(graphA, "A", "D"))


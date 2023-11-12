graphA = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 1), ('D', 4)],
    'C': [('D', 3)],
    'D': [('E', 5)],
}
graphB = {'A': [('B', 2), ('H', 2)],
 'B': [('A', 1), ('C', 1)],
 'C': [('B', 1), ('D', 1)],
 'D': [('C', 1), ('E', 1)],
 'E': [('D', 1), ('F', 1)],
 'F': [('E', 1), ('G', 1)],
 'G': [('F', 1), ('H', 1)],
 'H': [('G', 1), ('A', 2)]}
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

def test(order, input, start, end, output):
    expect_output = dijkstra(input, start, end)
    if expect_output == output:
        return "Test " + str(order) + " passed"
    else:
        return "Test " + str(order) + " failed"
print(test(1, graphA, "A", "B", 2))
print(test(2, graphB, "A", "H", 3))


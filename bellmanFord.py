from convertArray import convertDirectedGraph
import sys
def bellmanFord(fileName):
    setVetices, setEdges = convertDirectedGraph(fileName)
    budget = len(setVetices)
    result = sys.maxsize
    for start in setVetices:
        init, prev = [None], set()
        # Initialize 
        prev.add(start)
        for vertex in setVetices:
            if vertex == start:
                init.append(0) 
            else:
                init.append(sys.maxsize) 
        # Main loop
        for i in range(budget):
            new_nodes = set()
            for tail in prev:
                if tail in setEdges:
                    for head, weight in setEdges[tail]:
                        value = min(init[head], init[tail] + weight)
                        init[head] = value
                        result = min(result, value)
                        new_nodes.add(head)
            prev.update(new_nodes)
        # Detect a negative cycle
        for tail in prev:
            if tail in setEdges:
                for head, weight in setEdges[tail]:
                    value = min(init[head], init[tail] + weight)
                    if init[head] != value:
                        return "A negative cycle"
                        
    return result


    

print(bellmanFord("problem_set/course4/g1week1.txt"))
print(bellmanFord("problem_set/course4/g2week1.txt"))
print(bellmanFord("problem_set/course4/g3week1.txt"))
print(bellmanFord("problem_set/course4/g4week1.txt"))

from convertArray import convertSetEdges

def bellmanFord(fileName):
    setVetices, setEdges, setWeight = convertSetEdges(fileName)
    print(setVetices)

print(bellmanFord("problem_set/course4/g1week1.txt"))
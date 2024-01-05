def convertArray(fileName):
    # Read data from the file
    with open(fileName, 'r') as file:
        lines = file.readlines()
    
    # Convert data to a list of integers
    data = [int(line.strip()) for line in lines]

    return data


def convertSCC(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()
    data = []
    for line in lines:
        i,j = map(int, line.split())
        data.append([i,j])
    return data

def convertDijkstra(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()
    data = {}
    for line in lines:
        parts = line.split('\t')
        key = int(parts[0])
        values = [tuple(map(int, pair.split(','))) for pair in parts[1:]]
        data[key] = values
    return data

def convertStrArray(fileName):
    # Read the content of the file
    with open(fileName, 'r') as file:
        lines = file.readlines()
    data_list = []
    leader, rank = [], []
    dicEdge = {}
    # Convert data to a list of floats
    for i in range(len(lines)):
        line = lines[i]
        leader.append(i)
        rank.append(0)
        if i > 0:
            value = str(line.strip().replace(" ",""))
            data_list.append(value)
            if dicEdge.get(value):
                dicEdge[value].append(i)
            else:
                dicEdge[value] = [i]
    return data_list, dicEdge, leader, rank

def convertSchedule(fileName):
    # Read data from the file
    with open(fileName, 'r') as file:
        lines = file.readlines()

    job_details = []

    # Extract details for each job
    for i in range(1, len(lines)):
        line = lines[i]
        if line:
            weight, length = map(int, line.split())
            job_details.append((weight, length))
    
    # Create the dictionary
    output_dict = {}
    output_dict["numofjob"] = lines[0].split()
    output_dict["details"] = job_details

    return output_dict
def convertSetEdges(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()
    setVetices, setEdges, setWeight = set(),[], []
    for line in lines:
        node, aNode, weight = map(int, line.split())
        setEdges.append((node, aNode, weight))
        setWeight.append(weight)
        setVetices.add(node)
        setVetices.add(aNode)
    return setVetices, setEdges, setWeight

def convertDirectedGraph(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()
    setVetices, setEdges = set(),{}
    for line in lines:
        node, aNode, weight = map(int, line.split())
        if node in setEdges :
            setEdges[node].append((aNode, weight))
        else:
            setEdges[node] = [(aNode, weight)]
        setVetices.add(node)
        setVetices.add(aNode)
    return setVetices, setEdges

def convertUndirectedGraph(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()
    setVertices = set()
    setEdges = {}
    for line in lines:
        fPoint, sPoint, weight = map(int, line.split())
        if fPoint not in setVertices:
            setVertices.add(fPoint)
            setEdges[fPoint] = [(sPoint, weight)]
        else:
            setEdges.get(fPoint).append((sPoint,weight))
        if sPoint not in setVertices:
            setVertices.add(sPoint)
            setEdges[sPoint] = [(fPoint, weight)]
        else:
            setEdges.get(sPoint).append((fPoint,weight))
    return setVertices, setEdges

# .txt -> ListNodeTree, P(a),  HeapP(a)
from heap import pairHeapify 
def convertHuffMan(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()
    Tree, HeapPa, Deep = set(), [], {} #set, array, dic
    for i in range(1,len(lines)):
        Tree.add(i)
        prob = int(lines[i].strip())
        
        Deep[i] = (0,0)
        HeapPa.append((i,prob))
        pairHeapify(HeapPa)
    return Tree, HeapPa, Deep

def convertKnapSack(fileName):
    with open(fileName, "r") as file:
        lines = file.readlines()
    data = []
    for i in range(1, len(lines)):
        value, size = map(int, lines[i].split())
        data.append((value,size))
    return data


def convertTsp(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()

    data, setVertices = {}, []
    for i in range(len(lines)):
        if i > 0:
            x, y = map(float, lines[i].split())
            data[i] = (x,y)
            setVertices.append(i)

    return setVertices, data

def convertHeuristicTsp(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()

    data, setVertices = {}, []
    for i in range(len(lines)):
        if i > 0:
            index, x, y = map(float, lines[i].split())
            data[i] = (x,y)
            setVertices.append(int(index))

    return setVertices, data

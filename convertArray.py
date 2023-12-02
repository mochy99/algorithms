def convertArray(fileName):
    # Read data from the file
    with open(fileName, 'r') as file:
        lines = file.readlines()

    # Convert data to a list of floats
    data_list = [float(line.strip()) for line in lines]

    return data_list

def convertIntArray(fileName):
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
        value = int(line.strip().replace(" ",""))
        data_list.append(value)
        if dicEdge.get(value):
            dicEdge[value].add(i)
        else:
            dicEdge[value] = {i}
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
        setEdges.append(line.split())
        node, aNode, weight = map(int, line.split())
        setWeight.append(weight)
        setVetices.add(node)
        setVetices.add(aNode)
    return setVetices, setEdges, setWeight

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
    Tree, Pa, HeapPa = set(), {}, [] #set, dic ,array
    for i in range(1,len(lines)):
        Tree.add(i)
        prob = int(lines[i].strip())
        Pa[i] = prob
        HeapPa.append((i,prob))
        pairHeapify(HeapPa)
    return Tree, Pa, HeapPa
print(convertHuffMan('testCase/huffman1.txt'))



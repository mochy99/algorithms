def convertArray(fileName):
    # Specify the path to your text file
    file_path = fileName

    # Read data from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Convert data to a list of floats
    data_list = [float(line.strip()) for line in lines]

    return data_list

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



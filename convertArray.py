def convertArray(fileName):
    # Specify the path to your text file
    file_path = fileName

    # Read data from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Convert data to a list of floats
    data_list = [float(line.strip()) for line in lines]

    return data_list

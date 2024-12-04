def read_file(file_path):
    array_2d = []

    with open(file_path, 'r') as file:
        [array_2d.append(list(line.strip())) for line in file]

    return array_2d
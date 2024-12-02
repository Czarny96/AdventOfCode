def read_file(file_path):
    with open(file_path, 'r') as file:
        data = [list(map(int, line.split())) for line in file]

    return data
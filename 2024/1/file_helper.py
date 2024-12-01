def read_file(file_path):
    left_list = []
    right_list = []

    with open(file_path, 'r') as file:
        for line in file:
            left_column, right_column = map(int, line.split())
            left_list.append(left_column)
            right_list.append(right_column)
    
    sorted_left_list = sorted(left_list)
    right_list.sort()

    return sorted_left_list, right_list
from file_helper import read_file

xmas = ['X', 'M', 'A', 'S']

search_options = [
(0, -1), (0, 1),
(1, -1), (1, 1),
(-1, 0), (1, 0), 
(-1, -1), (-1, 1)
]


def get_xmas(array, rowIdx, colIdx, row_direction, col_direction):
    print('')
    width = len(array)
    height = len(array[rowIdx]);

    for i in range(len(xmas)):
        row = rowIdx + (row_direction * i)
        col = colIdx + (col_direction * i)

        print('')
        print('i', i)
        print("Row", row)
        print("Col", col)
        print("Width", width)
        print("Height", height)

        if (0 > row or row >= width) or (0 > col or col >= height):
            print("Out of range")
            return False

        if array[row][col] != xmas[i]:
            print("Invalid char", array[row][col], xmas[i])
            return False

    return True
    
def xmas_score(file_path):
    array = read_file(file_path)

    score = 0

    i = 0

    for rowIdx in range(len(array)):
        for colIdx in range(len(array[rowIdx])):
            for row_direction, col_direction in search_options:
                if get_xmas(array, rowIdx, colIdx, row_direction, col_direction):
                    score += 1

    return score
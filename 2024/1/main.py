from file_helper import read_file

test_file_data = "Data/inputs_test.txt"
file_data = "Data/inputs.txt"

def calculate_distance(file_path):
    distance = 0
    left_list, right_list = read_file(file_path)

    left_list_len = len(left_list)
    
    for i in range(left_list_len):
        distance = distance + abs(left_list[i] - right_list[i])

    return distance

def calculate_score(file_path):
    score = 0
    left_list, right_list = read_file(file_path)

    for value_to_search in left_list:
        score =  score + (value_to_search * right_list.count(value_to_search))
    
    return score

print("Day 1")

print("Part 1")
print("Test distance: ", calculate_distance(test_file_data))
print("Distance: ", calculate_distance(file_data))

print("Part 2")
print("Test score: ", calculate_score(test_file_data))
print("Score: ", calculate_score(file_data))
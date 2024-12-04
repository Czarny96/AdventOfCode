from part_one import xmas_score

test_file_data = "Data/inputs_test.txt"
file_data = "Data/inputs.txt"

test_xmas_score = xmas_score(test_file_data)
xmas_score = xmas_score(file_data)

print("Day 4")

print("Part 1")
print("Test XMAS:", test_xmas_score)
print("XMAS", xmas_score)
from part_one import is_safe_part_one
from part_two import is_safe_part_two

test_file_data = "Data/inputs_test.txt"
file_data = "Data/inputs.txt"

print("Day 2")

print("Part 1")
print("Test validation:",  is_safe_part_one(test_file_data))
print("Validation::", is_safe_part_one(file_data))

print("Part 2")
print("Test dampener validation:",  is_safe_part_two(test_file_data))
print("Dampener validation:", is_safe_part_two(file_data))
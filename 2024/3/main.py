from file_helper import read_file;
from part_one import calculate_part_one
from part_two import calculate_part_two 
import re

test_file_data = "Data/inputs_test.txt"
file_data = "Data/inputs.txt"

print("Day 3")

print("Part 1")
print("Test mul:", calculate_part_one(test_file_data))
print("Mul:", calculate_part_one(file_data))

print("Part 2")
print("Test mul:", calculate_part_two(test_file_data))
print("Mul:", calculate_part_two(file_data))
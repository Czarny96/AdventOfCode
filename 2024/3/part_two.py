from file_helper import read_file
import re

mul_regex_pattern = "mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)"
digits_regex_pattern = '[0-9]{1,3}'

def get_muls(file_path):
    matches = []
    lines = read_file(file_path)

    for line in lines:
        match = re.findall(mul_regex_pattern, line)
        matches += match

    return matches

def multiple(muls):
    sum = 0
    process = True

    for mul in muls:

        if mul == "do()":
            process = True
            continue
        elif mul == "don't()":
            process = False
            continue
        
        if process:
            command = re.findall(digits_regex_pattern, mul)
            digits = list(map(int, command))
            sum += (digits[0] * digits[1])

    return sum


def calculate_part_two(file_path):
    get_data_to_multiple = get_muls(file_path)
    return multiple(get_data_to_multiple)
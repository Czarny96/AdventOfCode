from file_helper import read_file

def is_safe_part_one(file_path):
    safe_count = 0
    reports = read_file(file_path)

    for report in reports:
        delta = [report[i] - report[i - 1] for i in range(1, len(report))]
        delta_decreasing = all(-3 <= diff <= -1 for diff in delta)
        delta_increasing = all(1 <= diff <= 3 for diff in delta)

        if (delta_increasing or delta_decreasing):
            safe_count += 1
        
    return safe_count
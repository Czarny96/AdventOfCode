from file_helper import read_file

def is_safe(report):
    delta = [report[i] - report[i - 1] for i in range(1, len(report))]

    delta_decreasing = all(-3 <= diff <= -1 for diff in delta)
    delta_increasing = all(1 <= diff <= 3 for diff in delta)

    return delta_increasing or delta_decreasing

def is_safe_part_two(file_path):
    safe_count = 0
    reports = read_file(file_path)

    for report in reports:
        if (is_safe(report)):
            safe_count += 1
            continue

        for i in range(len(report)):
            remove_level = report[:i] + report[i+1:]

            if(is_safe(remove_level)):
                safe_count += 1
                break


    return safe_count
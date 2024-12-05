def format_lines_as_numbers(lines):
    # group lines into lists
    number_lines = [line.strip() for line in lines if line.strip()]
    return [[int(num) for num in line.split()] for line in number_lines]

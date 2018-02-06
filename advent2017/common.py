from pathlib import Path
import re



def parse_int(line):
    return tuple(map(int, re.findall(r'-?\d+', line)))

def puzzle_input(day):
    input_file_name = f"day{day}_input.txt"
    day_input = Path(__file__).parent / 'puzzle_input' / input_file_name

    return day_input.read_text().splitlines()

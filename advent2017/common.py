from pathlib import Path

def puzzle_input(day):
    input_file_name = f"day{day}_input.txt"
    day_input = Path(__file__).parent / 'puzzle_input' / input_file_name
    # assert day_input.exists(), f"Puzzle input {day_input} does not exist."

    return day_input.read_text().splitlines()

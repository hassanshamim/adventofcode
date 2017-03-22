"""
General Utility Functions for advent.
"""
import sys
import pathlib


def find_data_file():
    """
    Finds associated input data based on filename
    """
    currentfile = sys.argv[0]
    currentfile = pathlib.Path(currentfile).absolute()
    fname = currentfile.name.rstrip('.py')
    fname += '_input.txt'

    root_dir = currentfile.parent
    input_file = root_dir / 'puzzle_input' / fname

    if input_file.exists():
        return str(input_file)
    else:
        raise FileNotFoundError('Could not locate input file {}'.format(input_file))

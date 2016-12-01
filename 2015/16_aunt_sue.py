from operator import gt, lt, eq

def fetch_data():
    """generator for input data"""
    with open('./day_16.input.txt', 'r') as f:
        for line in f.readlines():
            yield line.strip()


def make_sue(line):
    sue_id, properties = line.split(': ', maxsplit=1)
    sue = {'id': int(sue_id[4:])}
    for prop in properties.split(', '):
        item, val = prop.split(': ')
        sue[item] = int(val)
    return sue
    
def compare(sue, target):
    """Comparison for part two"""
    comparison = {'cats': gt, 'trees': gt, 'pomeranians': lt, 'goldfish': lt}
    return all(comparison.get(key, eq)(val, target[key]) for key, val in sue.items())
    
    

def main1():
    sue_target = {'akitas': 0, 'cars': 2, 'cats': 7, 'children': 3, 'goldfish': 5,
                  'perfumes': 1, 'pomeranians': 3, 'samoyeds': 2, 'trees': 3, 'vizslas': 0}

    for sue in map(make_sue, fetch_data()):
        sue_id = sue.pop('id')
        for key, val in sue.items():
            if not sue_target[key] == val:
                break  # continue to next sue
        else:
            # found our sue!
            print('Sue {}'.format(sue_id))
            break


def main2():
    sue_target = {'akitas': 0, 'cars': 2, 'cats': 7, 'children': 3, 'goldfish': 5,
                  'perfumes': 1, 'pomeranians': 3, 'samoyeds': 2, 'trees': 3, 'vizslas': 0}

    for sue in map(make_sue, fetch_data()):
        sue_id = sue.pop('id')

        if compare(sue, sue_target):
            print('Sue {}'.format(sue_id))
if __name__ == '__main__':
    main1()
    main2()
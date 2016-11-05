def wrapping_for_present(dimms):
    x, y, z = dimms
    areas = (x*y, x*z, y*z)
    box = sum(2*area for area in areas)
    extra = min(areas)
    return box + extra

def ribbon_for_present(*dimms):
    x, y, z = sorted(*dimms)
    bow = x*y*z
    face = 2*x + 2*y
    return bow+face

with open ('./day_2.input', 'r') as f:
    total_required = sum(wrapping_for_present([int(char) for char in text.split('x')]) for text in f.readlines())
    print('total: wrapping', total_required)

with open ('./day_2.input', 'r') as f:
    total_required = sum(ribbon_for_present(int(char) for char in text.split('x')) for text in f.readlines())
    print('total: ribbon', total_required)


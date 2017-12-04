from ..day17 import current_location, shortest_path, longest_path


def test_current_location():
    assert current_location('DU') == (0, 0)
    assert current_location('DRLU') == (0, 0)
    assert current_location('RRR') == (3, 0)


def test_shortest_path_examples():
    assert shortest_path('ihgpwlah') == 'DDRRRD'
    assert shortest_path('kglvqrro') == 'DDUDRLRRUDRD'
    assert shortest_path('ulqzkmiv') == 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'


def test_longest_path_examples():
    assert longest_path('ihgpwlah') == 370
    # assert longest_path('kglvqrro') == 492
    # assert longest_path('ulqzkmiv') == 830

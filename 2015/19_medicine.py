# -*- coding: utf-8 -*-

from collections import defaultdict


def split_by_element(molecule):
    """
    >>> type(split_by_element('NaCl'))
    <class 'generator'>

    >>> [el for el in split_by_element('NaCl')]
    ['Na', 'Cl']
    """
    mol = iter(molecule)
    el = next(mol)
    for char in mol:
        if char.isupper():
            yield el
            el = char
        else:
            el += char
    else:
        yield el


def get_raw_input():
    with open('day_19.input.txt') as f:
        *data, empty, molecule = [line.strip() for line in f.readlines()]
        return data, molecule


def get_input():
    data, molecule = get_raw_input()
    replacements = defaultdict(list)
    for rep in data:
        inp, out = rep.split(' => ')
        replacements[inp].append(out)

    return replacements, molecule


def generate_new_molecules(molecule, substitutions):
    """
    >>> m = 'HOH'
    >>> reps = {'H': ['HO', 'OH'], 'O': ['HH']}
    >>> result = generate_new_molecules(m, reps)
    >>> type(result)
    <class 'set'>
    >>> sorted(result)
    ['HHHH', 'HOHO', 'HOOH', 'OHOH']

    """

    new_molecules = set()
    decomposed = list(split_by_element(molecule))
    for i, element in enumerate(decomposed):
        current_replaced = (decomposed[:i] + [replacement] + decomposed[i+1:] for replacement in substitutions[element])
        generated_molecules = {''.join(elems) for elems in current_replaced}
        new_molecules.update(generated_molecules)

    if molecule in new_molecules:
        new_molecules.remove(molecule)

    return new_molecules


def main1():
    replacements, mol = get_input()
    new_mols = generate_new_molecules(mol, replacements)

    print('total new molecules:', len(new_mols))


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    main1()

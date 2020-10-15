import numpy as np


def get_data():
    """
    :return: m, n, partitions

    m = numărul de valori posibile ale etichetei / atributului de ieşire
    n = numărul de valori ale atributului (notat mai jos cu A) în raport cu care se face partiţionarea mulţimii de
        instanţe asociate nodului-rădăcină al compasului de decizie
    partitions = partiţiile (de fapt, count-urile) corespunzătoare nodurilor descendente. Pornind de la aceste partiţii,
        programul va calcula partiţia asociată nodul-rădăcină al compasului de decizie.
    """
    fd = open("input.txt")
    input_data = fd.read()
    m, n = map(int, input_data.split()[:2])
    partitions = np.array(list(map(lambda s: list(map(int, s.replace("[", "").replace("]", "").split(","))),
                          input_data.split()[2:])))
    return (m, n), partitions


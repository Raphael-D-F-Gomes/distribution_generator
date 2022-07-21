import numpy as np
import itertools as it

def distribution_generator(possibilities):
    """
    args:
        possibilities: (list of possibilities)

    returns:
        (numpy.array): array with the possible scenarios
    """
    n_objects = len(possibilities)
    n_pos_list = [len(possibilities[i]) for i in range(n_objects)]
    n_possibilities = np.prod(n_pos_list)
    scenarios = [[0] * n_possibilities] * n_objects

    for i in range(n_objects):
        col = [[possibilities[i][j]] * int(n_possibilities / np.prod(n_pos_list[0:i + 1]))
               for j in range(n_pos_list[i])]
        col = list(it.chain.from_iterable(col))
        col = [col * int(n_possibilities / len(col))]
        scenarios[i] = col[0]

    return np.transpose(scenarios)


if __name__ == '__main__':

    colors = ['red', 'green', 'yellow', 'blue']
    print(distribution_generator([colors, colors]))

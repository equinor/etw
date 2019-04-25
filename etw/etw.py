import itertools
import numpy as np


def etw(ns, nt, cost=None, max_shift=None):
    """etw
    Parameters
    ----------
    ns : int
        Length of first series
    nt : int
        Length of second series
    cost : function(i: int, k: int) -> float
        Function returing the distance between sample i of s and sample k of t
    max_shift : int, optional
        The maximal computed shift, TODO: explain why it's needed.
        Defaults to min(ns, nt) // 2

    Returns
    -------
    (Path, AccumulatedCost, Cost, Weights)
    """

    if not cost:
        raise ValueError('dist function must be specified')

    if not max_shift:
        max_shift = min(ns, nt) // 2

    L = [[np.inf for _ in range(nt)] for _ in range(ns)]
    C = [[np.inf for _ in range(nt)] for _ in range(ns)]
    P = [[(None, None) for _ in range(nt)] for _ in range(ns)]
    T = [[np.inf for _ in range(nt)] for _ in range(ns)]

    for i in range(0, ns):
        L[i][0] = 1
        C[i][0] = cost(i, 0) if i < max_shift else np.inf
        T[i][0] = C[i][0]
        P[i][0] = (i, 0)
    for k in range(1, nt):
        L[0][k] = 1
        C[0][k] = cost(0, k) if k < max_shift else np.inf
        T[0][k] = C[0][k]
        P[0][k] = (0, k)

    for i, k in itertools.product(range(1, ns), range(1, nt)):
        C[i][k] = cost(i, k)

    for i, k in itertools.product(range(1, ns), range(1, nt)):
        prev = (i - 1, k - 1), (i - 1, k), (i, k - 1)
        i0, k0 = min(prev, key=lambda idx: T[idx[0]][idx[1]])
        T[i][k] = T[i0][k0] + cost(i, k)
        L[i][k] = L[i0][k0] + 1
        P[i][k] = (i0, k0)

    def weighted_table(idx):
        i, k = idx
        i, k = i % ns, k % nt

        # Idealized:
        # w = max(max(i + 1, k + 1) / min(i + 1, k + 1), 1.0)

        # Actual:
        w = max(max(i + 1, k + 1) / L[i][k], 1.0)

        return T[i][k] * w

    min_b = min(((i, -1) for i in range(max_shift, ns)), key=weighted_table)
    min_a = min(((-1, k) for k in range(max_shift, nt)), key=weighted_table)
    i, k = min(min_a, min_b, key=weighted_table)
    i, k = i % ns, k % nt

    p, q = [i], [k]

    while i > 0 and k > 0:
        i, k = P[i][k]
        p.append(i)
        q.append(k)

    p.reverse()
    q.reverse()

    return (p, q), T, C, L

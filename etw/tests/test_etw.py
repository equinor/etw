from .. import etw


# TODO:
# def test_ns_ne_nt():
#     s = [3, 2, 1, 2, 3,      4,       5,       6, 7]
#     t =       [1, 2, 3, 4, 4.2, 4, 4, 5, 5, 5]
#     cost = lambda i, k: 1.0 + abs(s[i] - t[k])


def test_ns_eq_nt():
    s = [3, 2, 1, 2, 3, 4, 5, 6, 6, 7]
    t = [1, 2, 3, 4, 4.2, 4, 4, 5, 5, 5]

    ref_path = ([2, 3, 4, 5, 5, 5, 5, 6, 6, 6], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    path, _, _, _ = etw(len(s), len(t),
                        cost=lambda i, k: 1.0 + abs(s[i] - t[k]))

    assert path == ref_path

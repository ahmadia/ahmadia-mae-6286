from examples.traffic_flow import advance_to_T


def test_advance_to_T():
    import numpy as np
    m = 400
    dx = 1.0 / m
    x = np.arange(-dx / 2, 1.0 + dx / 2, dx)

    t = 0
    T = 0.5
    dt = 0.9 * dx

    Q = 0.9 * np.exp(-100 * (x - 0.5) ** 2)

    QQ = advance_to_T(Q, t)
    assert QQ[0] is Q
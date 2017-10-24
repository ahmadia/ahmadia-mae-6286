import numpy as np

m = 400
dx = 1.0/m
x = np.arange(-dx/2, 1.0+dx/2, dx)

t = 0
T = 0.5
dt = 0.9 * dx

Q = 0.9*np.exp(-100*(x-0.5)**2)


def advance_to_T(Q, t):
    Q_new = np.empty(Q.shape)
    QQ = [Q]
    while t < T:
        Q_new[1:-1] = 0.5 * (Q[:-2] + Q[2:]) - \
                      0.5 * dt / dx * (Q[2:] * (1 - Q[2:]) - Q[:-2] * (1 - Q[:-2]))
        Q = Q_new.copy()
        Q[0] = Q[-2]
        Q[-1] = Q[1]
        t = t + dt
        QQ.append(Q)
    return QQ

if __name__ == '__main__':
    advance_to_T()

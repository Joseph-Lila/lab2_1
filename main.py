import numpy as np
from sympy import *
import matplotlib.pyplot as plt


def get_k_set(fi, si):
    k1, k2, k3 = symbols('k1 k2 k3')
    if len(fi) == len(si):
        eqs = [Eq(k1 * si[i] * cos(fi[i]) + k2 * sin(fi[i]) - k3, si[i] ** 2) for i in range(len(fi))]
        expr = nonlinsolve(eqs, [k1, k2, k3])
        return list(expr)
    return [[None, None, None]]


def get_a_set(k1, k2, k3):
    a1 = k1 / 2
    a3 = k2 / 2 / a1
    a2 = sqrt(a1 ** 2 + a3 ** 2 - k3)
    return a1, a2, a3


def main():
    fi = [45 * np.pi / 180, 22.5 * np.pi / 180, 67.5 * np.pi / 180]
    s = [1.2, 1.4, .95]
    a4 = .1
    b = 100 * np.pi / 180
    k1, k2, k3 = get_k_set(fi, s)[0]
    if k1 is None or k2 is None or k3 is None:
        return
    a1, a2, a3 = get_a_set(k1, k2, k3)
    exist = a1 < a2 - a3
    if exist:
        print('Условие существования выполняется')
        h = 1 if a3 >= 0 else -1
        fi = np.linspace(0, 2 * np.pi, 100)
        sh = [a1 * cos(fi[i]) + sqrt(a2 ** 2 - (a3 * h - a1 * sin(fi[i])) ** 2) for i in range(len(fi))]
        for i in range(len(fi)):
            if 1.18 < sh[i] < 1.22:
                print(f'sh = {sh[i]}; fi = {fi[i]}')
        plt.plot(fi, sh)
        plt.show()
    else:
        print('Условие существования не выполняется')


if __name__ == "__main__":
    main()

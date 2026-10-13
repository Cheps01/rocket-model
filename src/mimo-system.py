import numpy as np
from scipy import signal

class MIMO_System:
    def __init__(self, A: list, B: list, C: list, D: list):
        system = signal.StateSpace(A, B, C, D)
    def output(input):
        t = np.linspace(0, 10, 500)
        u = np.ones_like(t)
        return signal.lsim(sys, U=u, T=t)
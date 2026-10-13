import numpy as np
from scipy import signal

class MIMO_System:
    def __init__(self, A: list, B: list, C: list, D: list):
        self.system_ss = signal.StateSpace(A, B, C, D)
    def step_output(self):
        # TODO
        pass
    def impulse_output(self):
        # TODO
        pass
    def tranfer_function(self):
        # TODO
        pass
    def bode(self):
        # TODO
        pass
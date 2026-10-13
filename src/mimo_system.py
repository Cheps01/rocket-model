import numpy as np
from scipy import signal

class MIMO_System:
    def __init__(self, A: list, B: list, C: list, D: list):
        self.state_space = signal.StateSpace(A, B, C, D)
    def output(self, inp: list, start: float = 0.0, end: float = 1.0):
        t = np.linspace(start, end, 1000)
        if len(inp) != self.state_space.inputs:
            raise ValueError(f"Expected {self.state_space.inputs} inputs, got {len(inp)}")
        u = [np.broadcast_to(np.asarray(f(t), dtype=float), t.shape) for f in inp]
        return signal.lsim(self.state_space, U=np.column_stack(u), T=t)
    def tranfer_function(self):
        # TODO
        pass
    def bode(self):
        # TODO
        pass
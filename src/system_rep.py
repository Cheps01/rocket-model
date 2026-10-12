import sympy as sp
import numpy as np

# Zeros filled 2D array utility function
def zeros(height: int, width: int) -> list:
    return [[0 for _ in range(width)] for _ in range(height)]

# Matrix coeficients extraction from states and output equation systems
def get_all_matrixes(state_system: list[sp.Eq], output_system: list[sp.Eq], states: list[sp.Symbol], inputs: list[sp.Symbol], outputs: list[sp.Symbol]):
    # Build A (states x states)
    A = zeros(len(states), len(states))
    for i, eq in enumerate(state_system):
        for j, st in enumerate(states):
            A[i][j] = float(eq.rhs.coeff(st))

    # Build B matrix (states x inputs)
    B = zeros(len(states), len(inputs))
    for i, eq in enumerate(state_system):
        for j, inp in enumerate(inputs):
            B[i][j] = float(eq.rhs.coeff(inp))

    # Build C matrix (outputs x states)
    C = zeros(len(outputs), len(states))
    for i, eq in enumerate(output_system):
        for j, st in enumerate(states):
            C[i][j] = float(eq.rhs.coeff(st))

    # Build D matrix (outputs x inputs)
    D = zeros(len(outputs), len(inputs))
    for i, eq in enumerate(output_system):
        for j, inp in enumerate(inputs):
            D[i][j] = float(eq.rhs.coeff(inp))

    # Return system representation matrixes
    return A, B, C, D
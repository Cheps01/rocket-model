import sympy as sp

def zeros(height: int, width: int) -> list:
    return [[0 for _ in range(width)] for _ in range(height)]

def get_all_matrixes(state_system: list[sp.Eq], output_system: list[sp.Eq], states: list[sp.Symbol], inputs: list[sp.Symbol], outputs: list[sp.Symbol]):
    # Build A (states x states)
    A = zeros(len(states), len(states))
    for i, eq in enumerate(state_system):
        for j, st in enumerate(states):
            A[i][j] = eq.rhs.coeff(st)

    # Build B matrix (states x inputs)
    B = zeros(len(states), len(inputs))
    for i, eq in enumerate(state_system):
        for j, inp in enumerate(inputs):
            B[i][j] = eq.rhs.coeff(inp)

    # Build C matrix (outputs x states)
    C = zeros(len(outputs), len(states))
    for i, eq in enumerate(output_system):
        for j, st in enumerate(states):
            C[i][j] = eq.rhs.coeff(st)

    # Build D matrix (outputs x inputs)
    D = zeros(len(outputs), len(inputs))
    for i, eq in enumerate(output_system):
        for j, inp in enumerate(inputs):
            D[i][j] = eq.rhs.coeff(inp)

    # Return system representation matrixes
    return A, B, C, D

def display_state_equations(A: list, B: list, C: list, D: list, states: list[sp.Symbol], inputs: list[sp.Symbol]):
    print("STATE EQUATIONS")
    print("-" * 60)

    for i in range(len(A)):
        terms = []

        for j in range(len(states)):
            coefficient = A[i][j]
            if coefficient != 0:
                terms.append(f"({coefficient})*{states[j]}")

        for j in range(len(inputs)):
            coefficient = B[i][j]
            if coefficient != 0:
                terms.append(f"({coefficient})*{inputs[j]}")

        rhs = " + ".join(terms).replace("+ (-", "- (")
        print(f"dx{i+1}/dt = {rhs}")

    print("\nOUTPUT EQUATIONS")
    print("-" * 60)

    for i in range(len(C)):
        terms = []

        for j in range(len(states)):
            coefficient = C[i][j]
            if coefficient != 0:
                terms.append(f"({coefficient})*{states[j]}")

        for j in range(len(inputs)):
            coefficient = D[i][j]
            if coefficient != 0:
                terms.append(f"({coefficient})*{inputs[j]}")

        rhs = " + ".join(terms).replace("+ (-", "- (")
        print(f"y{i+1} = {rhs}")

def numeric_matrixes(A: list, B: list, C: list, D: list, sym: dict):
    a = []
    b = []
    c = []
    d = []
    for i in range(len(A)):
        a.append([])
        for j in range(len(A[i])):
            a[i].append(float(A[i][j].subs(sym)))
    for i in range(len(B)):
        b.append([])
        for j in range(len(B[i])):
            b[i].append(float(B[i][j].subs(sym)))
    for i in range(len(C)):
        c.append([])
        for j in range(len(C[i])):
            c[i].append(float(C[i][j].subs(sym)))
    for i in range(len(D)):
        d.append([])
        for j in range(len(D[i])):
            d[i].append(float(D[i][j].subs(sym)))      
    return a, b, c, d
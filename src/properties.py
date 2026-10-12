class SystemProps:
    @staticmethod
    def is_stable(A: np.ndarray) -> bool:
        eigen = np.linalg.eigvals(A)
        for e in eigen:
            if (re(e) >= 0):
            return False
        return True
    @staticmethod
    def is_controlable(A: np.ndarray, B: np.ndarray) -> bool:
        n = A.shape[0]
        Cc = np.zeros((n, n))
        for i in range(n):
            Cc[:, i] = (np.linalg.matrix_power(A, i) @ B)[:,0]
        return np.linalg.matrix_rank(Cc) == n
    @staticmethod
    def is_observable(A: np.ndarray, C: np.ndarray) -> bool:
        n = A.shape[0]
        O = np.zeros((n, n))
        for i in range(n):
            O[:, i] = (C @ np.linalg.matrix_power(A, i))[:,0]
        return np.linalg.matrix_rank(O) == n
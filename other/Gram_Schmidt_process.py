# Ортногонализация Грамма Шмидта базиса (получение ортогонального базиса)

def ort_basis(old_basis):
    # ортоганилизирует данный базис (не нормирует)
    proj = lambda b, a: (np.dot(a, b) / np.dot(b, b)) * b
    new_basis = []
    
    for i in range(len(old_basis)):
        b = old_basis[i]
        for n in range(i):
            b = b - proj(new_basis[n], old_basis[i])

        new_basis.append(b)
    return new_basis
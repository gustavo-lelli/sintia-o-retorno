import numpy as np

def verifica_base(vetores):
    matriz = np.array(vetores)
    determinante = np.linalg.det(matriz)
    if abs(determinante) > 1e-9:  # Considerando precisão numérica
        return "SimTia, o Retorno"
    else:
        return "Não"

# Exemplo de uso
d = int(input())
vetores = [list(map(float, input().split())) for _ in range(d)]
resultado = verifica_base(vetores)
print(resultado)
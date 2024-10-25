# esse é um caso de uma matriz 2D linearizada
class Solution(object):
    def searchMatrix(self, matrix, target):
        # Número de linhas (m) e colunas (n)
        m, n = len(matrix), len(matrix[0])
        esquerda, direita = 0, m * n - 1

        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            linha = meio // n
            coluna = meio % n
            valor_meio = matrix[linha][coluna]

            if valor_meio == target:
                return True
            elif valor_meio < target:
                esquerda = meio + 1
            else:
                direita = meio - 1

Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3)
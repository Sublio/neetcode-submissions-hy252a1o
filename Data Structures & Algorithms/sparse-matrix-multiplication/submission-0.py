class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
            m, k = len(mat1), len(mat1[0])
            k2, n = len(mat2), len(mat2[0])
            
            mat1_nonzero = []
            for i in range(m):
                row = []
                for p in range(k):
                    if mat1[i][p] != 0:
                        row.append((p, mat1[i][p]))
                mat1_nonzero.append(row)
            
            mat2_nonzero = [[] for _ in range(k)]
            for p in range(k):
                for j in range(n):
                    if mat2[p][j] != 0:
                        mat2_nonzero[p].append((j, mat2[p][j]))
            
            result = [[0] * n for _ in range(m)]
            for i in range(m):
                for p, val1 in mat1_nonzero[i]:
                    for j, val2 in mat2_nonzero[p]:
                        result[i][j] += val1 * val2
            
            return result
        
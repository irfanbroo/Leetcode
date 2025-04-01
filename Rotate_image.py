class Solution:
    def trans(self, matrix):
        m = len(matrix)
        for i in range(m):
            for j in range(i+1,m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
    
    def swap(self, matrix):
        m = len(matrix)
        for i in range(m):
            for j in range(m//2):
                matrix[i][j], matrix[i][m-j-1] = matrix[i][m-j-1], matrix[i][j]
        return matrix
    
    
    def rotate(self, matrix: List[List[int]]) -> None:
        self.trans(matrix)
        self.swap(matrix)
        

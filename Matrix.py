class Matrix():
    '''
    Class Matrix:
        Input: matrix
        Methods:
            Addition: +
            Subtraction: -
            Multiplication matrix with matrix or matrix with number: *
            Count of columns, count of rows: shape
            Transponse 
            Determinant
    ^_^
    '''
    def __init__(self, matrix):
        if not len(matrix):
            raise ValueError("Matrix is empty")
        rows_len = set(map(len, matrix))
        if len(rows_len) !=1:
            raise ValueError("Matrix rows have different length")
        self.matrix = matrix
        # Count of columns
        self.count_of_columns = len(matrix[0])
        # Count of rows
        self.count_of_rows = len(matrix)
        

    # ADD
    def __add__(self, other_matrix):
        
        if (self.count_of_columns != len(other_matrix[0])) or (self.count_of_rows != len(other_matrix)):
            raise ValueError("Matrices of different dimensions")

        mat_add = []
        for i in range(self.count_of_rows):
            row = []
            for j in range(self.count_of_columns):
                row.append(self.matrix[i][j] + other_matrix[i][j])
            mat_add.append(row)
        return Matrix(mat_add)
    

    # SUB
    def __sub__(self, other_matrix):
        return self + (-other_matrix)
    

    # MUL
    def __mul__(self, other_matrix):
        if isinstance(other_matrix, Matrix):
            mat_mul = []
            for i in range(self.count_of_rows):
                row = []
                for j in range(self.count_of_columns):
                    sum_row = 0
                    for k in range(len(other_matrix)):
                        sum_row += self.matrix[i][k] * other_matrix[k][j]
                    row.append(sum_row)
                mat_mul.append(row)
        else:
            mat_mul = []
            for i in range(self.count_of_rows):
                row = []
                for j in range(self.count_of_rows):
                    row.append(other_matrix * self.matrix[i][j])
                mat_mul.append(row)
        return Matrix(mat_mul)
    
    
    def __len__(self):
        return len(self.matrix)

    # Shape
    @property
    def shape(self):
        return self.count_of_columns, self.count_of_rows
    

    # GETITEM
    def __getitem__(self, pos):
        if isinstance(pos, tuple):
            # Retrun item
            item1, item2 = pos
            return self.matrix[item1][item2]
        else:
            # Retrun row 
            item = pos
            return self.matrix[item]
        
    # NEGATIVE 
    def __neg__(self):
        mat = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(-self.matrix[i][j])
            mat.append(row)
        return Matrix(mat)
    

    # POSITIVE
    def __pos__(self):
        return self 
    
    # STR
    def __str__(self):
        row = ''
        for i in range(len(self.matrix)):
            row += f'{self.matrix[i]}\n'
        return row

    # Transponse
    @property
    def Transponse(self):
        mat = []
        for i in range(self.count_of_columns):
            row = []
            for j in range(self.count_of_rows):
                row.append(self.matrix[j][i])
            mat.append(row)
        return Matrix(mat)

    # Determinant
    @property
    def determinant(self):
        det = 1
        for i in range(len(self.matrix)):
            for j in range(i + 1, len(self.matrix)):
                factor = self.matrix[j][i] / self.matrix[i][i]
            
                for k in range(i, len(self.matrix)):
                    self.matrix[j][k] -= factor * self.matrix[i][k]
                

        for i in range(len(self.matrix)):
            det *= self.matrix[i][i]
        if det == 0:
            return 0
        else:
            return det
                


# Тests
if __name__ == '__main__':  

    # print(Matrix.__doc__)

    # Create two matrix
    mat1 = [[1,2,3], 
            [4,5,6], 
            [7,8,9]]

    mat2 = [[9,8,7], [6,5,4], [3,2,1]]
    
    # Create two instances
    m1 = Matrix(mat1)
    m2 = Matrix(mat2)

    print(type.__dir__(Matrix))
    # print()
    # # ADD
    # print(f"If they belong to the same class m1 + m2: \n{m1 + m2}")
    # print('-'*100)

    # # SUB
    # print(f"If they belong to the same class m1 - m2: \n{m1 - m2}")
    # print('-'*100)

    # # MUL
    # print(f"If they belong to the same class m1 * m2: \n{m1 * m2}")
    # print('-'*100)

    # # LEN
    # print(f"Length of the first row of the matrix: {len(m1[0])}")
    # print('-'*100)

    # # Get item 
    # print(f"Get item from index m1[0, 1]: {m1[0, 1]}")
    # print('-'*100)
    # print(f"Get row from index m1[0, 1]: {m1[1]}")


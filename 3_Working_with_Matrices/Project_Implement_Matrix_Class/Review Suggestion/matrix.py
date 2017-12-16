import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here

        else:
            determinant = self.g[0][0] * self.g[1][1] - self.g[0][1] * self.g[1][0]

        return determinant

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        trace = 0
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        else:
            for i in range(self.h):
                trace += self.g[i][i]
        return trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        
        # TODO - your code here
    
        inverse = identity(self.h)
        if self.h == 1:
            inverse[0][0] = 1 / self[0][0]
        elif self.h == 2:
            detA = self[0][0] * self[1][1] - self[0][1] * self[1][0]
            #trA = self[0][0] + self[1][1]
            if detA == 0:
                raise ValueError('The matrix has no inverse matrix')
            else:
                inverse[0][0] = (1 / detA) * self.g[1][1]
                inverse[0][1] = (-1 / detA) * self.g[0][1]
                inverse[1][0] = (-1 / detA) * self.g[1][0]
                inverse[1][1] = (1 / detA) * self.g[0][0]
            
        return inverse


    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        return Matrix([[self.g[row][col] for row in range(self.h)] for col in range(self.w)])


    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        else:
            return Matrix([[self.g[row][col] + other.g[row][col] for col in range(self.w)] for row in range(self.h)])
        
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        return Matrix([[-self.g[row][col] for col in range(self.w)] for row in range(self.h)])

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        else:
            return Matrix([[self.g[row][col] - other.g[row][col] for col in range(self.w)] for row in range(self.h)])
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        def dot_product(v1, v2):
            return sum([v1[i] * v2[i] for i in range(len(v1))])
        
        def get_row(matrix, row_number):
            return matrix[row_number]

        def get_column(matrix, column_number):
            return [matrix[i][column_number] for i in range(len(matrix))]   

        return Matrix([[dot_product(get_row(self.g, i), get_column(other.g, j)) for j in range(other.w)] for i in range(self.h)])

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            return Matrix([[other * self.g[row][col] for col in range(self.w)] for row in range(self.h)])
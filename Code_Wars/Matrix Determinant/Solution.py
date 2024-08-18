import math

def determinant(matrix):
    n=len(matrix)
    if n==1:
        return matrix[0][0]
    elif n==2:
        return (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
    else:
        sum = 0
        counter = 1
        for z, i in enumerate(matrix[0]):
            new_matrix = []
            for d, g in enumerate(matrix[1:]):
                row = []
                for y,b in enumerate(g):
                    if not y==z:
                        row.append(b)
                new_matrix.append(row)
            sum += (math.pow(-1, z) * i * determinant(new_matrix))
            counter += 1
        return sum
            




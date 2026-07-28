def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        while True:
            row = list(map(int, input(f"Enter row {i + 1}: ").split()))
            if len(row) == cols:
                matrix.append(row)
                break
            else:
                print(f"Error: Please enter exactly {cols} values.")
    return matrix


def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:5}", end="")
        print()


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)

    return result


def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


def multiply_matrices(matrixA, matrixB):
    rowsA = len(matrixA)
    colsA = len(matrixA[0])
    colsB = len(matrixB[0])

    result = []
    for i in range(rowsA):
        row = []
        for j in range(colsB):
            total = 0
            for k in range(colsA):
                total += matrixA[i][k] * matrixB[k][j]
            row.append(total)
        result.append(row)

    return result


def main():
    print("PART A - Transpose Matrix")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    display_matrix(matrix)

    print("\nTransposed Matrix:")
    display_matrix(transpose_matrix(matrix))

    print("\nPART B - Add Two Matrices")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Enter Matrix 1:")
    matrix1 = read_matrix(rows, cols)

    print("Enter Matrix 2:")
    matrix2 = read_matrix(rows, cols)

    print("\nSum Matrix:")
    display_matrix(add_matrices(matrix1, matrix2))

    print("\nPART C - Multiply Two Matrices")
    rowsA = int(input("Enter rows for Matrix A: "))
    colsA = int(input("Enter columns for Matrix A: "))

    print("Enter Matrix A:")
    matrixA = read_matrix(rowsA, colsA)

    rowsB = int(input("Enter rows for Matrix B: "))
    colsB = int(input("Enter columns for Matrix B: "))

    if colsA != rowsB:
        print("Error: Number of columns in Matrix A must equal the number of rows in Matrix B.")
        return

    print("Enter Matrix B:")
    matrixB = read_matrix(rowsB, colsB)

    print("\nProduct Matrix:")
    display_matrix(multiply_matrices(matrixA, matrixB))


# Run the program
main()

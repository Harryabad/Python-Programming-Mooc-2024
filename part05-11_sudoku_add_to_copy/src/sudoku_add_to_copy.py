# Write your solution here

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    newDoku = []
    for row in sudoku:
        new_row = []
        for column in row:
            new_row.append(column)
        newDoku.append(new_row)
        
    newDoku[row_no][column_no] = number
    return newDoku
def print_sudoku(sudoku: list):
    newRow = 0
    newCol = 0

    for row in range(9):
        for column in range(9):
            if sudoku[row][column] == 0:
                sudoku[row][column] = "_"

    newDoku = sudoku[:]


    for newRow in range(9):
        if newRow > 0 and newRow % 3 == 0:
            print()
        
        for newCol in range(9):
            print(newDoku[newRow][newCol], end=" ")
            if (newCol + 1) % 3 == 0:
                print(end=" ")

        print()

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]


    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
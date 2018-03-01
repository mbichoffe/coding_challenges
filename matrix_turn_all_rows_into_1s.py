def convert_grid_to_ones(grid):
    rows = set()
    cols = set()
    for col in range(len(grid)):
        for row in range(len(grid[0])):
            if grid[row][col] == 1:
                rows.add(row)
                cols.add(col)

    ###Creating a matrix###
    c = len(grid)
    r = len(grid[0])

    new_grid = [[0]*r for i in range(c)]
    for row in rows:
        for col in range(c):
            new_grid[row][col] =1
    for col in cols:
        for row in range(r):
            new_grid[row][col] = 1
    return new_grid







new_grid = convert_grid_to_ones([[1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

for line in new_grid:
    print(line)
    print()


print('GRID BEFORE')
grid = [[0 for i in range(4)]for i in range(4)]
grid[1][1] = 1
grid[3][2] = 1
for row in grid:
    print(row)
print('**************')
def find_coordinates(matrix):
    all_coordinates = []
    row_length = len(matrix[0])
    col_length = len(matrix)
    for row in range(row_length):
        for col in range(col_length):
            if matrix[row][col] == 1:
                all_coordinates.append((row, col))
    return all_coordinates
def update_columns(matrix):

    coordinates = find_coordinates(matrix)

    row_length = len(matrix[0])
    col_length = len(matrix)
    for coordinate in coordinates:
        row, col = coordinate
        for i in range(row_length):
            grid[row][i] = 1
        for j in range(col_length):
            grid[j][col] = 1
print('AFTER')
update_columns(grid)
for row in grid:
    print(row)


def zero_matrix(matrix):
    """Given an NxM matrix, for cells=0, set their row and column to zeroes."""

    # START SOLUTION

    # Empty matrices are returned
    # (otherwise we'd hit an error when we ask for matrix[0]!)
    if not matrix:
        return []

    nrows = len(matrix)     # number of rows
    ncols = len(matrix[0])  # number of cols (in 1st row; will be same for all)

    # Make lists to keep track of which rows and columns we should clear
    clear_rows = [False] * nrows   # [False, False, ...] x many rows as have
    clear_cols = [False] * ncols   # [False, False, ...] x as many cols as have

    # Pass 1: figure out which cols/rows to clear and set those in our lists
    for y in range(nrows):
        for x in range(ncols):
            if matrix[y][x] == 0:
                clear_rows[y] = True
                clear_cols[x] = True

    # Pass 2: clear rows and columns
    for y in range(nrows):
        for x in range(ncols):
            if clear_rows[y] or clear_cols[x]:
                matrix[y][x] = 0

    return matrix
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
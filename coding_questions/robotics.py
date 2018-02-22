# -----

# def own_row_mines(row, index):
#     mines = 0
#
#     if index > 0:
#         if row[index - 1] == 1:
#             mines += 1
#
#     if index < len(row) - 1:
#         if row[index + 1] == 1:
#             mines += 1
#
#     return mines
#
#
# def row_mines(row, index):
#     mines = 0
#     start = index - 1
#     finish = index + 1
#
#     if index == 0:
#         start = 0
#
#     if index == len(row) - 1:
#         finish = index
#
#     for i in range(start, finish):
#         if row[i] == 1:
#             mines += 1
#
#     return mines
#
#
# def mines(grid, col_index, row_index):
#     mines = own_row_mines(grid[col_index], row_index)
#
#     if col_index > 0:
#         mines += row_mines(grid[col_index - 1], row_index)
#
#     if col_index < len(grid) - 1:
#         mines += row_mines(grid[col_index + 1], row_index)
#
#     return mines
#
#
# def count_mines(grid):
#     res = []
#
#     for i in range(len(grid)):
#         res.append([])
#
#         for j in range(len(grid[i])):
#             res[i].append(mines(grid, i, j))
#
#
#     return res

# ----
# Next Fibonacci number greater than 'Limit'

def fib_next(n1, n2, limit):
    next = n1 + n2
    if next > limit:
        return next

    return fib_next(n2, next, limit)


def fib(limit_list):
    start, n2 = 0, 1

    res = []
    for limit in limit_list:
        res.append(fib_next(start, n2, limit))

    return res

# ----
# given matrix filled out with 0 and 1. 1 - is mines.
# create mines mask for minesweeper game

def miner_mask(grid):
    col_len = len(grid)

    mask = [[0 for _ in range(len(grid[i]))] for i in range(col_len)]

    for col in range(col_len):
        row_len = len(grid[col])

        for row in range(row_len):

            if grid[col][row] != 0:

                if col > 0:
                    mask[col-1][row] += 1

                    if row > 0:
                        mask[col-1][row-1] += 1

                    if row < row_len - 1:
                        mask[col-1][row+1] += 1

                if row > 0:
                    mask[col][row-1] += 1

                if row < row_len - 1:
                    mask[col][row+1] += 1

                if col < col_len - 1:
                    mask[col+1][row] += 1

                    if row > 0:
                        mask[col+1][row-1] += 1

                    if row < row_len - 1:
                        mask[col+1][row+1] += 1

    return mask


if __name__ == '__main__':

#    print(count_mines([[0, 1, 0], [0, 0, 0], [1, 0, 0]]))

#    print(miner_mask([[0, 1, 0], [0, 0, 0], [1, 0, 0]]))

    limit_list = [9, 22, 100]

    result = fib(limit_list)

    # Output
    for num in result:
        print(num)

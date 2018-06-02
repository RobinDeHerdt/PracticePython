board = [['_' for x in range(100)] for y in range(63)]


def buildTree(max_depth=5, x_pos=50, y_pos=0, height=16):
    if max_depth <= 0:
        return

    max_depth -= 1

    # Straight up
    for i in range(height):
        y_pos += 1
        board[y_pos][x_pos] = '1'

    branch_point_x = x_pos
    branch_point_y = y_pos

    # Branch to the left
    for i in range(height):
        x_pos -= 1
        y_pos += 1

        board[y_pos][x_pos] = '1'

    buildTree(max_depth, x_pos, y_pos, height // 2)

    # Reset the x and y positions to start
    # the next branch in the correct spot
    x_pos = branch_point_x
    y_pos = branch_point_y

    # Branch to the right
    for i in range(height):
        x_pos += 1
        y_pos += 1
        board[y_pos][x_pos] = '1'

    buildTree(max_depth, x_pos, y_pos, height // 2)


def print_board():
    for i in board:
        line = ''
        for j in i:
            line += j

        print(line)


buildTree(5)
print_board()

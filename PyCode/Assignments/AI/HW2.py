import math

board_size = 9
black = 0
white = 0
size = 1  # 1 for empty board

# Accumulate all state until fill all board
while white != (board_size // 2 + 1):
    # Next turn
    if black == white:
        black += 1
    else:
        white += 1
    # All possible state non-consideration of overlapping
    stateThisTurn = math.perm(board_size, black + white)
    # Delete overlap combination
    stateThisTurn = stateThisTurn / (math.factorial(black) * math.factorial(white))
    size += stateThisTurn

print(size)

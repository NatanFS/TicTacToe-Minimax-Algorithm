from queue import Empty
import tictactoe as ttt
X = "X"
O = "O"
EMPTY = None
# board = [
#     [O, O, O ],
#     [EMPTY, EMPTY, X],
#     [EMPTY, EMPTY, X],
# ]
board = ttt.initial_state()
print(ttt.minimax(board=board))
# print(ttt.result(board=board, action=(1,0)))
# print(board)
# print(ttt.result(board))
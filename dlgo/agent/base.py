import random
from dlgo.agent.helpers import is_point_an_eye
from dlgo.goboard import Move
from dlgo.gotypes import Point

class Agent():
  def __init__(self):
    pass

  def select_move(self, game_state):
    candidates = []
    for r in range(1, game_state.board.num_rows + 1):
      for c in range(1, game_state.board.num_cols + 1):
        candidate = Point(row=r, col=c)
        if game_state.is_valid_move(Move.play(candidate)) and \
        not is_point_an_eye(game_state.board, candidate, game_state.next_player):
          candidates.append(candidate)
    if not candidates:
      return Move.pass_turn()
    return Move.play(candidates[0])
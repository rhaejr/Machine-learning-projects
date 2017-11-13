import re, random


class TicTacToe:
    def __init__(self):
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        self.moves = {'1': (0, 0), '2': (0, 1), '3': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '7': (2, 0),
                      '8': (2, 1), '9': (2, 2)}
        self.positions_groups = (
            [[(x, y) for y in range(3)] for x in range(3)] +  # horizontals
            [[(x, y) for x in range(3)] for y in range(3)] +  # verticals
            [[(d, d) for d in range(3)]] +  # diagonal from top-left to bottom-right
            [[(2 - d, d) for d in range(3)]]  # diagonal from top-right to bottom-left
        )
        self.play_game()

    def get_winner(self, board):
        """Return winner piece in board (None if no winner)."""
        for positions in self.positions_groups:
            values = [board[x][y] for (x, y) in positions]
            if len(set(values)) == 1 and values[0]:
                return values[0]

    def play_game(self, player='player'):
        for i in range(9):
            if i % 2 == 0:
                if player == 'player':
                    x, y = self.coords('X')
                    self.board[x][y] = 'X'
            else:
                x, y = self.coords('O')
                self.board[x][y] = 'O'

            print(self.board[0])
            print(self.board[1])
            print(self.board[2])

            if self.get_winner(self.board) == 'X' or self.get_winner(self.board) == 'O':
                break
        print(self.get_winner(self.board))

    def coords(self, player):
        correct = False

        while not correct:
            if player == 'O':
                move = '{}'.format(random.randint(1,9))
            else:
                # move = '{}'.format(random.randint(1, 9))
                move = input('{}[1-9]: '.format(player))
            correct = bool(re.match('^[1-9]$', move))
            x, y = self.moves[str(move)]
            try:
                if self.board[int(x)][int(y)] != ' ':
                    correct = False
            except IndexError:
                correct = False
        print()
        return int(x), int(y)


if __name__ == '__main__':
    # while True:
    TicTacToe()
        # input()

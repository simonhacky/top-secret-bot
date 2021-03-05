class Player:
    def __init__(self, player_id, alliance):
        self.player_id = player_id
        self.alliance = alliance


class Board:
    fields = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def move(self, index, player):
        self.fields[index] = player.alliance

    def is_won_by(self, player):
        possible_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for combination in possible_combinations:
            if all(self.fields[i] == player.alliance for i in combination):
                return True
        return False

    def is_full(self):
        return all(i != ' ' for i in self.fields)

    def to_string(self):
        string = ''
        for i in range(len(self.fields)):
            if i % 3 == 0 and i != 0:
                string += '\n'
            if self.fields[i] == 'x':
                string += '<:x:1451>'
            if self.fields[i] == 'o':
                string += '<:o:1447>'
            if self.fields[i] == ' ':
                string += '<:white_square_button:1546>'
        return string


class Game:
    def __init__(self, player_x_id, player_o_id):
        self.player_x = Player(player_x_id, 'x')
        self.player_o = Player(player_o_id, 'o')
        self.board = Board()

    def move(self, player_id, index):
        self.board.move(index - 1, self.player_x if player_id == self.player_x.player_id else self.player_o)
        return self.board.to_string()

    def get_winner(self):
        if self.board.is_won_by(self.player_x):
            return 'Player X has won the game!'
        if self.board.is_won_by(self.player_o):
            return 'Player O has won the game!'
        if self.board.is_full():
            return 'Game is drawn!'
        return False

    def reset(self):
        self.board.fields = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        return self.board.to_string()


game = None

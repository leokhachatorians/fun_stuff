import random
"""
1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by over-population.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""
class GameBoard():
    def __init__(self, rows=10, *, columns=10):
        self.rows = rows
        self.columns = columns

        self.__create_board()
        self.fill_board_randomly()
        # self.simple_test()
        self.neighbours = {}
        
    def __create_board(self):
        self.board = []
        for row in range(self.rows):
            self.board.append([])
            for cell in range(self.columns):
                self.board[row] += ['-']

    def glider_test(self):
        self.board = [
        ['-','-','-','-','-','-','-','-','-','-'],
        ['-','-','-','*','-','-','-','-','-','-'],
        ['-','-','-','-','*','-','-','-','-','-'],
        ['-','-','*','*','*','-','-','-','-','-'],
        ['-','-','-','-','-','-','-','-','-','-'],
        ['-','-','-','-','-','-','-','-','-','-'],
        ['-','-','-','-','-','-','-','-','-','-'],
        ['-','-','-','-','-','-','-','-','-','-'],
        ['-','-','-','-','-','-','-','-','-','-'],
        ['-','-','-','-','-','-','-','-','-','-'],
        ['-','-','-','-','-','-','-','-','-','-'],
        ]

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
    
    def fill_board_randomly(self):
        for row in range(1, self.rows - 1):
            for cell in range(1, self.columns - 1):
                number = self.get_random_number()

                if number == 1:
                    self.board[row][cell] = '*'

    def get_random_number(self):
        random_number = random.randrange(0,2)
        return random_number

    def find_neighbors(self):
        for row in range(1, self.rows - 1):
            for cell in range(1, self.columns - 1):
                total = 0
                if self.board[row][cell-1] == '*':
                    total += 1
                if self.board[row][cell+1] == '*':
                    total += 1
                if self.board[row-1][cell] == '*':
                    total += 1
                if self.board[row+1][cell] == '*':
                    total += 1
                if self.board[row+1][cell-1] == '*':
                    total += 1
                if self.board[row-1][cell+1] == '*':
                    total += 1
                if self.board[row+1][cell+1] == '*':
                    total += 1
                if self.board[row-1][cell-1] == '*':
                    total += 1
                self.neighbours[row, cell] = total

    def next_generation(self):
        for coords in self.neighbours:
            if self.neighbours[coords] > 3:
                self.board[coords[0]][coords[1]] = '-'
            elif self.neighbours[coords] < 2:
                self.board[coords[0]][coords[1]] = '-'
            elif self.neighbours[coords] == 3:
                self.board[coords[0]][coords[1]] = '*'

    def run_x_generations(self, x):
        for i in range(x):
            self.find_neighbors()
            self.next_generation()
            self.print_board()
            print('\n')

if __name__ == '__main__':
    rows = int(input('Rows: '))
    columns = int(input('Columns: '))
    generations = int(input('Generations: '))
    board = GameBoard(rows=rows,columns=columns)
    board.run_x_generations(generations)
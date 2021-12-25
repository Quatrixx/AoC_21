board_size = 5

class Board:
    bingo = False
    numbers = [[]]
    unmarked_numbers = []
    matches_in_col, matches_in_row = [], []

    def check_bingo(self, called_n):
        if called_n in self.unmarked_numbers:
            for row_index, row in enumerate(self.numbers):
                try:
                    col_index = row.index(called_n)
                    self.matches_in_row[row_index] += 1
                    self.matches_in_col[col_index] += 1
                except ValueError:
                    pass
            self.unmarked_numbers.remove(called_n)
            for row_matches in self.matches_in_row:
                if row_matches == board_size:
                    self.bingo = True
                    return True
            for col_matches in self.matches_in_col:
                if col_matches == board_size:
                    self.bingo = True
                    return True
        return False

    def sum_of_unmarked_nums(self):
        sum = 0
        for num in self.unmarked_numbers:
            sum += num
        return sum

    def init_tracking(self):
        for row in self.numbers:
            self.matches_in_row.append(0)
            for n in row:
                self.unmarked_numbers.append(n)
        for col in self.numbers[0]:
            self.matches_in_col.append(0)

    def __init__(self):
        self.bingo = False
        self.matches_in_col = []
        self.matches_in_row = []
        self.unmarked_numbers = []
        self.numbers = []

with open('day4.in') as input:
    called_numbers = [int(n) for n in input.readline().split(',')]
    nextline = input.readline()
    boards = []
    while nextline:
        b = Board()
        for r in range(5):
            number_row_string = input.readline().strip().replace("  ", ' ').split(' ')
            b.numbers.append([int(n) for n in number_row_string])
        b.init_tracking()
        boards.append(b)
        nextline = input.readline()

bingoes = 0
sum = 0
for c in called_numbers:
    for b in boards:
        if b.bingo == False:
            if b.check_bingo(c):
                bingoes += 1
                if bingoes == 1:
                    sum = b.sum_of_unmarked_nums()
                    print(f"first bingo: sum= {sum} call= {c}\n"
                        f"final_score= {sum * c}")
                if bingoes == len(boards):
                    break
    if bingoes == len(boards):
        sum = b.sum_of_unmarked_nums()
        print(f"last bingo: sum= {sum} call= {c}\n"
            f"final_score= {sum * c}")
        break

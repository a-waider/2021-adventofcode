from typing import Tuple


def parseFile(input: str):
    randomNumbers = [int(i) for i in input.splitlines()[0].split(",")]
    boards: 'list[Board]' = []
    for game in input.split("\n\n"):
        if not game.__contains__(","):  # Random numbers already read
            boards.append(Board(game))
    return randomNumbers, boards


class Board:
    def __init__(self, input: str):
        self.board, self.marks, self.matrixSize = self.getBoardFromInput(input)
        self.winner = False

    def getBoardFromInput(self, input: str) -> 'Tuple[list[list[int]], list[list[int]], int]':
        rows = input.split("\n")
        board = []
        marks = []
        for row in rows:
            tmp1 = []
            tmp2 = []
            matrixSize = 0
            columns = row.split(" ")
            for column in columns:
                if column:  # Ignore numbers with leading space
                    tmp1.append(int(column))
                    tmp2.append(False)
                    matrixSize += 1
            board.append(tmp1)
            marks.append(tmp2)
        return board, marks, 5

    def move(self, input: int) -> None:
        for i, row in enumerate(self.board):
            for j, column in enumerate(row):
                if column == input:
                    self.marks[i][j] = True

    def checkWin(self) -> bool:
        for i in range(self.matrixSize):  # Check rows for win
            counter = 0
            for j in range(self.matrixSize):
                if self.marks[i][j]:
                    counter += 1
            if counter == 5:
                self.winner = True
                return True
        for i in range(self.matrixSize):  # Check columns for win
            counter = 0
            for j in range(self.matrixSize):
                if self.marks[j][i]:
                    counter += 1
            if counter == 5:
                self.winner = True
                return True
        return False

    def sum(self) -> int:
        score: int = 0
        for i, row in enumerate(self.marks):
            for j, column in enumerate(row):
                if not column:
                    score += self.board[i][j]
        return score


file = open("4/input.txt", "r")
randomNumbers, boards = parseFile(file.read())
file.close()

firstWinner: Board = None
lastWinner: Board = None
winningOrder: 'list[Board]' = []
for randomNumber in randomNumbers:
    for board in boards:
        if not board.winner:
            board.move(randomNumber)
            if board.checkWin():
                if not firstWinner:
                    firstWinner = board
                    print(f"first winning score: {board.sum()*randomNumber}")
                lastWinner = board
                lastRandomNumber = randomNumber
                winningOrder.append(board)

# Part 2
print(f"last winning score: {lastWinner.sum()*lastRandomNumber}")

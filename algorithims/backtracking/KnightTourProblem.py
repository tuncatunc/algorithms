class KnightTourProblem:
    def __init__(self, N):
        self.N = N
        self.board = [[None for x in range(N)] for y in range(N)]
        self.offsets = [
            (2, 1), 
            (2, -1), 
            (-2, 1), 
            (-2, -1), 
            (1, 2), 
            (1, -2), 
            (-1, 2), 
            (-1, -2)]

    def solveProblem(self):
        self.board[0][0] = 1  # Starts with position 0, 0

        if self.solve(2, (0, 0)):
            self.printSolution()
        else:
            print(f"No feasible solution is found for board {self.N}x{self.N}")
       
    def printSolution(self):
        print("----------")
        for row in range(self.N):
            for col in range(self.N):
                if (self.board[row][col] == self.N * self.N):
                    print("💥", end="\t")
                else:
                    print(self.board[row][col], end="\t")
            print()

    def isValid(self, position):
        row = position[0]
        col = position[1]
        return row < self.N and row >= 0 and col < self.N and col >= 0 and self.board[row][col] == None


    def solve(self, step, position):
        if self.N * self.N < step:
            return True

        for offsett in self.offsets:
            nextRow = position[0] + offsett[0]
            nextCol = position[1] + offsett[1]
            nextPosition = (nextRow, nextCol)

            if self.isValid(nextPosition):
                self.board[nextRow][nextCol] = step

                if self.solve(step + 1, nextPosition):
                    return True

                # Backtrack
                self.board[nextRow][nextCol] = None

        return False


if __name__ == "__main__":
    knightTourProblem = KnightTourProblem(7)
    knightTourProblem.solveProblem()
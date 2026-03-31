'''Sudoku'''

import random

class Sudoku:
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.original_board = [[0 for _ in range(9)] for _ in range(9)]

    def print_board(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                if self.board[i][j] == 0:
                    print(".", end=" ")
                else:
                    print(self.board[i][j], end=" ")
            print()

    def is_valid(self, row, col, num):
        # Verificar linha
        for j in range(9):
            if self.board[row][j] == num:
                return False
        # Verificar coluna
        for i in range(9):
            if self.board[i][col] == num:
                return False
        # Verificar caixa 3x3
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[box_row + i][box_col + j] == num:
                    return False
        return True

    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.board[row][col] = num
                            if self.solve():
                                return True
                            self.board[row][col] = 0
                    return False
        return True

    def generate_puzzle(self, difficulty=40):
        # Preencher caixas diagonais 3x3 primeiro
        self.fill_diagonal()
        # Preencher células restantes
        self.solve()
        # Remover números para criar quebra-cabeça
        cells = [(i, j) for i in range(9) for j in range(9)]
        random.shuffle(cells)
        for i, j in cells[:difficulty]:
            self.board[i][j] = 0
        # Copiar para original
        for i in range(9):
            for j in range(9):
                self.original_board[i][j] = self.board[i][j]

    def fill_diagonal(self):
        for box in range(3):
            self.fill_box(box * 3, box * 3)

    def fill_box(self, row, col):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                self.board[row + i][col + j] = nums.pop()

    def is_complete(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return False
        return True

    def play(self):
        print("Bem-vindo ao Sudoku!")
        print("Digite jogadas como: linha coluna número (baseado em 1-9, ex.: 1 1 5)")
        print("Digite 'resolver' para resolver o quebra-cabeça")
        print("Digite 'sair' para sair")
        while not self.is_complete():
            self.print_board()
            move = input("Sua jogada: ").strip().lower()
            if move == 'sair':
                break
            elif move == 'resolver':
                if self.solve():
                    print("Quebra-cabeça resolvido!")
                    self.print_board()
                else:
                    print("Nenhuma solução encontrada.")
                break
            else:
                try:
                    row, col, num = map(int, move.split())
                    row -= 1
                    col -= 1
                    if 0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9:
                        if self.original_board[row][col] == 0:
                            if self.is_valid(row, col, num):
                                self.board[row][col] = num
                            else:
                                print("Jogada inválida!")
                        else:
                            print("Não é possível alterar os números originais!")
                    else:
                        print("Entrada inválida!")
                except:
                    print("Entrada inválida!")
        if self.is_complete():
            print("Parabéns! Você resolveu o quebra-cabeça!")

if __name__ == "__main__":
    game = Sudoku()
    game.generate_puzzle()
    game.play()
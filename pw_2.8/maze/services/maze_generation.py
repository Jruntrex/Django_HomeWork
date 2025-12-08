import random

def generate_maze(n=10, density=0.2):
    """
    Генерує лабіринт NxN.
    S - старт, F - фініш, X - стіна, _ - прохід.
    """
    maze = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == 0 and j == 0:
                row.append("S")
            elif i == n - 1 and j == n - 1:
                row.append("F")
            else:
                cell = "_" if random.random() > density else "X"
                row.append(cell)
        maze.append(row)
    return maze
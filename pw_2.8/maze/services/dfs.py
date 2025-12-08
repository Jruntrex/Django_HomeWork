def solve_maze_dfs(maze):
    n = len(maze)
    start = (0, 0)
    # Стек: (координати, шлях)
    stack = [(start, [start])]
    visited = set()

    while stack:
        (curr_i, curr_j), path = stack.pop()

        # Перевірка на фініш
        if curr_i == n - 1 and curr_j == n - 1:
            return path

        if (curr_i, curr_j) in visited:
            continue
        visited.add((curr_i, curr_j))

        # Логіка сусідніх клітинок
        moves = []

        # Праворуч
        if curr_j + 1 < n and maze[curr_i][curr_j + 1] != "X":
            moves.append((curr_i, curr_j + 1))

        # Вниз
        if curr_i + 1 < n and maze[curr_i + 1][curr_j] != "X":
            moves.append((curr_i + 1, curr_j))
        
        # Вгору
        # if curr_i - 1 >= 0 and maze[curr_i - 1][curr_j] != "X":
        #    moves.append((curr_i - 1, curr_j))
        
        # Ліворуч
        # if curr_j - 1 >= 0 and maze[curr_i][curr_j - 1] != "X":
        #    moves.append((curr_i, curr_j - 1))

        for next_move in moves:
            stack.append((next_move, path + [next_move]))

    return []
from django.shortcuts import render, redirect
from .services.maze_generation import generate_maze
from .services.dfs import solve_maze_dfs
import copy  # Щоб створювати копію матриці

def maze_view(request):
    """Генерація лабіринту"""
    context = {}
    
    if request.method == 'POST':
        try:
            size = int(request.POST.get('size', 10))
            density = float(request.POST.get('density', 0.2))
        except ValueError:
            size = 10
            density = 0.2

        matrix = generate_maze(n=size, density=density)
        request.session['maze_matrix'] = matrix
        
        context = {
            'matrix': matrix,
            'size': size,
            'density': density
        }

    return render(request, 'maze.html', context)

def solve_view(request):
    """Пошук шляху"""
    # 1. Беремо оригінальний лабіринт із сесії
    original_matrix = request.session.get('maze_matrix')
    
    if not original_matrix:
        return redirect('maze')

    # 2. Робимо глибоку копію, щоб малювати шлях, не псуючи оригінал в сесії
    display_matrix = copy.deepcopy(original_matrix)

    # 3. Шукаємо шлях
    path = solve_maze_dfs(original_matrix)
    
    # 4. НАЙГОЛОВНІШЕ: Мітимо шлях прямо в матриці для відображення
    # Якщо координата (r, c) є в шляху — ставимо там літеру 'P' (Path)
    if path:
        for r, c in path:
            # Не замальовуємо Старт (S) і Фініш (F)
            if display_matrix[r][c] != 'S' and display_matrix[r][c] != 'F':
                display_matrix[r][c] = 'P' 

    context = {
        'matrix': display_matrix, # Передаємо вже розмальовану матрицю
        'solved': True,
        'has_path': bool(path)
    }
    
    return render(request, 'maze.html', context)
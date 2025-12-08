from django.http import HttpResponse

def calculate_factorial(request, n):

    if n < 0:
        return HttpResponse(f"Факторіал не визначений для від'ємних чисел: {n}")
    
    # 0! = 1 за визначенням
    if n == 0:
        return HttpResponse(f"Факторіал числа 0: 1")

    # Алгоритм обчислення
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return HttpResponse(f"Факторіал числа {n}: {result}")
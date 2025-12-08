from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

FEEDBACK_STORAGE = []

# ================================
# ЗАВДАННЯ 1-2: Факторіал + Redirect
# ================================

@csrf_exempt
def factorial_input(request):
    # Якщо це POST-запит (натиснули кнопку)
    if request.method == 'POST':
        try:
            n_val = request.POST.get('n_value')
            if not n_val:
                return HttpResponse("Введіть число!")
            
            n = int(n_val)
            
            # Логіка факторіала
            if n < 0:
                res = "Error (Negative)"
            elif n == 0:
                res = 1
            else:
                res = 1
                for i in range(1, n + 1):
                    res *= i
            
            # ПЕРЕНАПРАВЛЕННЯ на сторінку результату
            return redirect(f'/result/?val={res}')
            
        except ValueError:
            return HttpResponse("Будь ласка, введіть ціле число.")

    # Якщо це GET-запит (просто відкрили сторінку)
    html = """
    <h1>Завдання 1: Факторіал</h1>
    <form method="POST">
        <label>Введіть число n:</label>
        <input type="number" name="n_value" required>
        <button type="submit">Рахувати</button>
    </form>
    """
    return HttpResponse(html)

def factorial_result(request):
    # Отримуємо результат з URL (?val=...)
    value = request.GET.get('val', 'Невідомо')
    
    html = f"""
    <h1>Результат</h1>
    <p>Факторіал дорівнює: <strong>{value}</strong></p>
    <br>
    <a href="/factorial/">Рахувати знову</a>
    """
    return HttpResponse(html)


# ================================
# ЗАВДАННЯ 3-4: Відгуки + Статистика
# ================================

@csrf_exempt
def feedback_form(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_rating = request.POST.get('rating')
        
        if user_name and user_rating:
            # Зберігаємо у глобальний список
            FEEDBACK_STORAGE.append({
                'name': user_name,
                'rating': int(user_rating)
            })
            # ПЕРЕНАПРАВЛЕННЯ на статистику
            return redirect('/rating/')
    
    # Форма відгуку
    html = """
    <h1>Завдання 2: Відгуки</h1>
    <form method="POST">
        <label>Ваше ім'я:</label><br>
        <input type="text" name="username" required><br><br>
        
        <label>Оцінка (1-5):</label><br>
        <input type="number" name="rating" min="1" max="5" required><br><br>
        
        <button type="submit">Надіслати</button>
    </form>
    """
    return HttpResponse(html)

def rating_page(request):
    total = len(FEEDBACK_STORAGE)
    
    # Рахуємо середнє
    if total > 0:
        s = sum(item['rating'] for item in FEEDBACK_STORAGE)
        avg = round(s / total, 2)
    else:
        avg = 0
        
    # Формуємо список статистики по оцінках
    stats_list = ""
    for r in range(1, 6):
        count = sum(1 for item in FEEDBACK_STORAGE if item['rating'] == r)
        stats_list += f"<li>Оцінка {r}: {count} разів</li>"
        
    html = f"""
    <h1>Статистика відгуків</h1>
    <p>Всього відгуків: {total}</p>
    <p>Середня оцінка: {avg}</p>
    <ul>
        {stats_list}
    </ul>
    <hr>
    <a href="/feedback/">Додати ще один відгук</a>
    """
    return HttpResponse(html)
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
import random

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <title>Вгадай число</title>
    <style>
        body { font-family: sans-serif; text-align: center; margin-top: 50px; }
        .message { padding: 10px; font-weight: bold; font-size: 1.2em; color: #333; }
        .success { color: green; }
        .error { color: #d9534f; }
        input { padding: 10px; font-size: 16px; }
        button { padding: 10px 20px; font-size: 16px; cursor: pointer; }
    </style>
</head>
<body>
    <h1>Гра "Вгадай число" (1-100)</h1>
    
    <div class="message">
        {message_html}
    </div>

    <form action="/guess/" method="POST">
        <input type="number" name="user_guess" required placeholder="Введіть число..." min="1" max="100">
        <button type="submit">Submit</button>
    </form>
    
    <br>
    <form action="/reset/" method="POST">
        <button type="submit" style="background-color: #f0ad4e;">Скинути гру</button>
    </form>
</body>
</html>
"""

@csrf_exempt 
def game_page(request):
    """
    GET: Відображає форму та повідомлення.
    POST: Обробляє спробу вгадати число (PRG патерн).
    """
    
    # Ініціалізація гри
    if 'target_number' not in request.session:
        request.session['target_number'] = random.randint(1, 100)
        request.session['message'] = "Я загадав число від 1 до 100. Спробуй вгадати!"

    # --- POST ЗАПИТ ---
    if request.method == "POST":
        try:
            user_guess = int(request.POST.get('user_guess'))
            target = request.session['target_number']

            if user_guess == target:
                request.session['message'] = f"<span class='success'>Вітаю! Ви вгадали число {target}. Я загадав нове.</span>"
                request.session['target_number'] = random.randint(1, 100)
            elif user_guess < target:
                request.session['message'] = f"<span class='error'>Число {user_guess} замале! Спробуй більше.</span>"
            else:
                request.session['message'] = f"<span class='error'>Число {user_guess} завелике! Спробуй менше.</span>"
        
        except (ValueError, TypeError):
            request.session['message'] = "Будь ласка, введіть коректне число."

        return redirect('game_url')

    # --- GET ЗАПИТ ---
    else:
        message = request.session.get('message', '')

        response_html = HTML_TEMPLATE.replace("{message_html}", message)
        
        return HttpResponse(response_html)

@csrf_exempt
def reset_game(request):
    request.session.flush()
    return redirect('game_url')
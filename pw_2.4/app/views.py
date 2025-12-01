from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import zlib
from datetime import datetime

# ============================================
# ЗАВДАННЯ 2.4 
# ============================================

def hello(request, name, year):
    # 1. Обчислення віку
    try:
        year = int(year)
    except ValueError:
        return HttpResponse("Рік має бути числом", status=400)
    
    current_year = datetime.now().year
    age = current_year - year

    # 2. РОБОТА З СЕСІЄЮ (Лічильник переглядів)
    # Отримуємо значення 'views', якщо немає — буде 0
    views_count = request.session.get('views', 0)
    views_count += 1
    # Зберігаємо оновлене значення
    request.session['views'] = views_count

    # 3. РОБОТА З COOKIES (Читання)
    # Формуємо список всіх кук, які прийшли від клієнта
    cookies_html = "<ul>"
    if request.COOKIES:
        for k, v in request.COOKIES.items():
            cookies_html += f"<li><strong>{k}</strong>: {v}</li>"
    else:
        cookies_html = "<li>Cookies порожні (або це перший візит)</li>"
    cookies_html += "</ul>"

    # 4. Формуємо відповідь (HTML)
    html_content = f"""
    <html>
        <head><title>Hello App</title></head>
        <body style="font-family: sans-serif; padding: 20px;">
            <h1>Hello {name}! Тобі {age} років.</h1>
            <hr>
            
            <h3>Статистика (Session):</h3>
            <p>Кількість переглядів цієї сторінки: <b style="color: blue; font-size: 1.2em;">{views_count}</b></p>
            
            <hr>
            <h3>Наявні Cookies (HttpRequest.COOKIES):</h3>
            {cookies_html}
        </body>
    </html>
    """

    response = HttpResponse(html_content)

    # 5. ВСТАНОВЛЕННЯ COOKIE (Завдання: прізвище автора)
    response.set_cookie('author', 'Hodis', max_age=3600)

    return response


# ============================================
# Старий код з PW 2.2 (hello2, hello3, comp, decomp)
# ============================================

def hello2(request):
    name = request.GET.get("name", "Anonymous")
    year = request.GET.get("year", "2000")
    try:
        year = int(year)
        age = datetime.now().year - year
    except ValueError:
        return HttpResponse("Невірний параметр year", status=400)
    return HttpResponse(f"Hello {name}! Тобі {age} років.")

@csrf_exempt
def hello3(request):
    if request.method != "POST":
        return HttpResponse("Only POST allowed", status=405)
    try:
        data = json.loads(request.body)
    except:
        return HttpResponse("Invalid JSON", status=400)
    name = data.get("name", "Anonymous")
    year = data.get("year", 2000)
    try:
        year = int(year)
    except ValueError:
        return HttpResponse("Invalid year", status=400)
    age = datetime.now().year - year
    return JsonResponse({"message": f"Hello {name}! Тобі {age} років."})

@csrf_exempt
def comp(request):
    if request.method != "POST":
        return HttpResponse("Only POST allowed", status=405)
    try:
        data = json.loads(request.body)
    except:
        return HttpResponse("Invalid JSON", status=400)
    text = data.get("text", "")
    compressed = zlib.compress(text.encode("utf-8"))
    return JsonResponse({
        "compressed_hex": compressed.hex(),
        "original_length": len(text),
        "compressed_length": len(compressed),
    })

@csrf_exempt
def decomp(request):
    if request.method != "POST":
        return HttpResponse("Only POST allowed", status=405)
    try:
        data = json.loads(request.body)
    except:
        return HttpResponse("Invalid JSON", status=400)
    data_hex = data.get("data_hex", "")
    try:
        compressed_bytes = bytes.fromhex(data_hex)
        decompressed = zlib.decompress(compressed_bytes).decode("utf-8")
    except Exception as e:
        return HttpResponse(f"Error decompressing: {str(e)}", status=400)
    return JsonResponse({"text": decompressed})
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import zlib
from datetime import datetime

# === ЗАВДАННЯ 1 ===
def hello(request, name, year):
    # Додамо безпечне приведення типів
    try:
        year = int(year)
    except ValueError:
        return HttpResponse("Рік має бути числом", status=400)
        
    current_year = datetime.now().year
    age = current_year - year
    return HttpResponse(f"Hello {name}! Тобі {age} років.")

# === ЗАВДАННЯ 2 ===
def hello2(request):
    name = request.GET.get("name", "Anonymous")
    year = request.GET.get("year", "2000")

    try:
        year = int(year)
        age = datetime.now().year - year
    except ValueError:
        return HttpResponse("Невірний параметр year", status=400)

    return HttpResponse(f"Hello {name}! Тобі {age} років.")

# === ЗАВДАННЯ 3 ===
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

# === ЗАВДАННЯ 4 ===
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
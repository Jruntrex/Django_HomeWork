from django.http import HttpResponse
from .models import Product
import random

# --- Перегляд товарів ---
def product_list(request):
    products = Product.objects.all()
    
    rows = ""
    for p in products:
        rows += f"""
        <tr>
            <td>{p.id}</td>
            <td>{p.name}</td>
            <td>{p.min_players}-{p.max_players}</td>
            <td>{p.genre}</td>
            <td>{p.price} грн</td>
        </tr>
        """
    
    html = f"""
    <h1>Склад настільних ігор</h1>
    <style>
        table {{ border-collapse: collapse; width: 60%; }}
        th, td {{ border: 1px solid black; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
    </style>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Назва</th>
                <th>Гравців</th>
                <th>Жанр</th>
                <th>Ціна</th>
            </tr>
        </thead>
        <tbody>
            {rows}
        </tbody>
    </table>
    <br>
    <p>Щоб додати авто-товари, перейдіть за посиланням: <code>/replenish/5</code> (де 5 - кількість)</p>
    """
    return HttpResponse(html)

# --- Генерація нових товарів ---
def replenish_products(request, count):
    prefixes = ["Super", "Mega", "Magic", "Space", "Dark", "Funny"]
    roots = ["Dungeon", "Empire", "Race", "Battle", "Mystery", "Farm"]
    genres = ["Strategy", "RPG", "Party", "Family", "Wargame"]

    for _ in range(count):
        name = f"{random.choice(prefixes)} {random.choice(roots)} {random.randint(1, 100)}"
        min_p = random.randint(1, 3)
        max_p = random.randint(min_p + 1, 8)
        genre = random.choice(genres)
        price = random.randint(300, 3000)

        Product.objects.create(
            name=name,
            min_players=min_p,
            max_players=max_p,
            genre=genre,
            price=price
        )
    
    return HttpResponse(f"<h1>Успішно додано {count} нових ігор!</h1> <a href='/products/'>Повернутися до списку</a>")
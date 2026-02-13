from django.http import HttpResponse

def index(request):
    html = """
    <h1>Добро пожаловать!</h1>
    <ul>
        <li><a href="http://127.0.0.1:8000/autor/">О сайте</a></li>
        <li><a href="http://127.0.0.1:8000/about/">Страница о магазине</a></li>
    </ul>
    """
    return HttpResponse(html)

def autor(request):
    html = """
    <h2>Автор: Швед Даниил Александрович</h2>
    <p> <b>Да, это я сделал лабу</b> </p>
    <p> 17 лет |  Любитель настюх</p>
    """
    return HttpResponse(html)

def about(request):
    html = """
    <h3> Наш магазин</h3>
    <p> Работаем,  Низкие цены,  Не китай</p>
    <p> <a href="https://www.salmo.by/?srsltid=AfmBOorK6ctFK3KR0yPAQLk_-mb3ln30L5-9vyCb-oySW4rHkl-HwbVD">КАТАЛОГ</a> </p>
    """
    return HttpResponse(html)
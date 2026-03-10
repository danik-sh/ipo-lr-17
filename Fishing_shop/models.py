from django.db import models

def validate_not_negative(value):
    if value < 0:
        raise ValueError(
            ('число не может быть отрицательным')
        )

class Categories(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    discription = models.TextField(blank=True, verbose_name='Описание')
    class Meta:
        verbose_name_plural = 'Категория товара'

def __str__(self):
    return self.title

class Manufacturer(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    country = models.CharField(max_length=100, verbose_name='Страна')
    discription = models.TextField(blank=True, verbose_name='Описание')
    class Meta:
        verbose_name_plural = 'Производитель'

def __str__(self):
    return self.title

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    discription = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Фотография')
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_not_negative], verbose_name='Цена')
    in_stock = models.IntegerField(validators=[validate_not_negative], verbose_name='На складе')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name='Производитель')
    class Meta:
        verbose_name_plural = 'Продукт'

def __str__(self):
    return self.title  
    


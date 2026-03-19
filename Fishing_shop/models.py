from django.db import models
from django.contrib.auth.models import User

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
        
class Bucket(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='bucket',
        verbose_name='пользоваетель'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'   
    )
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'
        ordering = ['-created_at']

    def __str__(self):
        return  f'Корзина пользователя {self.user.username}'
    
    def total_cost(self):
        ...
        return 0
    
def validator_for_bucket(self):
     if self.quantity > self.product.stock_quantity:
            raise ValueError({
                'quantity': f'Недостаточно товара на складе. Доступно: {self.product.stock_quantity} шт.'
            })
     
class Item_in_bucket(models.Model):
    bucket = models.ForeignKey(
        Bucket,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Корзины'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='bucket_items',
        verbose_name='Товар'
    )

    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Количество',
        validators=[validator_for_bucket]
    )

    def __str__(self):
        return f'{self.product.title} ({self.quantity} шт.)'
    
    def item_price(self):
        return self.product.price * self.quantity
    
    class Meta:
        verbose_name_plural = 'Объект корзины'
    

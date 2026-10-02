from django.db import models


class Product(models.Model):
    GENRE_CHOICES = [
        ('Jazz', 'Jazz'),
        ('Soul', 'Soul'),
        ('Rock', 'Rock'),
        ('Electronic', 'Electronic'),
    ]

    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    emoji = models.CharField(max_length=8, default='💿')
    bg_color = models.CharField(max_length=7, default='#17161A')
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} — {self.artist}"


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ]

    customer_name = models.CharField(max_length=120, blank=True)
    customer_email = models.EmailField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def recalculate_total(self):
        self.total = sum(item.subtotal() for item in self.items.all())
        self.save(update_fields=['total'])


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price_at_purchase = models.DecimalField(max_digits=8, decimal_places=2)

    def subtotal(self):
        return self.price_at_purchase * self.quantity

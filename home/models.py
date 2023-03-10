from django.db.models import Model, CharField, TextField, DecimalField, ImageField, \
    ForeignKey, CASCADE, SET_NULL, IntegerField, DateTimeField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    name = CharField(max_length=55)
    parent = TreeForeignKey('self', SET_NULL, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']


class Product(Model):
    name = CharField(max_length=255)
    about = TextField(null=True, blank=True)
    description = TextField(null=True, blank=True)
    seller = ForeignKey('Seller', CASCADE, related_name='owner', null=True, blank=True)
    price = DecimalField(decimal_places=2, max_digits=9)
    image = ImageField(upload_to='products/default-image/')
    category = ForeignKey('Category', CASCADE)
    orders = IntegerField(default=1)
    owner = ForeignKey('User', CASCADE, related_name='owner', null=True, blank=True)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        # ordering = ('-created_at',)
        db_table = 'product'


class Seller(Model):
    name = CharField(max_length=255)
    description = TextField(null=True, blank=True)
    seller_name = ForeignKey('User', CASCADE, null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    vendor = ForeignKey('User', CASCADE, related_name='merchant', null=True, blank=True)
    # image = ImageField(upload_to='shops')


class Order(Model):
    product = ForeignKey('Product', CASCADE)
    user = ForeignKey('User', CASCADE)
    cart = ForeignKey('Cart', CASCADE)

    def __str__(self):
        return f"{self.product.name}"


class Cart(Model):
    product = ForeignKey('home.Product', CASCADE)
    user = ForeignKey('User', CASCADE)
    count = IntegerField(default=1)

    class Meta:
        db_table = 'cart'


class Favourite(Model):
    product = ForeignKey('home.Product', CASCADE)
    user = ForeignKey('User', CASCADE)

    class Meta:
        db_table = 'favourite'


class ProductImages(Model):
    product = ForeignKey('Product', CASCADE)
    image = ImageField(upload_to='products/images/')

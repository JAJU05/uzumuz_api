from django.db.models import Model, CharField, TextField, DecimalField, ImageField, \
    ForeignKey, CASCADE, SET_NULL, IntegerField
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
    price = DecimalField(decimal_places=2, max_digits=9)
    image = ImageField(upload_to='products/default-image/')
    category = ForeignKey('Category', CASCADE)
    seller = ForeignKey('Seller', CASCADE)
    orders = IntegerField(default=1)

    class Meta:
        # ordering = ('-created_at',)
        db_table = 'product'


class Seller(Model):
    name = CharField(max_length=255)
    description = TextField(null=True, blank=True)
    image = ImageField(upload_to='shops')


class Cart(Model):
    product = ForeignKey('home.Product', CASCADE)
    count = IntegerField(default=1)

    class Meta:
        db_table = 'cart'


class Favourite(Model):
    product = ForeignKey('home.Product', CASCADE)

    class Meta:
        db_table = 'favourite'


class ProductImages(Model):
    product = ForeignKey('Product', CASCADE)
    image = ImageField(upload_to='products/images/')



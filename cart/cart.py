from django.conf import settings
from store.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):
        product_ids = self.cart.keys()

        product_clea_ids = []

        for p in product_ids:
            product_clea_ids.append(p)

            self.cart[str(p)]['product'] = Product.objects.get(pk=p)

        for item in self.cart.values():
            item['total_price'] = float(item['price']) * int(item['quantity'])

            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        price = product.price

        print('Product_id:', product_id)

        #sprawdzam czy juz jest w koszyku produkt
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': price, 'id': product_id}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            # jak dodajemy to inkrementujemy powyzsze.
            self.cart[product_id]['quantity'] = self.cart[product_id]['quantity'] + 1

        self.save()

    def save(self):
        print(self.cart)
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

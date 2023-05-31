from tienda.models import Product
from decimal import Decimal

class Carrito():

    def __init__(self, request):
        self.session = request.session
        carrito = self.session.get('skey')
        if 'skey' not in request.session:
            carrito = self.session['skey'] = {}
        self.carrito = carrito

    def add(self, product):
        product_id = product.id
        if product_id not in self.carrito:
            self.carrito[product_id] = {'price': str(product.price)}

        self.guardar()
        
    def __iter__(self):
        product_ids = self.carrito.keys()
        products = Product.products.filter(id__in=product_ids)
        carrito = self.carrito.copy()
        for product in products:
            carrito[str(product.id)]['product'] = product
            
        for item in carrito.values():
            item['price'] = Decimal(item['price'])
            yield item
            
    def get_total_price(self):
        return sum(Decimal(item['price']) for item in self.carrito.values())
    
    def delete(self, product):
        product_id = str(product)
        if product_id in self.carrito:
            del self.carrito[product_id]
        
        self.guardar()
            
    def guardar(self):
        self.session.modified = True
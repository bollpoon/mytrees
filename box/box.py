from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Box:

    def __init__(self,request):
        """
        初始化购物车对象
        """
        self.session = request.session
        box = self.session.get(settings.CART_SESSION_ID)
        if not box:
            # 向session中存入空白购物车数据
            box = self.session[settings.CART_SESSION_ID] = {}
        self.box =box
        
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.box:
            self.box[product_id] = {'quantity': 0, 'price': str(product.minprice)}
        if update_quantity:
            self.box[product_id]['quantity'] = quantity
        else:
            self.box[product_id]['quantity'] += quantity
        self.save()
    
    def remove(self, product):
        """
        从购物车中删除商品
        """
        product_id = str(product.id)
        if product_id in self.box:
            del self.box[product_id]
            self.save()
    
    def save(self):
    # 设置session.modified的值为True，中间件在看到这个属性的时候，就会保存session
        self.session.modified = True    
     
    def __iter__(self):
        """
        遍历所有购物车中的商品并从数据库中取得商品对象
        """
        product_ids = self.box.keys()
        # 获取购物车内的所有商品对象
        products = Product.objects.filter(id__in=product_ids)

        box = self.box.copy()
        for product in products:
            box[str(product.id)]['product'] = product

        for item in box.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item    
            
    def __len__(self):
        """
        购物车内一共有几种商品
        """
        return sum(item['quantity'] for item in self.box.values())

    def get_total_price(self):
        return sum(Decimal(item['minprice'])*item['quantity'] for item in self.box.values())


    def clear(self):
        del self.session[settings.BOX_SESSION_ID]
        self.save()
        
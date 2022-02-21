from store.models import Product
from decimal import Decimal






class Basket():
    """
    A base basket class, providing some default behaviours that
    can be inherited or overrided ,as necessary. 
    """

    def __init__(self, request):
        
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket
    


    def add(self, product, qty):

    
        """ 
           adding and updating the users basket session data 

        """
   
    
        product_id = str(product.id)

        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        else:
            self.basket[product_id]={'price':str(product.price),'qty':int(qty)}

        self.save()

    def __iter__(self):  #collect the product_id in the session data to query the database and return products. 
        """
        this function is made to make the class iterable.
        this function returns the iterater for the object.
        when we ask to iterate the class Basket this function allows us to do it. Because we can't just
        grab the data from the session just iterate over it. we need to collect the data from the database.
        """
        product_ids = self.basket.keys() # we get all the keys from the session data and we have all the ids of product and we can query the database
        products = Product.products.filter(id__in=product_ids) #query the database by grabing the session id and checking the ids in the databse table.
        basket = self.basket.copy()   # copy the basket data. copy an instace of the session data.
        
        for product in products:     # taking the existing basket which contains price and qty and adding some extra info like image,etc to it
            basket[str(product.id)]['product'] = product
        
        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price']*item['qty']
            yield item


    def __len__(self):
        '''
         get the basket data and count the qty of items
        '''
        return sum(item['qty'] for item in self.basket.values())
        

    def get_total_price(self):
        return sum(Decimal(item['price'])*item['qty'] for item in self.basket.values())

    def delete(self, product):
        """
        delete item from session data
        """
        product_id = str(product)
        # print(product_id)
       
    
        if product_id in self.basket:
            del self.basket[product_id]
            
        self.session.modified = True 
    
    def update(self,product,qty):
        """
        update values in session data
        """
        product_id = str(product)

        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        self.save()


    def save(self):
        self.session.modified = True 

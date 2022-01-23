




class Basket():
    """
    A base basket class, providing some default behaviours that
    can be inherited or overrided ,as necessary. 
    """

    def __init__(self, request):
        
        self.session = request.session
        basket = self.session.get('sessionkey')
        if 'sessionkey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket
    

    def add(self, product, qty):

    
        """ 
           adding and updating the users basket session data 

        """
   
    
        product_id = product.id

        if product_id not in self.basket:
            self.basket[product_id]={'price':str(product.price),'qty':int(qty)}

            self.session.modified = True
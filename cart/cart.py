class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        else:
            self.cart = cart
    
    def add(self, product):
        if(str(product.id) not in self.cart.keys()):
            self.cart[product.id] = {
                "product_id":product.id,
                "product_name":product.name,
                "product_price":str(product.price),
                "product_amount": 1,
                "product_image": product.image.url
            }
        else:
            for key, value in self.cart.items():
                if key==str(product.id):
                    value["product_amount"] = value["product_amount"]+1
                    break
        self.saveCart()
    
    def saveCart(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def delete(self, product):
        product.id = str(product.id)
        if product.id in self.cart:
            del self.cart[product.id]
            self.saveCart()
    
    def restProduct(self, product):
        for key, value in self.cart.items():
            if key==str(product.id):
                value["product_amount"] = value["product_amount"]-1
                if value["product_amount"] < 1:
                    self.delete(value)
                break
        self.saveCart()
    
    def cleanCart(self):
        self.session["cart"] = {}
        self.session.modified = True

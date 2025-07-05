class Mobile:
    def __init__(self,brand,price):
     self.brand = brand
     self.price = price 
     

    def show_details(self):
        print("phone brand",self.brand)
        print("phone price",self.price)

#creating object

m1=Mobile("apple","80k")


#showing details

m1.show_details()

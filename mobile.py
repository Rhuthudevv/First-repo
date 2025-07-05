class Mobile:
    def __init__(self,brand,price):
     self.brand = brand
     self.price = price 
     

    def show_details(self):
        print("company",self.brand)
        print("price of mobile",self.price)

#creating object

m1=Mobile("Oppo reno","80k")


#showing details

m1.show_details()

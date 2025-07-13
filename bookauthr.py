class Book:
    def __init__(self,title,author,pages):
      
     self.title = title
     self.author = author
     self.pages = pages


    def define_info(self):
        print("title",self.title)
        print("author",self.author)
        print("pages",self.pages)

b1=Book("Rich dad poor dad","john",243)
b1.define_info()
# Write a python program to implement a class named book store with the following specifications

class BookStore:
    NoOfBooks = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        
        BookStore.NoOfBooks += 1

    def Display(self):
        print(self.Name, "by" , self.Author + "." , "No of Books : ",BookStore.NoOfBooks)

obj1 = BookStore("Lsp", "Robert Love")
obj1.Display()

obj2 = BookStore("C Programming","Dennis Richie")
obj2.Display()

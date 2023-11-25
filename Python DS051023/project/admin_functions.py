# Online Bookstore 
import json
import pandas as pd

class admin:
    def __init__(self):

# reading the data from the Books.json file : 
        self.Books = []
        try:
            file = open('Books.json','r')
            data = json.load(file)
            if data:
                self.Books = data

        except Exception as ex:
            print("Getting error in opening the file ")
            print(ex)            
    
    def add_book(self):
        bookdict = {}
        bookdict['Book_title'] = input("Enter the Book Title : ")
        bookdict['Author'] = input("Enter the name of Author : ")
        bookdict['Price'] = int(input("Enter the price of Book : "))
        bookdict['Quantity'] = int(input("Enter the stock available for the book : "))
        self.Books.append(bookdict)
        file = open("Books.json",'w')
        json.dump(self.Books, file)
        print("Book added successfully!!!")
        file.close()

    def update_book(self):
        title = input("Enter the Book title to update the book : ")
        for i in self.Books:
            if i['Book_title'] == title:
                i['Price'] = int(input("Enter the new price of the Book : "))
                i['Quantity'] = int(input("Enter the updated Quantity of Book : "))
                break

        file = open('Books.json','w')
        json.dump(self.Books,file)
        file.close()
        print("Book updated successfully!!!")

    def delete_book(self):
        title = input("Enter the Book title to update the book : ")
        for i in self.Books:
            if i['Book_title'] == title:
                self.Books.remove(i)   
                break   

        file = open('Books.json','w')
        json.dump(self.Books,file)
        file.close()
        print("Book removed from the database successfully!!!")

    def view_book_list(self):
        df = pd.DataFrame(self.Books)
        print(df)

    def view_order_history(self):
        file = open("orders.json","r")
        orders = json.load(file)
        file.close()
        df = pd.DataFrame(orders)
        print(df)
    

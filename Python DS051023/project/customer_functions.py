import json
from datetime import datetime as dt
import pandas as pd

class customer:
    def __init__(self):
        self.customers = []
        self.customer_data = {}
        file = open("customers.json","r+")
        data = json.load(file)
        file.close()
        if data:
            self.customers = data

        file = open("Books.json","r")
        self.data2 = json.load(file)
        file.close()

        file = open("orders.json","r")
        self.orders_data = json.load(file)
        file.close()


    def signup(self):
        self.customer_data['Name'] = input("Enter your name : ")
        self.customer_data['mobile_number'] = input("Enter your mobile number : ")
        self.customer_data['Address'] = input("Enter your complete address : ")
        self.customer_data['Password'] = input("create a password for your account : ")
        self.customer_data['Wishlist'] = "Wishlist"
        self.customer_data['orders'] = {}
        self.customers.append(self.customer_data)
        file = open("customers.json","w")
        json.dump(self.customers, file)
        file.close()
        print("Signed up successfully!!!")

    def view_booklist(self):
        for i in self.data2:
            print(i)

    def order_book(self,userid):
        order_dict = {}
        order = []
# Taking orders from the customer
        while True:
            name = input("Enter the name of the book to order")
            for i in self.data2:
                if i['Book_title'] == name:
                    order.append(name)
                    break
            ch = int(input("Enter 1 to order more books or enter any other character to exit"))
            if ch == 1:
                continue
            else:
                break

        print(f"Your ordered Books are : {order}")
        ch = int(input("Enter 1 to confirm your order and proceed or Enter any other character to cancel this order"))
        if ch == 1: 
            # searching for the customer in customer data and then appending the current order in their data
            for i in self.customers:
                if i['mobile_number'] == userid:
                    customer_name = i['Name']
                    dict1 = i['orders']
                    dict1[str(dt.now())] = str(order)
                    i['orders'] = dict1

            # dumping order data to customer profile
            file = open("customers.json","w")
            json.dump(self.customers,file)
            file.close()

            # appending the order data in self.orders_data variable
            order_dict["Date"] = str(dt.now())
            order_dict["Customer_name"] = customer_name
            order_dict["mobile number"] = userid
            order_dict["Order"] = str(order)
            self.orders_data.append(order_dict)

            # dumping order data in common order file
            file = open("orders.json","w")
            json.dump(self.orders_data,file)
            file.close()
        
    def Add_book_to_wishlist(self,userid):
        wishlist = []
        while True:
            name = input("Enter the name of the book to order")
            for i in self.data2:
                if i['Book_title'] == name:
                    wishlist.append(name)
                    break
            ch = int(input("Enter 1 to order more books or enter any other character to exit"))
            if ch == 1:
                continue
            else:
                break
        for i in self.customers:
            if i['mobile_number'] == userid:
                i['Wishlist'] = str(wishlist)
                break

        file = open("customers.json","w")
        json.dump(self.customers,file)
        file.close()

    def update_profile(self,userid):
        for i in self.customers:
            if i['mobile_number'] == userid:
                ch = int(input("Enter 1 to update the mobile number : "))
                if ch == 1: 
                    i['mobile_number'] = input("Enter your mobile number to update it : ")
                ch = int(input("Enter 1 to update the Address : "))
                if ch == 1: 
                    i['Address'] = input("Enter your new address : ")
                ch = int(input("Enter 1 to update the password : "))
                if ch == 1: 
                    i['Password'] = input("Enter your new password : ")

        file = open("customers.json","w")
        json.dump(self.customers,file)
        file.close()
                
    def view_order_history(self,userid):
        for i in self.customers:
            if i['mobile_number'] == userid:
                data = i['orders']
                df = pd.DataFrame(data)
                print(df)        


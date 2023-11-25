from admin_functions import admin
from customer_functions import customer
import json

print("Welcome to The Bookstore\n Enter 1. To login \n Enter 2. To signup ")
choice = int(input("Enter : "))
if choice == 1:
    userid = input("Enter your userid  :")
    password = input("Enter your password : ")
    if userid == "admin@gmail.com" and password == "Admin@12345":
        print("Logged in to Admin account successfully!!!")
        admin_obj = admin()
        while True:
            print("Enter 1. To view booklist\nEnter 2. To add a Book\n Enter 3. To update a Book\n Enter 4. To remove a Book\nEnter 5 To view order History\n Enter 0 To Exit")
            choice = int(input("Enter : "))
            if choice == 1:
                admin_obj.view_book_list()

            elif choice == 2:
                admin_obj.add_book()

            elif choice == 3:
                admin_obj.update_book()

            elif choice == 4:
                admin_obj.delete_book()

            elif choice == 5:
                admin_obj.view_order_history()

            elif choice == 0:
                break

            else:
                print("Invalid choice!!!")

    else:
        file = open("customers.json","r")
        data = json.load(file)
        file.close()

        for i in data:
            if i['mobile_number'] == userid and i["Password"] == password:
                print("Logged in successfully!!!")

                obj = customer()
                while True:
                    ch = int(input("Enter 1. To view the booklist\nEnter 2. To order the books\nEnter 3. To wishlist the books\nEnter 4. To update the profile\nEnter 5. To view the order history\nEnter 0. To Exit"))
                    if ch == 1:
                        obj.view_booklist()

                    elif ch == 2:
                        obj.order_book(userid)

                    elif ch == 3:
                        obj.Add_book_to_wishlist(userid)

                    elif ch == 4:
                        obj.update_profile(userid)

                    elif ch == 5:
                        obj.view_order_history(userid)

                    elif ch == 0:
                        break

                    else:
                        print("Invalid choice!!!")


elif choice == 2:
    obj = customer()
    obj.signup()

else:
    print("Invalid choice !!!")



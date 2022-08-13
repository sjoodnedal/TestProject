class User:

    def __init__(self,list_size,first_name,last_name,age,id_no,phone_number):
        self.id = list_size + 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.id_no = id_no
        self.phone_number = phone_number


    def get_user(self):
        return {
            "id" : self.id,
            "last_name" : self.last_name,
            "first_name" : self.first_name,
            #TODO Complete Details
        }

class Librarian(User):

    def __init__(self, list_size, first_name, last_name, age, id_no, phone_number,salary):
        super().__init__(list_size, first_name, last_name, age, id_no, phone_number)
        self.salary = salary


    #TODO Override get_user method and return salary in it

class Book:

    def __init__(self,list_size,title):
        self.id = list_size +1
        self.status = "Active"
        self.title = title
        pass
        #TODO Complete Book Class
        #
        #
        ######################

    #TODO Create a method which return Book Details
    def get_book_details(self):
        pass


    #TODO Create a method which return Book Status
    def get_status(self):
        pass


import datetime
class BorrowingOrder:

    def __init__(self,days,book_id,client_id):
        self.start_date = datetime.datetime.now()
        self.days = days
        #TODO Estimate order end date
        # self.end_date =
        # pass
        self.book_id = book_id
        self.client_id = client_id
        status = "Active"

    # TODO Create a method which return Order Status
    def get_status(self):
        pass

    # TODO Create a method which update Order Status
    def set_status(self):
        pass

users_list = []
books_list = []
orders_list = []



while True:
    t = int(input("Enter 1. Add User \n2. Add Book\n3.Create Order\n4.Browse Books\n5. Exit"))
    if t == 1 :
        first_name = input("Enter Your First Name")
        last_name = input("Enter Your Last Name")
        age = int(input("Enter Your Age"))
        phone_number = input("Phone Number")
        id_no = input("Enter Your ID NO.")
        user = User(list_size=len(users_list),first_name=first_name,last_name=last_name,age=age,phone_number=phone_number,id_no=id_no)
        users_list.append(user)
        print("User has been added Successfully")
        print(user.get_user())
    elif  t == 2 :
        user_id = input("Enter Your User ID")
        is_exist = False
        for i in users_list:
            if i.id == user_id:
                is_exist = True
                break
        if not is_exist:
            pass
            #TODO CREATE NEW USER

        # TODO Enter BOOK ID
        # FOR LOOP TO CHECK BOOK ID

    elif  t == 5:
        exit()
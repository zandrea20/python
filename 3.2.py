class Person:
    def __init__(self, first_name, last_name, address, age, phone_number):
        self.__first_name = first_name  
        self.__last_name = last_name    
        self.__address = address
        self.__age = age    
        self.__phone_number = phone_number     

    def get_info(self):
        return f"{self.__first_name} {self.__last_name}, Address: {self.__address}, Age: {self.__age}, Phone Number: {self.__phone_number}"     
    
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age
    
    def get_phone_number(self):
        return self.__phone_number
    
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_address(self, address):
        self.__address = address

    def set_studentID(self, age):
        self.__age = age

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number


person1 = Person("Zach", "Andrea", "750 Tree Cirlce", "19", "224-555-8145")
person2 = Person("Jane","Doe", "850 Lake Park", "30", "212-555-2843")
person3 = Person("John", "Doe", "850 Lake Park", "30", "212-555-7652" )
print(person1.get_info())
print(person2.get_info())
print(person3.get_info())
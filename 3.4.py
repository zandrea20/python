class Pet:
    def __init__(self, kind, breed, name):
        self.__kind = kind
        self.__breed = breed
        self.__name = name

    def get_kind(self):
        return self.__kind
    
    def get_breed(self):
        return self.__breed
    
    def get_name(self):
        return self.__name
    
    def set__kind(self, value):
        self.__kind = value
    
    def set__breed(self, value):
        self.__breed = value

    def set__name(self, value):
        self.__name = value

    def print_details(self):
        print("Pet Details:")
        print(f"Kind: {self.__kind}")
        print(f"Breed: {self.__breed}")
        print(f"Name: {self.__name}")
    
    def get_type(self):
        return type(self).__name__
    
def main():
    pet_1 = Pet("Dog","Boxer","Piper")
    print("\n\n\n")
    pet_1.print_details()
    print(f"\nType of pet_1: {pet_1.get_type()}")
main()
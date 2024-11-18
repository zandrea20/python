class Pet:
    vet_name = "Python Animal Care"

    def __init__(self,owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id 
        self.__pet_name = pet_name
        self.__pet_type = pet_type
    
    def get_owner_first_name(self):
        return self.__owner_first_name
    
    def get_owner_last_name(self):
        return self.__owner_last_name
    
    def get_pet_id(self):
        return self.__pet_id
    
    def get_pet_name(self):
        return self.__pet_name
    
    def get_pet_type(self):
        return self.__pet_type
    
    def set_owner_first_name(self, value):
        self.__owner_first_name = value
        
    def set_owner_last_name(self, value):
        self.__owner_last_name = value

    def set_pet_id(self, value):
        self.__pet_id = value
    
    def set_pet_name(self, value):
        self.__pet_name = value

    def print_pet_details(self):
        print("Pet Details:")
        print(f"Owner: {self.__owner_first_name} {self.__owner_last_name}")
        print(f"Pet ID: {self.__pet_id}")
        print(f"Pet Name: {self.__pet_name}")
        print(f"Pet Type: {self.__pet_type}")
    

    
    def check_property(self):
        if hasattr(self, '_Pet__owner_first_name') and hasattr(self, '_Pet__owner_last_name'):
            print("Pet owner first and last names exist.")
        else:
            print("Pet owner first and/or last name attributes are missing.")
        
        if hasattr(self, '_Pet__pet_id') and hasattr(self, '_Pet__pet_name'):
            print("Pet ID and pet name exist.")
        else:
            print("Pet ID and/or pet name attributes are missing.")
    

    def display_pet_info(self):
        print(f"Id: {self.__pet_id}")
        print(f"Pet Name:{self.__pet_name}")
        print(f"Type: {self.__pet_type}")

def main():
    pet_1 = Pet("Zach", "Andrea","001","Piper",)
    print("\n\n\n")

    print("\nOwner's first name:", pet_1.get_owner_first_name())

    pet_1.print_pet_details()

    print("\nChecking properties for pet_1:")
    pet_1.check_property()
     
    print("\nChecking pet info:")
    pet_1.display_pet_info()
main()
class Employee:
    def __init__(self, employee_name, employee_number):
        self.__employee_name = employee_name
        self.__employee_number = employee_number
    
    def employee_name(self):
        return self.__employee_name
    
    def employee_number(self):
        return self.__employee_number
    
    def set__employee_name(self, value):
        self.__employee_name = value

    def set__employee_number(self, value):
        self.__employee_number = value

    def __str__ (self):
        return f"Employee Name: {self.__employee_name}, Employee Number: {self.__employee_number}"
    
class ProductionWorker(Employee):
    def __init__(self, employee_name, employee_number, shift_number, hourly_pay_rate):
        super().__init__(employee_name, employee_number)
        self.__shift_number = shift_number  
        self.__hourly_pay_rate = hourly_pay_rate
    
    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate

    def set_shift_number(self, value):
        self.__shift_number = value

    def set_hourly_pay_rate(self, value):
        self.__hourly_pay_rate = value

    def __str__(self):
       
        return super().__str__() + f", Shift Number: {self.__shift_number}, Hourly Pay Rate: ${self.__hourly_pay_rate:.2f}"
    
def main():
    employee_name = input("Please enter the employees name:")

    employee_number = input("Plese enter the employee number:")

    shift_number = int(input("Please enter the employees shift number (1 for day 2 for night):"))

    hourly_pay_rate = float(input("Please enter the employees hourly pay rate $"))

    worker = ProductionWorker(employee_name, employee_number, shift_number, hourly_pay_rate)

    print("\n Production Worker Details:")
    print(worker)
    
main()
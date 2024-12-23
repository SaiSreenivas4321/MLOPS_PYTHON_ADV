class employee:
    # special method /magic method /dundermethod -constructor
    def __init__(self):
        print("DUNDER METHODS ARE CALLING HERE AND STARTED HERE ")
        self.id = 1234
        self.salary = 7000000
        self.desgination = "Data Scetinst"
        print("This values are initiated")

    def employee_class_val(self,desgination):
        print("calling the values from dunder methods ")
        print(f"employee went for desinations places {desgination}")
        pass
    # def employee():
    #     pass
# create an obj/instance of class 
sai = employee()
print(sai.desgination)
print(type(sai))
# sai.employee_class_val(desgination={""})
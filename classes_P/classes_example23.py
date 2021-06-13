# creating a class mobile and store mobile info  in that class
class mobile:
    def __init__(self,device_name,model,version,price):
        
        self.device_name=device_name
        self.model=model
        self.version=version
        self.price=price

if __name__ == "_main_":
    a1 = mobile(device_name, model, version, price)('oppo','CPHI909','V5.2.1',10500)
    print(a1.device_name)
    print(a1.model)
    print(a1.price) 
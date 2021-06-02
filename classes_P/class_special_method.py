class student:

    def __init__(self, name, cls , marks):
        self.name = name
        self.cls = cls
        self.marks = marks
    
    def show(self):
        print("name =>",self.name)
        print("cls =>",self.cls)
        print("marks =>",self.name)

    #convert object to string when printed
    def _str_(self):
        return f"{self.name} in {self.cls}"

    def _gt_(self,other):
        return self.marks > other.marks

    def _lt_(self,other):
        return self.marks < other.marks

    def _repr_(self):
        return self.name
    
    def _add_(self,other):
        return self.marks + other.marks

    
    
s1 = student('vaishali',12,78)
s2 = student('Divya',11,98)
s3 = student('smita',12,88)
s4 = student('Anjali',11,78)
s5 = student('Nidhi',10,98)

print(s1)
print(s2)

if s3.marks > s1.marks:
    print(f'{s3.name} got more marks')


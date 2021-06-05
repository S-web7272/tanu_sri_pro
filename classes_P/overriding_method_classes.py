class person:

    def _init_(self,name, age, gender):
        self.name = name 
        self.age = age 
        self.gender = gender

    def work(self):
        print(f'{self.name} is working')

    def eat(self):
        print(f'{self.name} is eating')

    def purchase(self,item):
        print(f'{self.name} purchased {item}')


class student(person):

    def _init_(self, name, age, gender,college,cls):
        return super()._init_(name, age, gender)
        self.college = college
        self.cls = cls
    def study(self):
        print(f'{self.name} is studying')

    def work(self):
        print(f'{self.name} is working on a project')

    def purchase(self,item):
        super().purchase(item)
        print("with the help of tution money")

if __name__ == "_main_":
    p = person('rahul',20,"male")
    p.work()
    p.purchase('mobile')


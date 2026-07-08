class employee:

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = seld.first + "." + self.last + "@sbcglobal.net"
        
    def giveRaise(self, salary):
        self.salary = salary
        
        
class developer(employee):
    def __init__(self, first, last, salary, language):
         super().__init__(first, last, salary)
         self.language = language
         
    def addlanguage(self, lang):
        self.language += [lang]
        
employee1 = emplopyee("Toi", "lam", 50000)
print(employee1.salary)

employee1.giveRaise(100000)
print(employee1.salary)

dev = developer("Jane", "Smith", 90000, ["Python", "C"])
print(dev.salary)

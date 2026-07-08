class A:
    def __init__(self, name):
        self.name = name
        print("Calling A: A initialized")
        
class B(A):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print("Call B: B initialized\n")
        print(self.name, self.age)
        
class C(B, A):
    def __init__(self, name, age, wage):
        super().__init__(name, age)
        self.age = age
        self.wage = wage
        print("Calling C: C initialized\n")
        
        
Obj_B = B("Toi", 18)
Obj_C = C("Lan", 18, 1000)



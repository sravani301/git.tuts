class parent:
    def myfun(self,name,age):
        self.name=name
        self.age=age
        print(self.name, self.age)
    
p1 = parent()
p1.myfun("alexa", 2)
print(p1)


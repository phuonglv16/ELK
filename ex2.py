class perform :
    def name(self,name):
        print("ten la :",name)
class studen(perform):
    def age(self,age):
        print("tuoi :", age)
teo = studen()
print(teo.name("phuong"))
print(teo.age(26))

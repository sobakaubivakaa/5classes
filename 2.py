class Person:
    def __init__(self,f_name,l_name):
        self.f_name = f_name[0].upper() + f_name[1:len(f_name)].lower()
        self.l_name = l_name[0].upper() + l_name[1:len(l_name)].lower()
    def __repr__(self):
        print(f'{self.f_name} {self.l_name}')
person1= Person("aBYLaikhan","aBDRaman" )
print(person1.f_name)
print(person1.l_name)
person1.__repr__()

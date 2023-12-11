"""
IHERITANCE
- This is the process wherre a class acquires the properties of another class.
- This class thhat acuires the properties of another is referred to asthe child class whereas the class whose properties are being acuired is referred to as the parent class.
"""

class Mammal:
    def __init__(self):
        self.no_of_legs=4
        self.blood="Warm blooded"
        self.skin_cover = "Furry"
        self.common_hobby = "Noise making"
        
    def get_hobby(self):
        return self.common_hobby


class CatFamily(Mammal):
    def __init__(self):
        super().__init__()
        self.food = "Carniovorous"
            
    def get_food(self):
        return self.food
        
"""
EXPLANITION
- The first class, Mammal, is the parent class.
- The sevcond class, cat family inthis case is the child class
- Cat family inherits the porperties ofnthe Mammal class. In python the syntax used to represent a child inhertin fro, a parent during definition

class Childclass(ParenClass):
    '''
    
Eg 
class CatFamily(Mammal):
    '''
    
We can be able to access all the Mammal properties even inside the CatFamily and even if we create a CatFamily object.
"""

cat_obj = CatFamily()
print(cat_obj.common_hobby())
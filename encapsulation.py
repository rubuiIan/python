"""
Encapcsulation helps us regulate access and modifcation of class properties eg attributes and methods

Methods and Attributes can take the  follwing characteristics
1. public: This means that they are accessible inside and outside the class. When we create an object of the class we ae able to access its attributes and methods
2. private: This means that theye are accessible only inside the class, we cannot access them outside the class. When e create an object of the class we cannot access these methods and attributes. We do this to inform we want to protect eg: apikey/appId attributes, passwords field etv. protected :TODO Go check this out

If you want to make an attribute to be private/method you add 2 '___' just before the actual name of your attribute or method.

Example 1: Attibute
self.__privete_attribute = value
Eg: self.__WEATHER_APP_ID = 'your_id_here'

Example 2: Method
SYNTAX
def __your_private_method(self):
        ...
Eg: def __prepare_params(self):


Importace of encapsulation
1. Concealing data - Eg appId that we wouldnt want the public accessing and modifying
2. Introducing read only attributes
3. Introducing write only attributes 

Inroduction to Getters and Setters
> They are mainly public methods.

Getters
-> It is a method that is used to set to fetch the value of a particular class attribute. It is mainly used to expose the value of a private attribute.
Eg If we have a private attribute called national_id, we want it to be in such a way that we are able to see the value but we cannot change it

-> So we we can create a getter method, which will return the value of our national_id The benefit of using a getter method for this is that we wont be able to modify the value of the nation)id externally
Synatax: Getter methods start with the key prefix 'get' followed by the name of the atribute whose value we want Eg"
def get_national_id(self):
    return self.__national_id # assuming thr private attributes was declared.
    
    
Setters
-> They are used to control the modification of a private attribute Eg modification of password
-> Unlike the getter method, they do not return anything, however they take up a user's value of the private attributes to be modified as a parameter
Syntax: They start with the key suffix 'set', followed by the name of the private attribute to be modified

Example
def set_password(self, modified_password):
    self.__password = modified_password_password # Assuming the private attribute was declared
    
-> In the example above, the modified_password parameter is what will carry the user's modified password

i.e my_class_obj.set_password("new password) 
"""
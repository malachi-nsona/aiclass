class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        print(f"I'm {self.name} and I'm {self.age}") 

    def is_adult(self):
        if self.age>=18:
            print(f"True:is_adult") 
        else:
            print(f"False:minor")       
#create an object using the class , in this instance the object is individual
individual=person("sarah",25)         
individual1=person("keziah",15)
individual2=person("mala",18)


#calling the greet method on the object
individual.greet()
individual1.greet()
individual2.greet()

#calling the is_adult method on the object
individual.is_adult()
individual1.is_adult()
individual2.is_adult()



















class Persona:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hola, Mi nombre es {} y yo tengo {} años".format(self.name,self.age))


if __name__ =='__main__':
    person=Persona('Moises',21)

    print('Age:{}'.format(person.age))
    person.say_hello()


class Person:
    name = "Default Name" # class param

    def __init__(self, name=None):
        self.name = name


jo = Person("Joey")
ho = Person("Honey")

un = Person()
Person.name = "jhdjfh"

print(jo.name)
print(ho.name)
print(un.name)
print(Person.name)

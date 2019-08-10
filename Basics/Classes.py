# Basic class and sub-class with inheritance structuring


class Person(object):
    def __init__(self, name):
        self.name = name

    def reveal_identity(self):
        print("My name is {}!".format(self.name))


class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name

    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print("...and I am {}!".format(self.hero_name))


p1 = Person('Dustin')
p1.reveal_identity()
print('-' * 40)
p2 = SuperHero('Wade Wilson', 'Deadpool')
p2.reveal_identity()

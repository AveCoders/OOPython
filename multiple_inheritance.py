class Parent1:
    def __init__(self):
        super().__init__()
        self.smart = "smart"
        self.hair_colour = "light"

class Parent2:
    def __init__(self):
        super().__init__()
        self.pretty = "pretty"
        self.hair_colour = "dark"


class Child(Parent2, Parent1):
    def __init__(self):
        super().__init__()

    def traits(self):
        print(self.pretty)
        print(self.smart)
        print(self.hair_colour)


child = Child()
child.traits()
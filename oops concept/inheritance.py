class Father:
    def skills(self):
        print("Driving")


class Mother:
    def talent(self):
        print("Cooking")


class Child(Father, Mother):
    def study(self):
        print("Studying")


c = Child()

c.skills()
c.talent()
c.study()
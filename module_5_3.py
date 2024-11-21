class House:
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        print(self.number_of_floors)

    def __str__(self):
        print(f'Название: {self.name} ,количество этажей: {self.number_of_floors}')


    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, other):
        self.number_of_floors += other
        return self.number_of_floors

    def __iadd__(self, other):
        self.number_of_floors += other
        return self.number_of_floors

    def __radd__(self, other):
        self.number_of_floors += other
        return self.number_of_floors

h1 = House("ЖК Апрель", 12)
h2 = House("ЖК Олимпия", 14)
h1.__len__()
h1.__str__()
print(h1 != h2)
print(h1.__add__(2))
print(h1.__iadd__(12))
print(h2.__radd__(12))
print(h1 == h2)
h1.__str__()
h2.__str__()





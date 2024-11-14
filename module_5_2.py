class House:
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        print(self.number_of_floors)

    def __str__(self):
        print(f'Название: {self.name} ,количество этажей: {self.number_of_floors}')

h1 = House("ЖК Апрель", 12)
h1.__len__()
h1.__str__()
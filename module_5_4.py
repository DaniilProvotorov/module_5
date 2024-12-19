class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)
    
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

    def __del__(self):
        print(f'{self.name}, снесён, но он останется в истории')

h1 = House("ЖК Апрель", 12)
print(House.houses_history)
h2 = House("ЖК Олимпия", 14)
print(House.houses_history)
del h1
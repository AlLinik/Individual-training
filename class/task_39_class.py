class Cities:  # Родительский класс

    def __init__(self, city, region):
        self.city = city
        self.region = region

    def info(self):
        print(f'City - {self.city}. Region - {self.region}.')

class Population(Cities):  # Дочерний класс (Наследование)
    residents = 14500

    def __init__(self, city, region):
        super(Population, self).__init__(city, region)
        # self.residents = residents

    def info(self):
        super().info()  # or print(f'City - {self.city}. Region - {self.region}.') (Полиморфизм)
        print(f'Residents - {self.residents}.')

def show_polymorphism():
    for item in [Cities, Population]:
        print('**********')
        obj_class = item('Zhabinka', 'Brest')
        obj_class.info()

show_polymorphism()

# obj_population = Population(14_500, 'Zhabinka', 'Brest')  # or obj_population = Cities()
# obj_population.info()
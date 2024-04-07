class Animal:
    def __init__(self, name, sound, age):
        self.__name = name
        self.sound = sound
        self.age = age

    def name_get(self):
        return self.__name

    def name_set(self, name):
        self.__name = name

    def sound_get(self):
        pass

    def sound_set(self):
        pass

    def age_get(self):
        pass

    def age_set(self):
        pass

class Dog(Animal):
    def sound_get(self):
        print(f'dog sound is {self.sound}')

    def sound_set(self):
        a = str(input())
        if a != 'gav' or a != 'auuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu':
            print('no')
        else:
            self.sound = a

    def age_get(self):
        print(f'Dog age is {self.age}')

    def age_set(self):
        a = int(input())
        if 0 < a < 30:
            self.age = a
        else:
            print('no')


class Homyak(Animal):
    def sound_get(self):
        print(f'homyak sound is {self.sound}')

    def sound_set(self):
        a = str(input())
        if a != 'pip' or a != 'net, ya ne umru v tualete':
            print('no')
        else:
            self.sound = a

    def age_get(self):
        print(f'homyak age is {self.age}')

    def age_set(self):
        a = int(input())
        if 0 < a < 0.000000000000000000001:
            self.age = a
        else:
            print('no')


class Popugiv(Animal):
    def sound_get(self):
        print(f'popugiv sound is {self.sound}')

    def sound_set(self):
        a = str(input())
        if a != 'pip' or a != 'aaak':
            print('no')
        else:
            self.sound = a

    def age_get(self):
        print(f'popugiv age is {self.age}')

    def age_set(self):
        a = int(input())
        if 0 < a < 15:
            self.age = a
        else:
            print('no')
sobaka=Dog('baget','gav',7)
gamlet=Homyak('gamlya','pip',0.0000000000000000000000000000000000000000000000000000000000000000000000001)
kesha=Popugiv('gosha','aaak',3)
def create_animal():
    specie=str(input())
    if specie=='1':
        animal=Dog()
    elif specie=='2':
        animal=Homyak()
    elif specie=='3':
        animal=Popugiv()
    else:
        print('error')
        return None
    animal.name_set()
    animal.sound_set()
    animal.age_set()
    return animal
def get_all(lst):
    for Animal in lst:
        print(Animal.name_get(),'    ',Animal.sound_get(),'    ',Animal.age_get(),'    ')
user_animal=None
animals=[sobaka,gamlet,kesha,user_animal]
while True:
    action=str(input())
    if action=='1':
        user_animal=create_animal()
    elif action=='2':
        get_all(animals)

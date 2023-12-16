# # shawarma=lambda da:da*2
# # da=10
# # print(shawarma(da))
# # def aboba (net):
# #     return net*2
# # print(aboba(da))
# import functools
# my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
# # new_list = list(filter(lambda x: (x%2 == 0) , my_list))
# # new_list = list(map(lambda x: x*2 , my_list))
# # print(new_list)
# # summa = functools.reduce((lambda x, y: x + y), my_list)
# # print(summa)
# tables = [lambda x = i: x*10 for i in range(1, 11)]
# for table in tables:
#     print(table())
class Person:
    # def say(self,message):
    #     print(message)
    # def sdacha(self):
    #     self.say('da')
    def __init__(self,name):
        self.name=name
        self.age=1

    def display_info(self):
        print(f"Name: {self.name}  Age: {self.age}")

tom=Person('Tom')
print(tom.name)     # Tom
print(tom.age)      # 1
# изменение значения
tom.age = 37
print(tom.age)



tom.display_info()

# tom = Person()
# bob = Person()
# tom.sdacha()
tom.company = "Microsoft"
print(tom.company)

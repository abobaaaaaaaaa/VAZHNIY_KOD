class Product:
    def __init__(self,price,name,cnt):
        self.price=price
        self.name=name
        self.cnt=cnt
    def buy(self,lst,cnt_cnt_for_buy):
        if self.cnt >= cnt_cnt_for_buy:
            lst=lst.update([self.name,cnt_cnt_for_buy])
            self.cnt=self.cnt-cnt_cnt_for_buy
            return lst
        else:
            print('netu')
            return lst
class User:
    def __init__(self,name,balance_card,balance):
        self.name=name
        self.balance_card=balance_card
        self.balance=balance
    def cash_to_card(self):
        add_sum=int(input())
        if self.balance>=add_sum:
            self.balance_card=self.balance_card+add_sum
            self.balance=self.balance-add_sum
        else:
            self.balance=0
            print('uchis schitat')
    def card_to_cash(self):
        add_sum=int(input())
        if self.balance_card>=add_sum:
            self.balance+=add_sum
            self.balance_card-=add_sum
        else:
            self.balance_card=0
            print('uchis schitat')
    def free_money(self):
        add_sum=int(input())
        self.balance_card+=add_sum
products=[Product(1000,'shwarma',2312321),Product(0,'maksik',122893),Product(43,'sukharik',421232323)]
aboba=User('aboba',40,3)
korzina= {}
while True:
    action=str(input('1-buy,2-show profile,3-pay'))
    if action=='ЬЕЪ':
        aboba.free_money()
    elif action=='1':
        product=str(input())
        product=products.index(product)
        print('neeeext......')
        cnt=int(input())
        products[product].buy(korzina,cnt)
    elif action=='2':
        print(aboba)
    elif action=='3':
        pass

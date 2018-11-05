import random


class Person(object):
    """
    Person Class

    haha
    ee
    """
    def __init__(self, name, id_card, phone_number, card):
        self.name = name
        self.id_card = id_card
        self.phone_number = phone_number
        self.card = card


class Card(object):
    """
    Card Class
    haha
    hehe
    ...
    """
    def __init__(self, card_number, password, balance):
        self.card_number = card_number
        self.password = password
        self.balance = balance


class ATM(object):
    """
    ATM Class
    """
    def __init__(self):
        self.account_infos = {}

    def save_account(self, person):
        data = {person.id_card: person}
        self.account_infos.update(data)
        print('ATM save account %s success!' % person.name)

    def show_account(self):
        for person in self.account_infos.values():
            print('-------------------')
            print('Name: ', person.name)
            print('ID Card: ', person.id_card)
            print('Phone Number: ', person.phone_number)
            print('Card: ', person.card.card_number)
            print('Balance: ', person.card.balance)


class Admin(object):
    """
    Admin Class
    """
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def menu(self):
        while True:
            print('1. 开户')
            print('2. 查询')
            print('3. 取款')
            print('4. 查询所有账号')
            print('...')

            option = input('Please input option: ')
            if option == '1':
                self.open_an_account()
            elif option == '2':
                pass
            elif option == '3':
                pass
            elif option == '4':
                self.show_all_account()
            else:
                continue

    def open_an_account(self):
        # create account
        name = input('Name: ')
        id_card = input('ID Card: ')
        phone_number = input('Phone Number: ')

        # create card
        card_number = random.randint(10000000000, 19999999999)
        password = input('Card Password (6 digit): ')
        balance = input('Please input open account money: ')
        card = Card(card_number, password, balance)

        person = Person(name, id_card, phone_number, card)
        atm.save_account(person)
        print('%s 开户成功, 卡号: %d' % (name, card_number))

    def show_all_account(self):
        atm.show_account()


admin_username = 'admin'
admin_password = 'admin'
atm = ATM()

print('Authentication Admin account: ')
tmp_username = input('Please input username: ')
tmp_password = input('Please input password: ')
if tmp_username == admin_username and tmp_password == admin_password:
    admin = Admin(tmp_username, tmp_password)
    admin.menu()
else:
    print('Username or Password r!')

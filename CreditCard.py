import re
import pandas as pd

df = pd.read_json('regex_cards.json')

class credit_card:

    def __init__(self, number):
        self.number = number
        self.card_type = type(self)
        self.valid = luhn_check(self)
        self.usable = is_allowed(self)
       
def luhn_check(self):
    number_list = [int(i) for i in str(self.number)]
    number_list.reverse()
    number_list = [sum(divmod(number_list[i]*2, 10)) if i in range(1,len(number_list),2)
                       else number_list[i] for i in range(0,len(number_list))]
    return (sum(number_list) % 10) == 0

def is_allowed(self):
    if self.card_type not in get_ban_list():
        return True
    else:
        return False

def type(self):
    for regex in df['Regular Expression'].values:
        match = re.match(regex, str(self.number))
        if match:
            type_card = df[df['Regular Expression'] == regex]['Card Type'].values[0]
            return type_card
    return 'Unknown card'
            
   
def ban_cards():
    print('\n')
    for card in df['Card Type'].unique():
        print(card)
    card = input('\nEnter The name of the card you want to ban: ')
    if card in get_ban_list():
        print('{} card is already in ban list'.format(card))
        return
    cancel = 0
    while card not in df['Card Type'].unique() and cancel != 1:
        cancel = int(input("Unknown card! To cancel enter: 1, to continue enter: 2: "))
        while cancel not in [1,2]:
            cancel = int(input("Unknown choice! To cancel enter: 1, to continue enter: 2: "))
        if cancel ==1:
            return
        card = input('Enter one of the card names listed: ')
    with open("ban.txt", "a") as ban_file:
        ban_file.write(card +"\n")
    
def remove_ban():
    ban_list = get_ban_list()
    print('\nCurrent ban list: ')
    for card in ban_list:
        print(card)
    card = input('\nEnter card you want to remove from ban: ')
    if card not in ban_list:
        print('{} is not in ban list'.format(card))
    else:
        with open("ban.txt", "r") as ban_file:
            lines = ban_file.readlines()
        with open("ban.txt", "w") as ban_file:
            for line in lines:
                if line.strip("\n") != card:
                    ban_file.write(line)
                    
def get_ban_list():
    ban_list = list()
    with open("ban.txt", "r") as ban_file:
        for line in ban_file:
            ban_list.append(line.strip())
    return ban_list

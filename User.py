import CreditCard as cc
import re

number = input('Enter a credit card number: ')
while re.search('[\D]', number):
    print('Enter digits only. No spaces or nondigit Characters')
    number = input('Enter a correct credit card number: ')

while len(str(number)) not in range(12,20):
    print('Your number is either too short or too long')
    number = input('Enter another credit card number: ')
    
    
card = cc.credit_card(int(number))

if not card.usable:
    print('Sorry! Your card cannot be used to make purchase')
    print('Try another card!')
else:
    if not card.valid:
        print('That is incorrect card number!')
    elif card.valid:
        print('{} detected!'.format(card.card_type))
        print('Proceed with transaction!')
        
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 19:13:00 2021

@author: Acer
"""

import random
 
possible_numbers = [x for x in range(1, 50)]
 
def draw_lotto_numbers():
    lotto_num = []
    for i in range(0,6):
        lotto_num.append(random.choice(possible_numbers))
        possible_numbers.remove(lotto_num[i])
    return lotto_num
 
def drawn_users_numbers(lotto_num, user_numbers):
    result = 0
    for i in range (0,6):
        if user_numbers[i] in lotto_num:
            result += 1
    return result
 
user_numbers = []
for i in range(1,7):
    number = int(input("\nChoose number " + str(i) + " : "))
    while number not in possible_numbers:
        number = int(input("""\nError! The value must belong to a set (1,49) and should't be used twice.
Choose number again : """))
    possible_numbers.remove(number)
    user_numbers.append(number)
 
print("Your numbers : ",user_numbers)
print("Numbers from Lotto : ",draw_lotto_numbers())
print("You've guessed : ",drawn_users_numbers(draw_lotto_numbers(),user_numbers))
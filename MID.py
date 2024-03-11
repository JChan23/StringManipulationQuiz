import random
import numpy as np

array = ['abcde','hijklmp']
command = ['LEFT','RIGHT','MID','ONECHAR']

string = np.random.choice(array)
command = np.random.choice(command)

def part1(s,c):
    point = 0
    if c == 'MID':
        l = len(s)
        number2 = random.randint(1,l)
        number1 = random.randint(0,l-number2)
        answer = string[number1:number1+number2]
        print("Here's the string:",string)
        print("Print",c,"start at position",(number1+1),"of length",number2)
        print(answer)
        response = input("Write down the answer you get: ")
        if response == answer:
            point = point+1
            print("That's your current points:",point)
        else:
            print("That's wrong")

part1(string,command)

# pyWars.py
# Author: Taylor Marrion
# Date: 4/19/2020
"""This file contains functions used to setup and complete pyWars challenges."""

## setup
# mkdir -p /home/teebs/Public/packets /home/teebs/Public/log /home/teebs/Public/registry
# sudo cp -R /mnt/c/Users/Teebs/Desktop/local_pyWars/* /home/teebs

## initialize python environment
# python3
# import local_pyWars as pyWars
# game = pyWars.exercise()

## sample commands
# game.question(1)
# game.data(1)
# game.answer(1, answer1(game.data(1)))

def answer1(number):
    #result = 0
    result = number + 5
    return result

def answer2(s):
    import codecs
    result = codecs.encode(s, 'rot_13')
    return result
    
def answer3(s):
    import base64
    result = base64.b64decode(s)
    return result

def answer4(s):
    result = s.upper()
    return result

def answer5(s):
    result = s.find('SANS')
    return result

def answer6(s):
    if len(s) ==0:
        return s
    else:
        return answer6(s[1:]) + s[0]

def answer7(s):
    result = s
    reverse = answer6(s)
    result += reverse
    result += s
    return result

def answer8(s):
    result = s[1] + s[4] + s[8]
    return result

def answer9(s):
    result = ""
    first = s[0]
    last = s[len(s)-1]
    middle = s[1:len(s)-1]
    result = last + middle + first
    return result
    
def answer10(s):
    result = ""
    half_int = int(len(s)/2)
    rev_start = s[half_int-1::-1]
    end = s[half_int:]
    result = rev_start + end
    return result

def answer11(s):
    result = ""
    for c in s:
        if (c == 'E'):
            result += '3'
        elif (c == 'A'):
            result += '4'
        elif (c == 'T'):
            result += '7'
        elif (c == 'S'):
            result += '5'
        elif (c == 'G'):
            result += '6'
        else :
            result += c
    return result

def answer12(d):
    return d[2]

def answer13(d):
    result = []
    i = 1
    while (i < d):
        result.append(i)
        i += 1
    return result

def answer14(d):
    return len(d)

def answer15(d):
    result = d.split(',')[9]
    return result

def answer16(d):
    result = ""
    pass_info = d.split(':')[1]
    pass_salt = pass_info.split('$')[2]
    result = pass_salt
    return pass_salt

def answer17(d):
    s = "Pywars rocks"
    d.append(s)
    return d

def answer18(d):
    result = 0
    for x in d:
        result += x
    return result

def answer19(d):
    result = 0
    numbers = d.split()
    for x in numbers:
        result += int(x)
    return result

def answer20(d):
    result = 'this' + d + 'python' + d + 'stuff' + d + 'really' + d + 'is' + d + 'fun'
    return result

def answer20_2(d):
    result = d.join(['this', 'python', 'stuff', 'really', 'is', 'fun'])
    return result
    
def answer21(d):
    result = []
    for x in range(1,1000):
        if x%d == 0:
            result.append(x)
    return result

def answer22(d):
    result = ""
    for x in d:
        result += (bytes.fromhex(x)).decode("ASCII")
    return result

def answer23(d):
    result = []
    for lst in d:
        for num in lst:
            if num not in result:
                result.append(num)
    result.sort()
    return result

# 24-26 are not available offline

def answer27(d):
    result = []
    for key in d:
        if key not in result:
            result.append(key)
    result.sort()
    return result

def answer27_2(d):
    result = []
    result = sorted(d.keys())
    return result

def answer28(d):
    result = []
    for key in d:
        if d[key] not in result:
            result.append(d[key])
    result.sort()
    return result

def answer28_2(d):
    result = []
    result = sorted(d.values())
    return result

def answer29(d):
    result = sorted([(key, d[key]) for key in d])
    #result.sort()
    return result

def answer30(d):
    result = 0
    for key in d:
        if key == 'python' or key == 'rocks':
            result += d[key]
    return result

def answer31(d):
    result = 0.0
    
    return result









"""
Algorithmic Methods of Data Mining - Homework 1
Soluzioni HackerRank, organizzate per sezione.
"""

# ============================================================
# PROBLEM 1
# ============================================================



### Challenge: <Say "Hello, World!" With Python>

if __name__ == '__main__':
    print("Hello, World!")


### Challenge: <Python If-Else>

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n > 20:
        print("Not Weird")



### Challenge: <Arithmetic Operators>

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a+b)
print(a-b)
print(a*b)


### Challenge: <Python: Division>

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b)
    print(a/b)


### Challenge: <Loops>

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i ** 2)


### Challenge: <Write a function>

def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True
        
    return leap

year = int(input())
print(is_leap(year))


### Challenge: <Print Function>

if __name__ == '__main__':
    n = int(input())
   
    for i in range(1, n + 1):
        print(i, end="")


### Challenge: <Map and Lambda Function>

cube = lambda x: x ** 3

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


### Challenge: <List Comprehensions>

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    risultato = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    
    print(risultato)



### Challenge: <Find the Runner-Up Score!> 

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # Remove duplicates by converting to a set, then sort the unique elements
    unique_scores = sorted(set(arr))
    
    # Print the second to last element (the runner-up score)
    print(unique_scores[-2])



### Challenge: <Nested Lists> 

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        # Store name and score as a nested list
        students.append([name, score])
        
   
    unique_scores = sorted(list(set([score for name, score in students])))
    second_lowest_score = unique_scores[1]
    

    target_students = [name for name, score in students if score == second_lowest_score]
    

    for student_name in sorted(target_students):
        print(student_name)


### Challenge: <Finding the percentage> 

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # Recupera i voti dello studente richiesto
    target_scores = student_marks[query_name]
    
    # Calcola la media dei voti
    average_score = sum(target_scores) / len(target_scores)
    
    # Stampa il risultato formattato a 2 cifre decimali
    print(f"{average_score:.2f}")


### Challenge: <Tuples> 

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = tuple(map(int, raw_input().split()))
    print hash(integer_list)



### Challenge: <Detect HTML Tags, Attributes and Attribute Values> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

if __name__ == '__main__':
    parser = MyHTMLParser()
    html_code = ""
    
    for _ in range(int(input())):
        html_code += input() + "\n"
        
    parser.feed(html_code)



### Challenge: <Validating UID> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    uid = input().strip()
    
    if (len(uid) == 10 and 
        uid.isalnum() and 
        len(set(uid)) == 10 and 
        len(re.findall(r'[A-Z]', uid)) >= 2 and 
        len(re.findall(r'\d', uid)) >= 3):
        print("Valid")
    else:
        print("Invalid")



### Challenge: <Validating Credit Card Numbers> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    card = input().strip()
    
    
    if re.match(r"^[456](\d{15}|\d{3}-\d{4}-\d{4}-\d{4})$", card):
        
       
        card_no_hyphens = card.replace('-', '')
        
        if re.search(r"(\d)\1{3}", card_no_hyphens):
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")



### Challenge: <Validating Postal Codes> 

regex_integer_in_range = r"^[1-9][0-9]{5}$"    # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"    


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


### Challenge: <Matrix Script> 

#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded_string = ""
for col in range(m):
    for row in range(n):
        decoded_string += matrix[row][col]


pattern = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])'
final_string = re.sub(pattern, ' ', decoded_string)

print(final_string)



### Challenge: <Validating and Parsing Email Addresses> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils


pattern = r"^[a-zA-Z][a-zA-Z0-9\-._]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$"

for _ in range(int(input())):
    raw_string = input()
    
    name, email_address = email.utils.parseaddr(raw_string)
    
   
    if re.match(pattern, email_address):
        # Riformatta e stampa la coppia se l'email è valida
        print(email.utils.formataddr((name, email_address)))




### Challenge: <Hex Color Code> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


pattern = r'(?<!^)(#[a-fA-F0-9]{6}|#[a-fA-F0-9]{3})'

for _ in range(int(input())):
    line = input()
    matches = re.findall(pattern, line)
    
    for match in matches:
        print(match)




### Challenge: <HTML Parser - Part 1> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")
            
    def handle_endtag(self, tag):
        print(f"End   : {tag}")
            
    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

if __name__ == '__main__':
    parser = MyHTMLParser()
    for _ in range(int(input())):
        parser.feed(input())




### Challenge: <HTML Parser - Part 2> 

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        
        if '\n' in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)
        
    def handle_data(self, data):
      
        if data != '\n':
            print(">>> Data")
            print(data)

html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()




### Challenge: <Default Arguments> 

class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return
def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next()) # <- Questa riga deve essere spostata a destrad



queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())





### Challenge: <Transpose and Flatten> 

import numpy


n, m = map(int, input().split())

my_array = numpy.array([input().split() for _ in range(n)], int)

print(numpy.transpose(my_array))
print(my_array.flatten())






### Challenge: <Lists> 

if __name__ == '__main__':
    N = int(input())
    my_list = []
    
    for _ in range(N):
        # Read the line and split it into a list of strings
        command = input().split()
        cmd_name = command[0]
        
        if cmd_name == 'insert':
            my_list.insert(int(command[1]), int(command[2]))
        elif cmd_name == 'print':
            print(my_list)
        elif cmd_name == 'remove':
            my_list.remove(int(command[1]))
        elif cmd_name == 'append':
            my_list.append(int(command[1]))
        elif cmd_name == 'sort':
            my_list.sort()
        elif cmd_name == 'pop':
            my_list.pop()
        elif cmd_name == 'reverse':
            my_list.reverse()





### Challenge: <Regex Substitution> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    line = input()
    line = re.sub(r"(?<= )\|\|(?= )", "or", line)
    print(line)




### Challenge: <Validating Roman Numerals> 

regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"    

import re
print(str(bool(re.match(regex_pattern, input()))))





### Challenge: <Detect Floating Point Number> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


pattern = r"^[+-]?\d*\.\d+$"

for _ in range(int(input())):
    string_to_test = input()
    
    
    is_valid_float = bool(re.match(pattern, string_to_test))
    
    print(is_valid_float)





### Challenge: <Re.split()> 

regex_pattern = r"[.,]"    # Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))




### Challenge: <Group(), Groups() & Groupdict()> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

m = re.search(r'([a-zA-Z0-9])\1', input().strip())

if m:
    # Print the captured repeating character
    print(m.group(1))
else:
    print("-1")




### Challenge: <Re.findall() & Re.finditer()> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


vowels = 'aeiouAEIOU'
consonants = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'


pattern = r'(?<=[' + consonants + r'])([' + vowels + r']{2,})(?=[' + consonants + r'])'


matches = re.findall(pattern, input().strip())


if matches:
    for match in matches:
        print(match)
else:
    print('-1')




### Challenge: <Re.start() & Re.end()> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

S = input()
k = input()


pattern = re.compile(k)
match = pattern.search(S)


if not match:
    print("(-1, -1)")
else:
   
    while match:
      subtract 1
        print(f"({match.start()}, {match.end() - 1})")
        
      
        match = pattern.search(S, match.start() + 1)






### Challenge: <Class 2 - Find the Torsional Angle> 

import math

class Points(object):
    def __init__(self, x, y, z):
        
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __sub__(self, no):
        
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        
        return (self.x * no.x) + (self.y * no.y) + (self.z * no.z)

    def cross(self, no):
       
        return Points(
            (self.y * no.z) - (self.z * no.y),
            (self.z * no.x) - (self.x * no.z),
            (self.x * no.y) - (self.y * no.x)
        )
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':nts(object):
    
    def __init__(self, x, y, z):
        
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __sub__(self, no):
        
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        
        return (self.x * no.x) + (self.y * no.y) + (self.z * no.z)

    def cross(self, no):
       
        return Points(
            (self.y * no.z) - (self.z * no.y),
            (self.z * no.x) - (self.x * no.z),
            (self.x * no.y) - (self.y * no.x)
        )
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))




### Challenge: <Set .intersection() Operation
> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

english_subscribers = set(input().split())

b = int(input())

french_subscribers = set(input().split())

both_subscribers = english_subscribers.intersection(french_subscribers)

print(len(both_subscribers))




### Challenge: <Set .difference() Operation> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

english_subscribers = set(input().split())

b = int(input())

french_subscribers = set(input().split())

english_only_subscribers = english_subscribers.difference(french_subscribers)

print(len(english_only_subscribers))


### Challenge: <Set .symmetric_difference() Operation> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

english_subscribers = set(input().split())

b = int(input())

french_subscribers = set(input().split())

exclusive_subscribers = english_subscribers.symmetric_difference(french_subscribers)

print(len(exclusive_subscribers))



### Challenge: <Set Mutations> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

num_a = int(input())

set_a = set(map(int, input().split()))

num_other_sets = int(input())

for _ in range(num_other_sets):
  
    operation, _ = input().split()

    other_set = set(map(int, input().split()))
 
    if operation == 'update':
        set_a.update(other_set)
    elif operation == 'intersection_update':
        set_a.intersection_update(other_set)
    elif operation == 'difference_update':
        set_a.difference_update(other_set)
    elif operation == 'symmetric_difference_update':
        set_a.symmetric_difference_update(other_set)

print(sum(set_a))




### Challenge: <The Captain's Room
> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())

rooms = list(map(int, input().split()))

unique_rooms = set(rooms)

captain_room = (sum(unique_rooms) * k - sum(rooms)) // (k - 1)

print(captain_room)



### Challenge: <Check Subset> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())

for _ in range(t):

    num_a = int(input())

    set_a = set(input().split())
   nt(input())
 
    set_b = set(input().split())
    
    print(set_a.issubset(set_b))




### Challenge: <Check Strict Superset> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

set_a = set(input().split())

n = int(input())

is_strict_superset = True

for _ in range(n):
    other_set = set(input().split())
    
    if not (set_a > other_set):
        is_strict_superset = False
        break

print(is_strict_superset)



### Challenge: <itertools.permutations()> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

input_data = input().split()
S = input_data[0]
k = int(input_data[1])

sorted_S = sorted(S)

perms = list(permutations(sorted_S, k))

for p in perms:
    print(''.join(p))




### Challenge: <itertools.combinations_with_replacement()> 

from itertools import combinations_with_replacement

input_data = input().split()
S = input_data[0]
k = int(input_data[1])

sorted_S = sorted(S)

combos = combinations_with_replacement(sorted_S, k)

for combo in combos:
    print("".join(combo))




### Challenge: <Compress the String!> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

s = input().strip()

result = []

for key, group in groupby(s):

    count = len(list(group))
    integer_key = int(key)

    result.append(f"({count}, {integer_key})")

print(" ".join(result))





### Challenge: <Iterables and Iterators> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

n = int(input())

letters = input().split()

k = int(input())

all_combinations = list(combinations(letters, k))

favorable_outcomes = sum(1 for combo in all_combinations if 'a' in combo)

probability = favorable_outcomes / len(all_combinations)

print(f"{probability:.3f}")



### Challenge: <Maximize It!> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

k_m = input().split()
K = int(k_m[0])
M = int(k_m[1])

lists = []
for _ in range(K):
    elements = list(map(int, input().split()[1:]))
    lists.append(elements)

max_modulo = 0

for combination in product(*lists):

    sum_of_squares = sum(x**2 for x in combination)

    current_modulo = sum_of_squares % M
    
    if current_modulo > max_modulo:
        max_modulo = current_modulo

print(max_modulo)




### Challenge: <sWAP cASE> 

def swap_case(s):
    return s.swapcase()
def swap_case(s):
    risultato = ""
    for c in s:
        if c.islower():
            risultato += c.upper()
        elif c.isupper():
            risultato += c.lower()
        else:
            risultato += c
    return risultato
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)



### Challenge: <String Split and Join
> 

def split_and_join(line):
    parole = line.split(" ")
    return "-".join(parole)
    # write your code here
def split_and_join(line):
    return "-".join(line.split(" "))
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)



### Challenge: <What's Your Name?> 

#
# Complete the 'print_full_name' function below.
#


def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")
    # Write your code here

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)



### Challenge: <Mutations> 

def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)



### Challenge: <Find a string> 

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)




### Challenge: <String Validators> 

if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))



### Challenge: <Text Alignment> 

#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))





### Challenge: <Text Wrap> 

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)



### Challenge: <Designer Door Mat> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())

for i in range(1, n, 2):
    print((".|." * i).center(m, "-"))

print("WELCOME".center(m, "-"))

for i in range(n - 2, 0, -2):
    print((".|." * i).center(m, "-"))



### Challenge: <String Formatting
> 

def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)



### Challenge: <Alphabet Rangoli> 

import string

def print_rangoli(size):
    alfabeto = string.ascii_lowercase
    larghezza = 4 * size - 3
    righe = []

    for i in range(size):
       
        lettere = [alfabeto[size - 1 - j] for j in range(i + 1)]
        meta = lettere[::-1]
        riga = "-".join(lettere + meta[1:])
        righe.append(riga.center(larghezza, "-"))

    for riga in righe + righe[-2::-1]:
        print(riga)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)



### Challenge: <Capitalize!> 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return " ".join(parola.capitalize() for parola in s.split(" "))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()



### Challenge: <The Minion Game> 

def minion_game(string):
    vocali = "AEIOU"
    stuart = 0
    kevin = 0
    n = len(string)

    for i in range(n):
        if string[i] in vocali:
            kevin += n - i
        else:
            stuart += n - i

    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)


### Challenge: <Merge the Tools!> 

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        blocco = string[i:i + k]
        risultato = ""
        for c in blocco:
            if c not in risultato:
                risultato += c
        print(risultato)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


### Challenge: <XML2 - Find the Maximum Depth> 

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    if level > maxdepth:
        maxdepth = level
    for figlio in elem:
        depth(figlio, level)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)



### Challenge: <Mean, Var, and Std> 

import numpy

n, m = map(int, input().split())
matrice = numpy.array([input().split() for _ in range(n)], int)

print(numpy.mean(matrice, axis=1))
print(numpy.var(matrice, axis=0))
print(numpy.round(numpy.std(matrice), 11))




### Challenge: <Dot and Cross> 

import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)

print(numpy.dot(a, b))



### Challenge: <Inner and Outer> 

import numpy

a = numpy.array(input().split(), int)
b = numpy.array(input().split(), int)

print(numpy.inner(a, b))
print(numpy.outer(a, b))



### Challenge: <Polynomials> 

import numpy

coefficienti = list(map(float, input().split()))
x = float(input())

print(numpy.polyval(coefficienti, x))




### Challenge: <Linear Algebra> 

import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n)], float)

print(round(numpy.linalg.det(a), 2))




### Challenge: <Input()> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
x, k = map(int, input().split())
print(eval(input()) == k)




### Challenge: <Python Evaluation> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
eval(input())




### Challenge: <Athlete Sort> 

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    arr.sort(key=lambda riga: riga[k])
    for riga in arr:
        print(*riga)





### Challenge: <Any or All> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
numeri = input().split()

print(all(int(x) > 0 for x in numeri) and any(x == x[::-1] for x in numeri))




### Challenge: <ginortS> 

# Read the input string
s = input()

sorted_s = sorted(s, key=lambda x: (
    x.isdigit(),                 
    x.isdigit() and int(x)%2==0, 
    x.isupper(),                 
    x                            
))

print("".join(sorted_s))



### Challenge: <Shape and Reshape> 

import numpy as np

input_data = input().split()

my_array = np.array(input_data, int)

reshaped_array = np.reshape(my_array, (3, 3))

print(reshaped_array)



### Challenge: <Concatenate> 

import numpy as np

n, m, p = map(int, input().split())

array_1 = np.array([input().split() for _ in range(n)], int)

array_2 = np.array([input().split() for _ in range(m)], int)

result = np.concatenate((array_1, array_2), axis=0)

print(result)





### Challenge: <Zeros and Ones> 

import numpy as np

shape = tuple(map(int, input().split()))

print(np.zeros(shape, dtype=int))

print(np.ones(shape, dtype=int))




### Challenge: <Eye and Identity> 

import numpy as np

np.set_printoptions(legacy='1.13')

n, m = map(int, input().split())

print(np.eye(n, m))



### Challenge: <Array Mathematics> 

import numpy as np

n, m = map(int, input().split())

a = np.array([input().split() for _ in range(n)], int)

b = np.array([input().split() for _ in range(n)], int)

print(a + b)          
print(a - b)          
print(a * b)          
print(a // b)         
print(a % b)          
print(a ** b)         




### Challenge: <Floor, Ceil and Rint> 

import numpy as np

np.set_printoptions(legacy='1.13')

a = np.array(input().split(), float)

print(np.floor(a))
print(np.ceil(a))
print(np.rint(a))





### Challenge: <Sum and Prod> 

import numpy as np

n, m = map(int, input().split())

my_array = np.array([input().split() for _ in range(n)], int)

sum_array = np.sum(my_array, axis=0)

print(np.prod(sum_array))



### Challenge: <Min and Max> 

import numpy as np

n, m = map(int, input().split())

my_array = np.array([input().split() for _ in range(n)], int)

min_array = np.min(my_array, axis=1)

print(np.max(min_array))



### Challenge: <Mod Divmod> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())

b = int(input())

print(a // b)

print(a % b)

print(divmod(a, b))




### Challenge: <Power - Mod Power> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
b = int(input())
m = int(input())

print(pow(a, b))

print(pow(a, b, m))




### Challenge: <Integers Come In All Sizes> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(a**b + c**d)



### Challenge: <Triangle Quest> 

for i in range(1, int(input())):
    print(i * ((10**i - 1) // 9))



### Challenge: <XML 1 - Find the Score> 

import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):

    score = len(node.attrib)
    
    for child in node:
        score += get_attr_number(child)
        
    return score
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))




### Challenge: <Validating Email Addresses With a Filter> 

import re

def fun(s):
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'

    return bool(re.match(pattern, s))

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)



### Challenge: <Standardize Mobile Number Using Decorators> 

def wrapper(f):
    def fun(l):
        formatted_list = ["+91 " + num[-10:-5] + " " + num[-5:] for num in l]
        
        return f(formatted_list)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


### Challenge: <Decorators 2 - Name Directory> 

import operator

def person_lister(f):
    def inner(people):

        return [f(person) for person in sorted(people, key=lambda x: int(x[2]))]
    return inner
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


### Challenge: <Words Score> 

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1  
    return score


n = int(input())
words = input().split()
print(score_words(words))


### Challenge: <Arrays> 

import numpy
def arrays(arr):
    return numpy.array(arr[::-1], float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


### Challenge: <Collections.deque()> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

d = deque()

for _ in range(int(input())):

    command, *args = input().split()
    
    getattr(d, command)(*args)

print(*d)



### Challenge: <Piling Up!> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):

    n = int(input())

    blocks = list(map(int, input().split()))
    
    left = 0
    right = n - 1
    current_top = float('inf')
    possible = True
    
    while left <= right:
        if blocks[left] >= blocks[right]:
            chosen = blocks[left]
            left += 1
        else:
            chosen = blocks[right]
            right -= 1

        if chosen <= current_top:
            current_top = chosen
        else:

            possible = False
            break

    if possible:
        print("Yes")
    else:
        print("No")



### Challenge: <Company Logo> 

#!/bin/python3

from collections import Counter

if __name__ == '__main__':
    s = input()

    counts = Counter(s)

    sorted_chars = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    
    for char, count in sorted_chars[:3]:
        print(f"{char} {count}")



### Challenge: <Time Delta> 

#!/bin/python3

import math
import os
import random
import re
import sys

from datetime import datetime

def time_delta(t1, t2):

    fmt = '%a %d %b %Y %H:%M:%S %z'
  whitespaces in the test case inputs
    dt1 = datetime.strptime(t1.strip(), fmt)
    dt2 = datetime.strptime(t2.strip(), fmt)
    

    diff_seconds = abs(int((dt1 - dt2).total_seconds()))

    return str(diff_seconds)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()



### Challenge: <No Idea!> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = input().split()

arr = input().split()

A = set(input().split())
B = set(input().split())

happiness = 0

for i in arr:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
        
# Print the final happiness score
print(happiness)



### Challenge: <Set .add()> 

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

distinct_stamps = set()

for _ in range(n):
    distinct_stamps.add(input().strip())

print(len(distinct_stamps))


### Challenge: <Set .discard(), .remove() & .pop()> 

n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    command, *args = input().split()
    
    getattr(s, command)(*(int(x) for x in args))

print(sum(s))



### Challenge: <Set .union() Operation> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())

english_subs = set(input().split())

b = int(input())

french_subs = set(input().split())

print(len(english_subs.union(french_subs)))


### Challenge: <Symmetric Difference> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

m_size = int(input())

m = set(map(int, input().split()))

n_size = int(input())

n = set(map(int, input().split()))

sym_diff = m.symmetric_difference(n)

    print(item)


### Challenge: <Collections.OrderedDict()> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

n = int(input())

ordered_dictionary = OrderedDict()

for _ in range(n):

    item_data = input().rsplit(' ', 1)
    item_name = item_data[0]
    item_price = int(item_data[1])
 
    ordered_dictionary[item_name] = ordered_dictionary.get(item_name, 0) + item_price

# Print the final items and their net prices
for item_name, net_price in ordered_dictionary.items():
    print(f"{item_name} {net_price}")



### Challenge: <Word Order> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

n = int(input())

word_counts = OrderedDict()

for _ in range(n):
    word = input().strip()
    word_counts[word] = word_counts.get(word, 0) + 1

print(len(word_counts))

print(*(word_counts.values()))


### Challenge: <Introduction to Sets> 

def average(array):
    distinct_heights = set(array)
    
    avg = sum(distinct_heights) / len(distinct_heights)
    return round(avg, 3)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


### Challenge: <Classes: Dealing with Complex Numbers> 

import math

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
        
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
        
    def __mul__(self, no):
        r = self.real * no.real - self.imaginary * no.imaginary
        i = self.real * no.imaginary + self.imaginary * no.real
        return Complex(r, i)

    def __truediv__(self, no):
        denominator = no.real**2 + no.imaginary**2
        r = (self.real * no.real + self.imaginary * no.imaginary) / denominator
        i = (self.imaginary * no.real - self.real * no.imaginary) / denominator
        return Complex(r, i)

    def mod(self):
        m = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(m, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')


### Challenge: <collections.Counter()> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

num_shoes = int(input())
r
shoe_inventory = Counter(map(int, input().split()))

num_customers = int(input())

total_earnings = 0

for _ in range(num_customers):
    size, price = map(int, input().split())
    
    if shoe_inventory[size] > 0:
        total_earnings += price
        shoe_inventory[size] -= 1  

print(total_earnings)


### Challenge: <DefaultDict Tutorial> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

n, m = map(int, input().split())

group_a = defaultdict(list)

for i in range(1, n + 1):
    word = input().strip()
    group_a[word].append(str(i))

for _ in range(m):
    word = input().strip()
    if word in group_a:
        print(" ".join(group_a[word]))
    else:
        print("-1")


### Challenge: <Collections.namedtuple()> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

n = int(input())

Student = namedtuple('Student', input().split())

total_marks = 0

for _ in range(n):
    student = Student(*input().split())
  
    total_marks += int(student.MARKS)

print(f"{total_marks / n:.2f}")


### Challenge: <Find Angle MBC> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

ab = int(input())
bc = int(input())

theta_rad = math.atan2(ab, bc)
r
theta_deg = round(math.degrees(theta_rad))

print(f"{theta_deg}\u00B0")



### Challenge: <Triangle Quest 2> 

for i in range(1, int(input())+1): 
    print(((10**i) // 9) ** 2)


### Challenge: <Incorrect Regex> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

t = int(input())
for _ in range(t):
    try:
        re.compile(input())
        print(True)
    except re.error:
        print(False)



### Challenge: <Reduce Function> 

from fractions import Fraction
from functools import reduce

def product(fracs):
    from functools import reduce
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator



if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)


### Challenge: <itertools.product()> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*product(a, b))


### Challenge: <Calendar Module> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar

mese, giorno, anno = map(int, input().split())
print(calendar.day_name[calendar.weekday(anno, mese, giorno)].upper())



### Challenge: <Zipped!> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

n, x = map(int, input().split())
voti = [list(map(float, input().split())) for _ in range(x)]

for studente in zip(*voti):
    print(f"{sum(studente) / x:.1f}")



### Challenge: <Polar Coordinates> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

import cmath

z = complex(input())

print(abs(z))
print(cmath.phase(z))



### Challenge: <Exceptions> 

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())
for _ in range(t):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)



### Challenge: <Birthday Cake Candles> 

#!/bin/python3

import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    return candles.count(max(candles))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


### Challenge: <Time Conversion> 

#!/bin/python3

import math
import os
import random
import re
import sys


def timeConversion(s):
    ora = int(s[:2])
    periodo = s[-2:]
    resto = s[2:-2]

    if periodo == "AM":
        if ora == 12:
            ora = 0
    else:
        if ora != 12:
            ora += 12

    return f"{ora:02d}{resto}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()



### Challenge: <Common Child> 

#!/bin/python3

import math
import os
import random
import re
import sys


def commonChild(s1, s2):
    prec = [0] * (len(s2) + 1)
    for c1 in s1:
        corr = [0]
        for j, c2 in enumerate(s2):
            if c1 == c2:
                corr.append(prec[j] + 1)
            else:
                corr.append(max(prec[j + 1], corr[j]))
        prec = corr
    return prec[-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()


### Challenge: <Bear and Steady Gene> 

#!/bin/python3

import math
import os
import random
import re
import sys

def steadyGene(gene):
    n = len(gene)
    target = n // 4

    conta = {"A": 0, "C": 0, "G": 0, "T": 0}
    for c in gene:
        conta[c] += 1

    if all(v == target for v in conta.values()):
        return 0

    migliore = n
    sinistra = 0
    for destra in range(n):
        conta[gene[destra]] -= 1

        while sinistra <= destra and all(v <= target for v in conta.values()):
            migliore = min(migliore, destra - sinistra + 1)
            conta[gene[sinistra]] += 1
            sinistra += 1

    return migliore

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()


### Challenge: <Morgan and a String> 

#!/bin/python3

import math
import os
import random
import re
import sys


def morganAndString(a, b):
    a = a + "z"
    b = b + "z"
    i = 0
    j = 0
    risultato = []
    totale = len(a) + len(b) - 2

    for _ in range(totale):
        if a[i:] <= b[j:]:
            risultato.append(a[i])
            i += 1
        else:
            risultato.append(b[j])
            j += 1

    return "".join(risultato)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        fptr.write(result + '\n')

    fptr.close()


### Challenge: <Count Strings> 

#!/bin/python3

import math
import os
import random
import re
import sys


def countStrings(r, l):
    MOD = 10**9 + 7
    trans = []

    def nuovo():
        trans.append([])
        return len(trans) - 1

    def parse(pos):
        c = r[pos]
        if c == 'a' or c == 'b':
            s = nuovo()
            e = nuovo()
            trans[s].append((c, e))
            return s, e, pos + 1
        s1, e1, pos = parse(pos + 1)
        c = r[pos]
        if c == '*':
            s = nuovo()
            e = nuovo()
            trans[s].append(('', s1))
            trans[s].append(('', e))
            trans[e1].append(('', s1))
            trans[e1].append(('', e))
            return s, e, pos + 2
        if c == '|':
            s2, e2, pos = parse(pos + 1)
            s = nuovo()
            e = nuovo()
            trans[s].append(('', s1))
            trans[s].append(('', s2))
            trans[e1].append(('', e))
            trans[e2].append(('', e))
            return s, e, pos + 1
        s2, e2, pos = parse(pos)
        trans[e1].append(('', s2))
        return s1, e2, pos + 1

    start, fine, _ = parse(0)

    def chiusura(insieme):
        pila = list(insieme)
        visti = set(insieme)
        while pila:
            x = pila.pop()
            for sim, y in trans[x]:
                if sim == '' and y not in visti:
                    visti.add(y)
                    pila.append(y)
        return frozenset(visti)

    iniziale = chiusura({start})
    ids = {iniziale: 0}
    lista = [iniziale]
    archi = []
    i = 0
    while i < len(lista):
        corrente = lista[i]
        riga = []
        for sim in 'ab':
            dest = set()
            for x in corrente:
                for s2, y in trans[x]:
                    if s2 == sim:
                        dest.add(y)
            if dest:
                d = chiusura(dest)
                if d not in ids:
                    ids[d] = len(lista)
                    lista.append(d)
                riga.append(ids[d])
        archi.append(riga)
        i += 1

    n = len(lista)
    M = [[0] * n for _ in range(n)]
    for a in range(n):
        for b in archi[a]:
            M[a][b] += 1

    accettanti = [k for k in range(n) if fine in lista[k]]

    def mul(A, B):
        C = []
        for riga in A:
            nuova = [0] * n
            for k in range(n):
                v = riga[k]
                if v:
                    Bk = B[k]
                    for j in range(n):
                        if Bk[j]:
                            nuova[j] += v * Bk[j]
            C.append([x % MOD for x in nuova])
        return C

    def vec_mul(v, A):
        nuova = [0] * n
        for k in range(n):
            if v[k]:
                Ak = A[k]
                for j in range(n):
                    if Ak[j]:
                        nuova[j] += v[k] * Ak[j]
        return [x % MOD for x in nuova]

    v = [0] * n
    v[0] = 1
    e = l
    while e:
        if e & 1:
            v = vec_mul(v, M)
        e >>= 1
        if e:
            M = mul(M, M)

    return sum(v[k] for k in accettanti) % MOD

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        r = first_multiple_input[0]

        l = int(first_multiple_input[1])

        result = countStrings(r, l)

        fptr.write(str(result) + '\n')

    fptr.close()


### Challenge: <String Function Calculation> 

#!/bin/python3

import math
import os
import random
import re
import sys


def maxValue(t):
    n = len(t)
    maxn = 2 * n + 2
    link = [-1] * maxn
    length = [0] * maxn
    cnt = [0] * maxn
    nxt = [None] * maxn
    nxt[0] = {}
    size = 1
    last = 0

    for ch in t:
        cur = size
        size += 1
        length[cur] = length[last] + 1
        cnt[cur] = 1
        nxt[cur] = {}
        p = last
        while p != -1 and ch not in nxt[p]:
            nxt[p][ch] = cur
            p = link[p]
        if p == -1:
            link[cur] = 0
        else:
            q = nxt[p][ch]
            if length[p] + 1 == length[q]:
                link[cur] = q
            else:
                clone = size
                size += 1
                length[clone] = length[p] + 1
                nxt[clone] = dict(nxt[q])
                link[clone] = link[q]
                cnt[clone] = 0
                while p != -1 and nxt[p].get(ch) == q:
                    nxt[p][ch] = clone
                    p = link[p]
                link[q] = clone
                link[cur] = clone
        last = cur


    ordine = sorted(range(1, size), key=lambda i: -length[i])
    migliore = 0
    for v in ordine:
        valore = length[v] * cnt[v]
        if valore > migliore:
            migliore = valore
        cnt[link[v]] += cnt[v]

    return migliore
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = input()

    result = maxValue(t)

    fptr.write(str(result) + '\n')


### Challenge: <Insertion Sort - Part 2> 

#!/bin/python3

import math
import os
import random
import re
import sys


def insertionSort2(n, arr):
    for i in range(1, n):
        valore = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > valore:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = valore
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)



### Challenge: <Insertion Sort - Part 1> 

#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    valore = arr[n - 1]
    i = n - 2
    while i >= 0 and arr[i] > valore:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1
    arr[i + 1] = valore
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


### Challenge: <Recursive Digit Sum> 

#!/bin/python3

import math
import os
import random
import re
import sys


def superDigit(n, k):
    somma = sum(int(c) for c in n) * k
    while somma >= 10:
        somma = sum(int(c) for c in str(somma))
    return somma

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()



### Challenge: <Viral Advertising> 

#!/bin/python3

import math
import os
import random
import re
import sys


def viralAdvertising(n):
    condivisi = 5
    cumulativo = 0
    for _ in range(n):
        piaciuti = condivisi // 2
        cumulativo += piaciuti
        condivisi = piaciuti * 3
    return cumulativo

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


### Challenge: <nome> 

#!/bin/python3

import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
    if v1 <= v2:
        return "NO"
    if (x2 - x1) % (v1 - v2) == 0:
        return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

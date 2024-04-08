print('Hello world! I dont give a bug'),

greetings = 'Hello world'
print (greetings)

#python conditionals
time = 10
if time <10:
    print ('sleep its not yet time!')
elif time > 10:
    print ('Wake up and grind!')
else: print ('seems time clock not working!')

day = 'friday'

if day == 'thursday':
    print('hey pal thursday is the new friday')
elif day == 'tuesday':
    print('focus! the week just started')
elif day == 'friday':
    print('Yay lets go party!')
else:
    print('Seems the app is not straight!')

num = 2.566

#PYTHON NUMBERS
#addition
print(type(num))

a = 5
b = 6
c = a + b

print (c)

#subtraction
d = 9
e = 6
f = d - e

print (f)

#multiplication
g = 9.7
h = 2.5
j = g*h

print (j)

#division
k = 0.640000
l = 0.88890
m = k/l

print (m)

#square/exponent
n =7
p= 9
q = 7 ** 9

print(q)

#PYTHON_LISTS
list = ['kev','nick', 'churchil', 'sam', 'davy']
print(list)

#accessinglists
print(list[2]) #(access the second item on list)
print(list[-1]) #(access the last item on list)

#Insert in a list
list = ['kev','nick', 'churchil', 'sam', 'davy']
print(list)
list.insert(2, 'stacy')
list.insert(6, 'maxy')
print(list)
new_list =list.copy()
print(new_list)

#if __name__ == '__main__':
    #a = int(input())
    #b = int(input())

a = 5
b = 6
c = a + b
d = b - a
e = a * b
print(c, d, e)


#
a = int(input())
b = int(input())

c = a // b
d = a / b

print(c)
print(d)

#loops
#GREGORIAN CALENDER
def is_leap(year):
    leap = False

    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    return leap


year = int(input(1999))
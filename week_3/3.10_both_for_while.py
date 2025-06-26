

'''#problem 1.find the factorial of the given number using for loop
num =int(input('entr the number: '))
fact = 1
if (num < 0):
    print('not defined')
else:
    for i in range(num, 1, -1):
        fact = fact * i
    print(fact)


#find the factorial of the given number using while loop

num =int(input("enter the number:"))
fact = 1
if (num<0):
    print("not defined")
else:
    while(num>0):
        fact = fact * num
        num = num -1
    print(fact)

    '''
'''

#problem 2.find the number of digits in the given number using while loop 
num =abs(int(input("enter the number:")))
digits =1
while(num>10):
    num = num // 10
    digits = digits + 1
print(digits)


#problem 2.find the number of digits in the given number using for loop
num =abs(int(input("enter the number:")))
strNum = str(num)
digits = 0
for c in strNum:
    digits = digits +1
print(digits)
'''
'''
#problem 3.reverse the digits in the given number using while loop
num = int(input("enter the number:"))
absNum = abs(num)
rev = absNum % 10
absNum = absNum //10
while(absNum>0):
    r = absNum % 10
    absNum = absNum//10
    rev = rev * 10 + r
if(num > 0):
    print(rev)
else:
    print(rev - 2* rev)


#problem 3.reverse the digits in the given number using for loop

num = int(input("enter the number:"))
absNum = str(abs(num))
rev =''
for c in absNum:
    rev = c + rev
if (num>= 0):
    print(rev)
else:
    print('-' + rev)
'''

#problem 5. find whether the entered numbre is palindrome or not

#Find the factorial of the given number
'''
fac =int(input())
answer =1
if(0>fac):
    print('not valied')
else:
    while(0<fac):
        answer = answer*i
        fac=fac+1
    print(answer)

'''
#Find the number of digits in the given number
'''
num = abs(int(input()))
digits =1
while(9<num):
    num = num/10
    digits = digits+1
print(digits)

'''

#reverse the digits in the given number
'''

num=int(input())
absnum =abs(num)
rev=absnum %10
absnum=absnum//10
while(absnum>0):
    r=absnum%10
    absnum=absnum//10
    rev =rev*10+r
if(num>=0):
    print(rev)
else:
    print(rev -2 * rev)

'''

#find whether the entered number is palindrome or not?


num=int(input())
absnum =abs(num)
rev=absnum %10
absnum=absnum//10
while(absnum>0):
    r=absnum%10
    absnum=absnum//10
    rev =rev*10+r
if(num<0):
    rev = rev-2*rev
if(num==rev):
    print('palindrome')
else:
    print('non-palindrone')
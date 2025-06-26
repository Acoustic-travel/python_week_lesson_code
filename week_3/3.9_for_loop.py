'''

for x in range(1,10):
    print(x, end=' ')
'''
'''
d=10
m=5
y=2021
print("Today's date is ",end='')
print(d,m,y,sep ='/')

'''

'''

num = int(input())
for i in range(1,11):
    print(f'{num} X {i}={num * i}')

'''
'''

pi =22/7
print(f'value of PI={pi}')
print(f'value of PI={pi:.3f}')
print('value of PI={0:.2f}'.format(pi))
print('value of PI=%f' %(pi))

'''
'''

print('{0}'.format(1))
print('{0}'.format(11))
print('{0}'.format(111))
print('{0}'.format(1111))
print('{0}'.format(11111))
print('{0:5d}'.format(1))
print('{0:5d}'.format(11))
print('{0:5d}'.format(111))
print('{0:5d}'.format(1111))
print('{0:5d}'.format(11111))
print('{0:5d}'.format(111111))
'''
# Print increasing numbers: 1, 11, 111, ...
print("Without formatting:")
num = 0
for i in range(1, 6):  # 5 times
    num = num * 10 + 1
    print('{0}'.format(num))

print("\nWith formatting (right aligned in width 5):")
num = 0
for i in range(1, 7):  # 6 times
    num = num * 10 + 1
    print('{0:5d}'.format(num))
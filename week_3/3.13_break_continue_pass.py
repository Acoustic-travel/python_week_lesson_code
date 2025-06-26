#break
'''
email=input()
for c in email:
    if(c=='@'):
        break
    print(c,end='')
'''
'''
#continue
email=input()
for c in email:
    if(c =='@'):
        print('')
        continue
    print(c,end='')

'''

#pass
'''
for x in range(11):
    if(x % 3==0):
        print(x)
    else:
        pass

'''
num = int(input())
i = num
result = 0
while True:
    i -= 5
    if i>15:
        continue
    if i<-15:
        break
    result -= i
print(result)
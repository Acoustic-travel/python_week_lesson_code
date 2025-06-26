#find all prime number less than the entered numbers
'''
n=int(input("enter the number:"))

if (n>2):
    print(2, end =' ')
for i in range(3,n):
    flag=False
    for j in range(2, i):
        if (i%j==0):
            flag=False
            break
        else:
            flag=True
    if(flag):
        print(i,end=' ')

'''

#problem 2 find the total profit/loss of each trader working 
# in a trading firm. information regarding number of traders and numbers of transactions is unknown.
'''
empID=input("Enter employee id:")
while(empID!= '-1'):
    trade = int(input('Enter the trade amount:'))
    profit_loss = 0
    while(trade != 0):
        profit_loss = profit_loss +trade
        trade = int(input('Enter the trade amount:'))
    print(f'profit/loss for employee{empID} is {profit_loss}')
    empID =input('\nEnter employee ID:')

    '''
'''
#problem 3 find the day wise total rainfall for the enterd 
# durations of time e.g week , month etc
days = int(input('enter the number of dyas: '))
for i in range(1,days+1):
    total =0
    rainfall =int(input('enter the rainfall: '))
    while(rainfall != -1):
        total = total +rainfall
        rainfall = int(input('enter the raianfall:'))
    print('Total rainfall for day{0} is {1}'.format(i,total))
'''

#problem 4 find the length of longest word from the set of words entered by the user

word = input('enter a word:')
maxLen = 0
while(word != '-1'):
    count =0
    for letter in word:
        count = count + 1
    if(count > maxLen):
        maxLen = count
    word = input('enter a word:')
print('the lenth of lonest word %s'%maxLen)
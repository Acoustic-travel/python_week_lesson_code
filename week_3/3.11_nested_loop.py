s='VIBGYOR'
t='VIBGYOR'

#example of a nested for loop
count=0
for i in range(7):
    for j in range(7):
        print(i,j,s[i],s[j])
        count = count+1
print("The total way in which the two brothers can wear 7 diffrent colours:",count)
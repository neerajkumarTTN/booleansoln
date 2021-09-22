list=[2,3,4,5,6,7,8,9,10]
count=0
sum=0
for i in list:
    if( i%2==0):
        count+=1
        sum+=i
print(count)
print(sum)
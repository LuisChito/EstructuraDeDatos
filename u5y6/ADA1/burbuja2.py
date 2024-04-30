val = [1,3,5,4,7,2,9,8,6,10,11,14,12,44,22,15,18,20,19]
num = len(val)
i= 0
while (i < num):
    x = i
    while (x < num):
        if(val[i] > val[x]):
            temp = val[i]
            val[i] = val[x]
            val[x] = temp
        x= x+1
    i=i+1
 
for val in val:
    print (val)
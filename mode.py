import math

x=[2,3,5,2,2,4,5,3,4,4,6]
print("SUM=>",sum(x))
print("MEAN=>",sum(x)/len(sum))
if len(x) % 2 == 0:
    x.sort()
    idx = len(x)/2
    value = x[idx] + x[idx+1]
    print("median=>",value/2)
else:
    value = x[len(x)//2 + 1]
    print("median=>",value/2)
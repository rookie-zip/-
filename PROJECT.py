from math import sqrt
flag=1
for i in range(101,200):
    for j in range(2,int(sqrt(i)+1)):
        if i%j==0:
            flag=0
            break
    if flag==1:
        print("素数是{}".format(i))
    flag =1

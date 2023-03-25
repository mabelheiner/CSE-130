num = 30;
count = 0;

for j in range(2,num+1):
    if ((num - (num / j) * j) == 0):
        count+=1
        print(j, "not prime")
    else:
        print("prime: ", j)

if (count == 0):
    print(num + "is Prime");
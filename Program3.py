# Check Prime Number

num=3 
if num>1:
    for i in range (2,num):
        if num%i==0:
            print(num,"Not Prime")
            break
    else:
        print(num,"Not prime")
else:
    print("Not prime")

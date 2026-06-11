# check palindrome number
num=151
temp=num
reverse=0
while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num//=10
if temp==reverse:
     print("is a palindrome")
else:
    print(" not palindrome")

#Write a python script to print first 10 odd natural numbers in reverse order
n=int(input("enter any number "))
i=(2*n)-1
while i>=1:
    print(i,end=' ')
    i-=2

#Write a python script to print first 10 even natural numbers in reverse order
n=int(input("enter a number "))
i=2*n
while i>=1:
    print(i,end=' ')
    i-=2

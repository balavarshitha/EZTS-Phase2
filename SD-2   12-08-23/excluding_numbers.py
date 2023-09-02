'''write a program to print numbers from 1-100 excluding (10,22,99,97,25,44)'''
n= {10, 22, 99, 97, 25, 44}

for num in range(1, 101):
    if num not in n:
        print(num,end=' ')

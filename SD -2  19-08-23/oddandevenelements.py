'''the function accepts an integers arr of size 'length' as its arguments you are required to return the sum of second largest element
from the even positions and secong smallest from the odd position of given 'arr'.
ASSUMPTION:
all the array elements are unique
treat the 0th position as even
NOTE:
Return 0 ,if array is empty
return 0, if array length is 3 or less than 3'''

length=int(input())
Arr=list(map(int,input().split()))
Even_arr=[]
Odd_arr=[]
for i in range(length):
    if i%2==0:
        Even_arr.append(arr[i])
    else:
        Odd_arr.append(arr[i])
    Even_arr=sorted(even_arr)
    Odd_arr=sorted(Odd_arr)
print(Even_arr[len(Even_arr)-2]+Odd_arr[len(Odd_arr)-2])

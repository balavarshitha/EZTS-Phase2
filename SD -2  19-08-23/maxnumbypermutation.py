'''execute a function that accepts the integer array of length 'size' and finds out the maximum number that can be formed
by permutation
note: you will have to rearrange the numbers to make the maximum number'''

def max_permutation(arr):
    arr_str=[str(num)for num in arr]
    arr_str.sort(reverse=True,key=lambda x:x*3)
    max_number=''.join(arr_str)
    return max_number
input_str=input("input:")
input_arr=list(map(int,input_str.split()))
output=max_permutation(input_arr)
print("output",output)

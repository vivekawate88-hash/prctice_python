# i = 1
# c = 0
# while i <= 10:
#     c+=1
#     i+=1

# print(c)

# n=int(input('enter a number:'))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)

arr = [2,4,8,9,1,5,6,8,5]
def divide(arr):
    if len(arr)<=1:
        return 
    mid = len(arr)//2
    left = arr[:mid:1]
    right = arr[mid:]
    print(left,right)
    divide(left)
    divide(right)
divide(arr)


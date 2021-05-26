# to_sort=input("input list element separated by space\n").split()

# #change each element to intiger using map function
# to_sort=list(map(int,to_sort)) 

# #sort function sort unsorted list
# to_sort.sort()  

# print(to_sort)                           
# to_find=int(input("which element to find using binary search\n"))
# min=0
# max=len(to_sort)-1

# #implementing binary search 
# while min<=max:
#     mean=int((min+max)//2)
#     if to_sort[mean]==to_find:
#         print(f"element found at index {mean}")
#     elif to_sort[mean]<= to_find:
#         min=mean+1
#     elif to_sort[mean]>= to_find:
#         max=mean-1

#input a list and sort it in ascending order
to_sort=input("input list element with space in between\n").split()
to_sort.sort()
print(f"the sorted string is {to_sort}")
n=input("input element which you want to find from the list.\n") 

#searching algo in function where it returns -1 if false
def binary_search(to_sort, n):  
    min = 0  
    max = len(to_sort) - 1   
    
    #comparing element and using loop to find the element
    while min <= max: 
        mean = (min + max) // 2
        if to_sort[mean]==n:
            return mean
        elif to_sort[mean] < n:  
            min = mean + 1
        elif to_sort[mean] > n:  
            max = mean - 1 
        else:  
            print("not found")
    return -1  


ans = binary_search(to_sort, n)  
    
if ans!=-1:  
    print(f"Element is in index {ans}")  
else:  
    print("Element not found in given list")   





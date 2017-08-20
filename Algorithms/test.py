import sys
import timeit
import random

def merge_sort(lst):
   mid = len(lst)//2 
   lft, rght = lst[:mid], lst[mid:]
   if len(lft) > 1: lft = merge_sort(lft) 
   if len(rght) > 1: rght = merge_sort(rght)
   sorted_list = []
   while lft and rght:
       if lft[-1] <= rght[-1]:
           sorted_list.append(lft.pop())
       else:
           sorted_list.append(rght.pop())
   sorted_list.reverse()
   return (lft or rght) +    sorted_list



if __name__ == "__main__":
    #arr = inputArray()
    arr = random.sample(range(-1000000, 1000000), 200000)

    start_time = timeit.default_timer()
    sortedArr = merge_sort(arr)
    stopt_time = timeit.default_timer()
    print(stopt_time - start_time)

    #print('Merge Sorted list:',sortedArr)
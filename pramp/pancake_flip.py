def flip(arr, k):
  result = []
  for i,index in enumerate(range(k, -1, -1)):
    result.append(arr[index])
  for i in range(k+1, len(arr)):
      result.append(arr[i])
  return result

def pancake_sort(arr):
  back_step = len(arr)-1
  while back_step > 0:
    max_value = arr[0]
    max_value_index = 0
    for i in range(back_step+1):
      if max_value < arr[i]:
        max_value = arr[i]
        max_value_index = i
    if max_value_index > 0:
      arr = flip(arr,max_value_index)
      arr = flip(arr,back_step)
      back_step -=1
    elif max_value_index == 0:
      arr = flip(arr,back_step)
      back_step -=1
  return arr
  

arr = [1 ,2 ,8 ,100, 5 ,6, 9]
k = 4

print pancake_sort(arr)


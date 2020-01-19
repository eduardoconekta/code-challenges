def array_of_array_products_without_division(arr):
  result = [1] * len(arr)
  if len(arr) <= 1:
    return []
  for index1 in range(len(arr)):
    for index2 in range(len(arr)):
      if index1 != index2: 
          result[index1] *= arr[index2]
  return result 

def get_product(arr):
  product = 1 
  for i in arr:
    if i != 0: 
      product *= i
  return product

def array_of_array_products_division(arr):
  product = get_product(arr)
  zero_counter = 0
  zero_index = 0
  result = arr
  for i in range(len(arr)):
    # if zero exists 
    if arr[i] == 0:
      zero_counter+=1
      zero_index =i
  
  if zero_counter > 1:
    return [0] * len(arr)
  if zero_index:
    print zero_index
    arr = [0] * len(arr)
    arr[zero_index] = product
    return arr
    
  for i in range(len(arr)):
    result[i] = product/arr[i] 

  return result

test_case_1 = [8, 10, 2]
test_case_2 = [8, 0, 2]

array_of_array_products_division(test_case_1)
# [20, 16, 80]
array_of_array_products_division(test_case_2)
# [0 , 16, 0]
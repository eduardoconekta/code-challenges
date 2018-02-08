class SelectionSort(object):
  def sort(self, obj):
    if obj[ 0 ] > obj[ 1 ]:
      tmp      = obj[ 0 ]
      obj[ 0 ] = obj[ 1 ]
      obj[ 1 ] = tmp
    else:
      tmp      = obj[ 1 ]
      obj[ 1 ] = obj[ 0 ]
      obj[ 0 ] = tmp
    
    for i in range(len(obj)):  
      count = 0
      for j in range(len(obj)): # (16), [27] 
        if obj[ i ] < obj[ j + count ]:
          tmp      = obj[ j + count ] 
          obj[ j + count ] = obj[ i ] 
          obj[ i ] = tmp  
        break
      count = count + 1

    return obj

     
  def __init__(self, arg=None):
    super(SelectionSort, self).__init__()
    self.arg = arg

arr_sample = [27,16,44,10,7]
selection = SelectionSort()
result = selection.sort(arr_sample)
print(result)



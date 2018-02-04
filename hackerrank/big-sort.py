
class BigSort(object):
  def numeric_validation(self, obj ):
    for number in obj:
      if not isinstance(number, int):
        return False
    return True

  def sort_numbers( self, obj ):
    if not self.numeric_validation(obj): return False 
    total_len = len(obj) - 1
    for i in range(total_len):
      if not self.array_sorted(obj):
        for j in range(total_len):
          if obj[ j ] > obj[ j + 1 ]:
            tmp          = obj[ j ]
            obj[ j ]     = obj[ j + 1 ]
            obj[ j + 1 ] = tmp
    return obj

  def array_sorted(self, obj):
    for i in range(len(obj) - 1 ):
      if obj[ i ] > obj[ i + 1]:
        return False
    return True
        
     
  def __init__(self, arg=None):
    super(BigSort, self).__init__()
    self.arg = arg

unsort_numbers = [31415926535897932384626433832795,1,3,10,3,5]
b_sort = BigSort()
print(b_sort.sort_numbers(unsort_numbers))
class FullCountingSort(object):
  def print_words(self,obj):
    copy_of_object  = obj.split('\n')
    original_object = obj.split('\n')
    index           = int(original_object.pop(0))
    middle_len      = index/2

    copy_of_object.pop(0) #pop index reference 20
    self.order(copy_of_object, index)

    for i in range(middle_len):
      for j in range(index):
        if original_object[ i ] == copy_of_object[ j ] :
          copy_of_object[j] = '-'

    return copy_of_object

  def order(self, obj, index):
    for i in range(index):
      for j in range(index-1):
        if obj[ j ].split(' ')[0] > obj[ j + 1 ].split(' ')[0]: 
          tmp          = obj[ j ]
          obj[ j ]     = obj[ j + 1 ]
          obj[ j + 1 ] = tmp        
    return obj

  def __init__(self, arg=None):
    super(FullCountingSort, self).__init__()
    self.arg = arg



full_csort = FullCountingSort()
f = open("./test-entries/full-counting.txt").read()
result = full_csort.print_words(f)

# just print
for i in result:
  print(i.split(' ')[-1]),
print
  

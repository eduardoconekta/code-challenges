from time import sleep
class BinarySort(object):
  def sort(self, obj, key):
    mid = (len(obj)/2) + (len(obj) % 2)
    while True:
        if obj[mid] == key:
            break
        elif key < obj[mid]: 
            # print "{} < {}".format(key,obj[mid])
            min = mid - mid
            mid = (len(obj[min:mid])/2) + (len(obj[min:mid]) % 2)
        elif  key > obj[mid]:  
            # print "{} > {}".format(key,obj[mid])
            max = (len(obj[mid:len(obj)]) / 2) + (len(obj[mid:len(obj)]) % 2)
            mid += max
    return obj[mid]

     
  def __init__(self, arg=None):
    super(BinarySort, self).__init__()
    self.arg = arg



arr = [0,1,2,4,4,5,6,7,8,9]
key = 9
binary = BinarySort() 
print binary.sort(arr,key)